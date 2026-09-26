import pytest
import time
import os
import ctypes as ct
import ctypes.wintypes as w

from vicalc.vicalc import MainWindow
from PySide6.QtWidgets import QApplication
from vicalc.AppGlobals import AppGlobals
from vicalc.NumberBase import NumberBase
from vicalc.WordSize import WordSize
from vicalc.CalcMode import CalcMode

# --- Win32 DirectInput API Mappings ---
KEYEVENTF_SCANCODE = 0x8
KEYEVENTF_KEYUP = 0x2
INPUT_KEYBOARD = 1
ULONG_PTR = ct.c_size_t

class KEYBDINPUT(ct.Structure):
    _fields_ = [
        ('wVk', w.WORD),
        ('wScan', w.WORD),
        ('dwFlags', w.DWORD),
        ('time', w.DWORD),
        ('dwExtraInfo', ULONG_PTR)
    ]

class MOUSEINPUT(ct.Structure):
    _fields_ = [
        ('dx', w.LONG),
        ('dy', w.LONG),
        ('mouseData', w.DWORD),
        ('dwFlags', w.DWORD),
        ('time', w.DWORD),
        ('dwExtraInfo', ULONG_PTR)
    ]

class HARDWAREINPUT(ct.Structure):
    _fields_ = [
        ('uMsg', w.DWORD),
        ('wParamL', w.WORD),
        ('wParamH', w.WORD)
    ]

class DUMMYUNIONNAME(ct.Union):
    _fields_ = [
        ('mi', MOUSEINPUT),
        ('ki', KEYBDINPUT),
        ('hi', HARDWAREINPUT)
    ]

class INPUT(ct.Structure):
    _anonymous_ = ['u']
    _fields_ = [
        ('type', w.DWORD),
        ('u', DUMMYUNIONNAME)
    ]

def zerocheck(result, func, args):
    if result == 0:
        raise ct.WinError(ct.get_last_error())
    return result

user32 = ct.WinDLL('user32', use_last_error=True)
SendInput = user32.SendInput
SendInput.argtypes = w.UINT, ct.POINTER(INPUT), ct.c_int
SendInput.restype = w.UINT
SendInput.errcheck = zerocheck

# --- Windows Keyboard Helpers ---
def send_key_press(scancode):
    i = INPUT()
    i.type = INPUT_KEYBOARD
    i.ki = KEYBDINPUT(0, scancode, KEYEVENTF_SCANCODE, 0, 0)
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))

def send_key_release(scancode):
    i = INPUT()
    i.type = INPUT_KEYBOARD
    i.ki = KEYBDINPUT(0, scancode, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0, 0)
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))

def send_ctrl_less():
    """Simulates hardware-level key press for Ctrl + <."""
    SCAN_CTRL = 0x1D  # Left Control Scan Code
    SCAN_LESS = 0x56  # '<' Scan Code on German keyboards

    send_key_press(SCAN_CTRL)
    time.sleep(0.02)

    send_key_press(SCAN_LESS)
    time.sleep(0.02)
    send_key_release(SCAN_LESS)
    time.sleep(0.02)

    send_key_release(SCAN_CTRL)

def send_key_not():
    """Simulates hardware-level key press for Bitwise NOT ('T' key alone)."""
    SCAN_T = 0x14     # Scan Code 20 (0x14) for 'T'
    VK_T = 0x54       # Virtual Key Code for 'T'

    i = INPUT()
    i.type = INPUT_KEYBOARD
    i.ki = KEYBDINPUT(VK_T, SCAN_T, KEYEVENTF_SCANCODE, 0, 0)
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))
    time.sleep(0.02)

    i.ki.dwFlags |= KEYEVENTF_KEYUP
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))
    time.sleep(0.02)

def send_ctrl_six():
    """Simulates hardware-level key press for Ctrl + 6 (Bitwise XOR)."""
    SCAN_CTRL = 0x1D  # Left Control Scan Code
    SCAN_SIX = 0x07   # '6' Scan Code on main numrow
    VK_SIX = 0x36     # Virtual Key Code for '6'

    send_key_press(SCAN_CTRL)
    time.sleep(0.02)

    i = INPUT()
    i.type = INPUT_KEYBOARD
    i.ki = KEYBDINPUT(VK_SIX, SCAN_SIX, KEYEVENTF_SCANCODE, 0, 0)
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))
    time.sleep(0.02)

    i.ki.dwFlags |= KEYEVENTF_KEYUP
    SendInput(1, ct.byref(i), ct.sizeof(INPUT))
    time.sleep(0.02)

    send_key_release(SCAN_CTRL)

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    return window

@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["11001&11100="], "00011000"),    # AND
        (["11010|10100="], "00011110"),    # OR
        (["10110~"], "11101001"),       # NOT
        
        # Hardware shortcut test: Ctrl + < (Bitwise OR)
        (
            [
                "11010",
                "CTRL_LESS",
                "10100="
            ],
            "00011110"
        ),

        # Hardware key test: T (Bitwise NOT) -> ~10110 (8-bit) = 11101001
        (
            [
                "10110",
                "KEY_T"
            ],
            "11101001"
        ),

        # Hardware shortcut test: Ctrl + 6 (Bitwise XOR) -> 11010 ^ 10100 = 01110
        (
            [
                "11010",
                "CTRL_SIX",
                "10100="
            ],
            "00001110"
        ),
    ],
)

def test_calculator_expressions(main_window, qtbot, inputs, expected):
    input_box = AppGlobals.input_box

    original_calc_mode = AppGlobals.calc_mode
    AppGlobals.calc_mode = CalcMode.base_n
    original_base = AppGlobals.number_base
    AppGlobals.number_base = NumberBase.BIN
    original_word_size = AppGlobals.current_word_size
    AppGlobals.current_word_size = WordSize.BIT8
    main_window.update_keyboard()

    try:
        input_box.clear()
        input_box.setFocus()
        main_window.activateWindow()
        qtbot.wait(100)

        for item in inputs:
            if item == "CTRL_LESS":
                send_ctrl_less()
                QApplication.processEvents()
                qtbot.wait(50)
            elif item == "KEY_T":
                send_key_not()
                QApplication.processEvents()
                qtbot.wait(50)
            elif item == "CTRL_SIX":
                send_ctrl_six()
                QApplication.processEvents()
                qtbot.wait(50)

            elif isinstance(item, str):
                qtbot.keyClicks(input_box, item)

        qtbot.waitUntil(lambda: input_box.text() == expected, timeout=1000)
    finally:
        AppGlobals.number_base = original_base
        AppGlobals.current_word_size = original_word_size
        AppGlobals.calc_mode = original_calc_mode