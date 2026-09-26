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
        # --- BYTE (8-Bit + Carry Bit) ---
        # Case 1: ROL 0xA2 (0b10100010), Carry=0 -> 0b01000100 (0x44 = 68), New Carry=1
        # Explanation: MSB '1' shifts into Carry, initial Carry '0' shifts into LSB.
        (
            [
                "A2",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            68,
        ),
        # Case 2: ROR 0xA3 (0b10100011), Carry=0 -> 0b01010001 (0x51 = 81), New Carry=1
        # Explanation: LSB '1' shifts into Carry, initial Carry '0' shifts into MSB.
        (
            [
                "A3",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            81,
        ),
        # Case 3: ROR 0x51 (0b01010001), Carry=0 -> 0b00101000 (0x28 = 40), New Carry=1
        # Explanation: LSB '1' shifts into Carry, initial Carry '0' shifts into MSB.
        (
            [
                "51",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            40,
        ),
        # Case 4: ROL 0x81 (0b10000001), Carry=0 -> 0b00000010 (0x02 = 2), New Carry=1
        # Explanation: MSB '1' shifts into Carry, initial Carry '0' shifts into LSB.
        (
            [
                "81",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            2,
        ),

        # --- WORD (16-Bit + Carry Bit) ---
        # Case 5: ROL 0x8001, Carry=0 -> 0x0002 (2), New Carry=1
        # Explanation: Bit 15 ('1') shifts into Carry, initial Carry '0' shifts into Bit 0.
        (
            [
                "8001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            2,
        ),
        # Case 6: ROR 0x0001, Carry=0 -> 0x0000 (0), New Carry=1
        # Explanation: Bit 0 ('1') shifts into Carry, initial Carry '0' shifts into Bit 15.
        (
            [
                "1",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            0,
        ),

        # --- DWORD (32-Bit + Carry Bit) ---
        # Case 7: ROL 0x80000001, Carry=0 -> 0x00000002 (2), New Carry=1
        # Explanation: Bit 31 ('1') shifts into Carry, initial Carry '0' shifts into Bit 0.
        (
            [
                "80000001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            2,
        ),
        # Case 8: ROR 0x00000001, Carry=0 -> 0x00000000 (0), New Carry=1
        # Explanation: Bit 0 ('1') shifts into Carry, initial Carry '0' shifts into Bit 31.
        (
            [
                "1",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            0,
        ),

        # --- QWORD (64-Bit + Carry Bit) ---
        # Case 9: ROL 0x8000000000000001, Carry=0 -> 0x0000000000000002 (2), New Carry=1
        # Explanation: Bit 63 ('1') shifts into Carry, initial Carry '0' shifts into Bit 0.
        (
            [
                "8000000000000001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
            ],
            2,
        ),
        # Case 10: ROR 0x0000000000000001, Carry=0 -> 0x0000000000000000 (0), New Carry=1
        # Explanation: Bit 0 ('1') shifts into Carry, initial Carry '0' shifts into Bit 63.
        (
            [
                "1",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
            ],
            0,
        ),
    ],
)
def test_rotate_through_carry_bitwise_shift(
    main_window, qtbot, key_sequence, expected_int
):
    """Test bitwise rotation through carry (RoLC) operations across various word sizes."""
    input_box = AppGlobals.input_box
    input_imag_box = AppGlobals.input_imag_box

    original_calc_mode = AppGlobals.calc_mode
    AppGlobals.calc_mode = CalcMode.base_n
    original_word_size = AppGlobals.current_word_size
    AppGlobals.current_word_size = WordSize.BIT8
    original_number_base = AppGlobals.number_base
    AppGlobals.number_base = NumberBase.HEX
    original_bitwise_shift = AppGlobals.bitwise_shift
    AppGlobals.bitwise_shift = ShiftRotateOperation.circular_carry_bit
    AppGlobals.carry_flag = 0

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