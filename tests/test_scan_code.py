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

def send_unicode(s):
    i = INPUT()
    i.type = INPUT_KEYBOARD
    # Handles non-BMP code points by sending UTF-16 code units.
    for c in array.array('H', s.encode('utf-16le')):
        i.ki = KEYBDINPUT(0, c, KEYEVENTF_UNICODE, 0, 0)
        SendInput(1, ct.byref(i), ct.sizeof(INPUT))
        i.ki.dwFlags |= KEYEVENTF_KEYUP
        SendInput(1, ct.byref(i), ct.sizeof(INPUT))

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    return window

def test_typing(main_window, qtbot):
    print("TEST: scan_code 3, should produce '2' character in input box")
    input_box = AppGlobals.input_box
    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    # Qt Key Simulation
    # simulate_key(main_window, Qt.Key_A, "a")

    # Windows scan_code Simulation (z. B. 'A' = 0x1E)
    send_scancode(3)

    qtbot.wait(50)

    # Hier prüfen wir z. B. Textfeld
    assert input_box.text() == "2"

    if os.getenv("VICALC_DEBUG"):
        qtbot.wait(10_000)