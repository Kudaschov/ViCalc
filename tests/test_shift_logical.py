import os
import math
import pytest
from PySide6.QtCore import Qt, QEventLoop
from vicalc.AppGlobals import AppGlobals
from vicalc.vicalc import MainWindow
from vicalc.CalcMode import CalcMode
from vicalc.CalcOperations import CalcOperations
from vicalc.WordSize import WordSize
from vicalc.NumberBase import NumberBase
from vicalc.ShiftRotateOperation import ShiftRotateOperation


@pytest.fixture
def main_window(qtbot):
    """Fixture to initialize and display the main application window."""
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    return window


def wait_for_manual_close(window):
    """Keep the window open and wait until the user closes it manually (e.g., via Alt+F4)."""
    loop = QEventLoop()
    window.destroyed.connect(loop.quit)
    loop.exec()


@pytest.mark.parametrize(
    "key_sequence, expected_int",
    [
        # --- BYTE (8-Bit) ---
        # Case 1: LshL 0b10100010 << 1 = 0b01000100 (162 << 1 = 324 -> masked 8-bit = 68)
        (
            ["A2", lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift), "1="],
            68,
        ),
        # Case 2: LshR 0b10100010 >> 2 = 0b00101000 (0xA2 >> 2 = 0x28 = 40) - Zero extension (not sign extension)
        (
            ["A2", lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift), "2="],
            40,
        ),
        # Case 3: LshR 0b01010001 >> 2 = 0b00010100 (0x51 >> 2 = 0x14 = 20)
        (
            ["51", lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift), "2="],
            20,
        ),
        # Case 4: LshL 0b10100011 << 1 = 0b01000110 (0xA3 << 1 = 0x46 = 70)
        (
            ["A3", lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift), "1="],
            70,
        ),

        # --- WORD (16-Bit) ---
        # Case 5: LshL 0xA2 << 1 = 0x0144 (324) - Word size expands bit capacity to 16 bits
        (
            [
                "A2",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "1=",
            ],
            324,
        ),
        # Case 6: LshR 0x8000 >> 2 = 0x2000 (8192) - MSB is 1, but filled with 00 (Zero Extension)
        (
            [
                "8000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            8192,
        ),
        # Case 7: LshR 0x7000 >> 2 = 0x1C00 (7168) - MSB is 0, filled with 00
        (
            [
                "7000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            7168,
        ),
        # Case 8: LshL 0x00FF << 4 = 0x0FF0 (4080)
        (
            [
                "FF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "4=",
            ],
            4080,
        ),
        # Case 9: LshL 0x8001 << 1 = 0x0002 (2) - Overflow beyond 16 bits
        (
            [
                "8001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "1=",
            ],
            2,
        ),

        # --- DWORD (32-Bit) ---
        # Case 10: LshL 0x0000FFFF << 4 = 0x000FFFF0 (1048560)
        (
            [
                "FFFF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "4=",
            ],
            1048560,
        ),
        # Case 11: LshR 0x80000000 >> 2 = 0x20000000 (536870912) - MSB is 1, filled with 00 (Zero Extension)
        (
            [
                "80000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            536870912,
        ),
        # Case 12: LshR 0x70000000 >> 2 = 0x1C000000 (469762048)
        (
            [
                "70000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            469762048,
        ),
        # Case 13: LshL 0x80000001 << 1 = 0x00000002 (2) - Overflow beyond 32 bits
        (
            [
                "80000001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "1=",
            ],
            2,
        ),

        # --- QWORD (64-Bit) ---
        # Case 14: LshL 0x00000000FFFFFFFF << 4 = 0x0000000FFFFFFFF0 (68719476720)
        (
            [
                "FFFFFFFF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "4=",
            ],
            68719476720,
        ),
        # Case 15: LshR 0x8000000000000000 >> 2 = 0x2000000000000000 (2305843009213693952) - Zero Extension on 64 bits
        (
            [
                "8000000000000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            2305843009213693952,
        ),
        # Case 16: LshR 0x7000000000000000 >> 2 = 0x1C00000000000000 (2017612633061982208)
        (
            [
                "7000000000000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            2017612633061982208,
        ),
        # Case 17: LshL 0x8000000000000001 << 1 = 0x0000000000000002 (2) - Overflow beyond 64 bits
        (
            [
                "8000000000000001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "1=",
            ],
            2,
        ),
    ],
)
def test_logical_bitwise_shift(
    main_window, qtbot, key_sequence, expected_int
):
    """Test logical bitwise shift operations across various word sizes."""
    input_box = AppGlobals.input_box
    input_imag_box = AppGlobals.input_imag_box

    original_calc_mode = AppGlobals.calc_mode
    AppGlobals.calc_mode = CalcMode.base_n
    original_word_size = AppGlobals.current_word_size
    AppGlobals.current_word_size = WordSize.BIT8
    original_number_base = AppGlobals.number_base
    AppGlobals.number_base = NumberBase.HEX
    original_bitwise_shift = AppGlobals.bitwise_shift
    AppGlobals.bitwise_shift = ShiftRotateOperation.logical

    input_box.button_clicked(CalcOperations.number_base_hexadecimal)
    main_window.update_keyboard()

    assertion_error = None

    try:
        qtbot.wait(50)
        input_box.clear()
        input_imag_box.clear()
        input_box.setFocus()
        qtbot.wait(50)

        for item in key_sequence:
            focus_widget = main_window.focusWidget() or input_box

            if callable(item):
                item()
            elif isinstance(item, Qt.Key):
                qtbot.keyClick(focus_widget, item)
            elif isinstance(item, str) and len(item) > 1:
                qtbot.keyClicks(focus_widget, item)
            else:
                qtbot.keyClick(focus_widget, item)

            qtbot.wait(20)

        qtbot.wait(50)

        int_val = int(input_box.text(), 16)

        try:
            assert int_val == expected_int
        except AssertionError as err:
            assertion_error = err

    finally:
        # Keep window open for manual inspection if needed:
        # wait_for_manual_close(main_window)

        # Restore original global state
        AppGlobals.calc_mode = original_calc_mode
        AppGlobals.current_word_size = original_word_size
        AppGlobals.number_base = original_number_base
        AppGlobals.bitwise_shift = original_bitwise_shift

        if assertion_error:
            raise assertion_error