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
        # Case 1: ROL 0xA2 (0b10100010) << 1 = 0b01000101 (0x45 = 69) - MSB '1' wraps around to LSB
        (
            [
                "A2",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            69,
        ),
        # Case 2: ROR 0xA3 (0b10100011) >> 1 = 0b11010001 (0xD1 = 209) - LSB '1' wraps around to MSB
        (
            [
                "A3",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            209,
        ),
        # Case 3: ROR 0x51 (0b01010001) >> 1 = 0b10101000 (0xA8 = 168) - LSB '1' wraps around to MSB
        (
            [
                "51",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            168,
        ),
        # Case 4: ROL 0x81 (0b10000001) << 1 = 0b00000011 (0x03 = 3) - MSB '1' wraps around to LSB
        (
            [
                "81",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            3,
        ),

        # --- WORD (16-Bit) ---
        # Case 5: ROL 0x8001 << 1 = 0x0003 (3) - Bit 15 ('1') wraps around to Bit 0
        (
            [
                "8001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            3,
        ),
        # Case 6: ROR 0x0001 >> 1 = 0x8000 (32768) - Bit 0 ('1') wraps around to Bit 15
        (
            [
                "1",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            32768,
        ),

        # --- DWORD (32-Bit) ---
        # Case 7: ROL 0x80000001 << 1 = 0x00000003 (3) - Bit 31 ('1') wraps around to Bit 0
        (
            [
                "80000001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            3,
        ),
        # Case 8: ROR 0x00000001 >> 1 = 0x80000000 (2147483648) - Bit 0 ('1') wraps around to Bit 31
        (
            [
                "1",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            2147483648,
        ),

        # --- QWORD (64-Bit) ---
        # Case 9: ROL 0x8000000000000001 << 1 = 0x0000000000000003 (3) - Bit 63 ('1') wraps around to Bit 0
        (
            [
                "8000000000000001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            3,
        ),
        # Case 10: ROR 0x0000000000000001 >> 1 = 0x8000000000000000 (9223372036854775808) - Bit 0 ('1') wraps to Bit 63
        (
            [
                "1",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            9223372036854775808,
        ),
    ],
)
def test_circular_bitwise_shift(
    main_window, qtbot, key_sequence, expected_int
):
    """Test circular bitwise shift (rotation) operations across various word sizes."""
    input_box = AppGlobals.input_box
    input_imag_box = AppGlobals.input_imag_box

    original_calc_mode = AppGlobals.calc_mode
    AppGlobals.calc_mode = CalcMode.base_n
    original_word_size = AppGlobals.current_word_size
    AppGlobals.current_word_size = WordSize.BIT8
    original_number_base = AppGlobals.number_base
    AppGlobals.number_base = NumberBase.HEX
    original_bitwise_shift = AppGlobals.bitwise_shift
    AppGlobals.bitwise_shift = ShiftRotateOperation.circular

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
        # Restore original global state
        AppGlobals.calc_mode = original_calc_mode
        AppGlobals.current_word_size = original_word_size
        AppGlobals.number_base = original_number_base
        AppGlobals.bitwise_shift = original_bitwise_shift

        if assertion_error:
            raise assertion_error