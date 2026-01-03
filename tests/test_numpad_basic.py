import pytest
from vicalc.vicalc import MainWindow
from PySide6.QtWidgets import QApplication
from vicalc.AppGlobals import AppGlobals
from PySide6.QtCore import QCoreApplication
import os
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
import ctypes
from ctypes import wintypes
from PySide6.QtGui import QKeyEvent
import sys
import time

# Source - https://stackoverflow.com/a
# Posted by Mark Tolonen, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-02, License - CC BY-SA 4.0

import ctypes as ct
import ctypes.wintypes as w
import struct
import time
import array

KEYEVENTF_SCANCODE = 0x8
KEYEVENTF_UNICODE = 0x4
KEYEVENTF_KEYUP = 0x2
SPACE = 0x39
INPUT_KEYBOARD = 1

# not defined by wintypes
ULONG_PTR = ct.c_size_t

class KEYBDINPUT(ct.Structure):
    _fields_ = [('wVk' , w.WORD),
                ('wScan', w.WORD),
                ('dwFlags', w.DWORD),
                ('time', w.DWORD),
                ('dwExtraInfo', ULONG_PTR)]

class MOUSEINPUT(ct.Structure):
    _fields_ = [('dx' , w.LONG),
                ('dy', w.LONG),
                ('mouseData', w.DWORD),
                ('dwFlags', w.DWORD),
                ('time', w.DWORD),
                ('dwExtraInfo', ULONG_PTR)]

class HARDWAREINPUT(ct.Structure):
    _fields_ = [('uMsg' , w.DWORD),
                ('wParamL', w.WORD),
                ('wParamH', w.WORD)]

class DUMMYUNIONNAME(ct.Union):
    _fields_ = [('mi', MOUSEINPUT),
                ('ki', KEYBDINPUT),
                ('hi', HARDWAREINPUT)]

class INPUT(ct.Structure):
    _anonymous_ = ['u']
    _fields_ = [('type', w.DWORD),
                ('u', DUMMYUNIONNAME)]

print(ct.sizeof(INPUT))

def zerocheck(result, func, args):
    if result == 0:
        raise ct.WinError(ct.get_last_error())
    return result

user32 = ct.WinDLL('user32', use_last_error=True)
SendInput = user32.SendInput
SendInput.argtypes = w.UINT, ct.POINTER(INPUT), ct.c_int
SendInput.restype = w.UINT
SendInput.errcheck = zerocheck

def send_scancode(code):
    i = INPUT()
    i.type = INPUT_KEYBOARD
    i.ki = KEYBDINPUT(0, code, KEYEVENTF_SCANCODE, 0, 0)
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))
    i.ki.dwFlags |= KEYEVENTF_KEYUP
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))

def send_scancode_down(code):
    i = INPUT()
    i.type = INPUT_KEYBOARD
    i.ki = KEYBDINPUT(0, code, KEYEVENTF_SCANCODE, 0, 0)
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))

def send_scancode_up(code):
    i = INPUT()
    i.type = INPUT_KEYBOARD
    i.ki = KEYBDINPUT(0, code, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0, 0)
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    return window

def test_addition(main_window, qtbot):
    input_box = AppGlobals.input_box
    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    assert input_box.numlock_state() == True

    data = [81, 75, 83, 76, 78]
    for code in data:
        send_scancode(code) # 34.5+
        qtbot.wait(20)
    qtbot.wait(50)
    
    send_scancode_down(42) # Left Shift down
    qtbot.wait(50)

    send_scancode(74)  # (-) sign
    qtbot.wait(50)

    send_scancode_up(42) # Left Shift up
    qtbot.wait(50)

    data2 = [77, 83, 71, 72, 57372] # 6.78 Enter
    for code in data2:
        send_scancode(code)
        qtbot.wait(20)

    assert input_box.text() == "27.72"

def test_subtraction(main_window, qtbot):
    # 90 - 12 = 78
    input_box = AppGlobals.input_box
    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    assert input_box.numlock_state() == True

    data = [73, 82, 74]
    for code in data:
        send_scancode(code) # 90-
        qtbot.wait(20)
    qtbot.wait(50)
    
    data2 = [79, 80, 57372] # 12 Enter
    for code in data2:
        send_scancode(code)
        qtbot.wait(20)

    assert input_box.text() == "78"

def test_multiplication(main_window, qtbot):
    # 12 * 34 = 408    

    input_box = AppGlobals.input_box
    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    assert input_box.numlock_state() == True

    data = [79, 80, 55] # 27
    for code in data:
        send_scancode(code) # 12*
        qtbot.wait(20)

    # send_scancode(57397) # / From some reason this does not work
    # qtbot.keyClick(input_box, Qt.Key_Slash)
    qtbot.wait(50)
    
    data2 = [81, 75, 57372] # 34 Enter
    for code in data2:
        send_scancode(code)
        qtbot.wait(20)

    assert input_box.text() == "408"

def test_division(main_window, qtbot):
    #27 / 12 = 2.25    

    input_box = AppGlobals.input_box
    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    assert input_box.numlock_state() == True

    data = [80, 71] # 27
    for code in data:
        send_scancode(code) # 90
        qtbot.wait(20)

    # send_scancode(57397) # / From some reason this does not work
    qtbot.keyClick(input_box, Qt.Key_Slash)
    qtbot.wait(50)
    
    data2 = [79, 80, 57372] # 12 Enter
    for code in data2:
        send_scancode(code)
        qtbot.wait(20)

    assert input_box.text() == "2.25"

    if os.getenv("VICALC_DEBUG"):
        qtbot.wait(10_000)