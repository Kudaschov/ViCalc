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
        # =====================================================================
        # --- AND OPERATION ---
        # =====================================================================
        # Case 1: 8-Bit AND: 0xF0 AND 0xAA = 0xA0 (160)
        (
            [
                "F0",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.AND),
                "AA",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0xA0,
        ),
        # Case 2: 16-Bit AND: 0xABCD AND 0x0F0F = 0x0B0F (2831)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                "ABCD",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.AND),
                "0F0F",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0x0B0D,
        ),

        # =====================================================================
        # --- NAND OPERATION ---
        # =====================================================================
        # Case 3: 8-Bit NAND: 0xF0 NAND 0xAA = NOT(0xA0) & 0xFF = 0x5F (95)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_byte),
                "F0",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NAND),
                "AA",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0x5F,
        ),
        # Case 4: 16-Bit NAND: 0xFFFF NAND 0x1234 = NOT(0x1234) & 0xFFFF = 0xEDCB (60875)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                "FFFF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NAND),
                "1234",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0xEDCB,
        ),

        # =====================================================================
        # --- XOR OPERATION ---
        # =====================================================================
        # Case 5: 8-Bit XOR: 0xFF XOR 0x0F = 0xF0 (240)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_byte),
                "FF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.XOR),
                "0F",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0xF0,
        ),
        # Case 6: 32-Bit XOR: 0x12345678 XOR 0xFFFFFFFF = 0xEDCBA987 (3989547399)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                "12345678",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.XOR),
                "FFFFFFFF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0xEDCBA987,
        ),

        # =====================================================================
        # --- XNOR OPERATION ---
        # =====================================================================
        # Case 7: 8-Bit XNOR: 0xFF XNOR 0x0F = NOT(0xF0) & 0xFF = 0x0F (15)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_byte),
                "FF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.XNOR),
                "0F",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0x0F,
        ),
        # Case 8: 16-Bit XNOR: 0x1234 XNOR 0x1234 = NOT(0x0000) & 0xFFFF = 0xFFFF (65535)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                "1234",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.XNOR),
                "1234",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0xFFFF,
        ),

        # =====================================================================
        # --- OR OPERATION ---
        # =====================================================================
        # Case 9: 8-Bit OR: 0x0F OR 0xF0 = 0xFF (255)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_byte),
                "0F",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.OR),
                "F0",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0xFF,
        ),
        # Case 10: 64-Bit OR: 0x1000000000000000 OR 0x0000000000000001 = 0x1000000000000001
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                "1000000000000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.OR),
                "1",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0x1000000000000001,
        ),

        # =====================================================================
        # --- NOR OPERATION ---
        # =====================================================================
        # Case 11: 8-Bit NOR: 0x0F NOR 0xF0 = NOT(0xFF) & 0xFF = 0x00 (0)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_byte),
                "0F",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NOR),
                "F0",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0x00,
        ),
        # Case 12: 16-Bit NOR: 0x0000 NOR 0x0000 = NOT(0x0000) & 0xFFFF = 0xFFFF (65535)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                "0",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NOR),
                "0",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.calculate),
            ],
            0xFFFF,
        ),

        # =====================================================================
        # --- NOT (BITWISE UNARY NOT) OPERATION ---
        # =====================================================================
        # Case 13: 8-Bit NOT: NOT(0x0F) = 0xF0 (240)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_byte),
                "0F",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NOT),
            ],
            0xF0,
        ),
        # Case 14: 16-Bit NOT: NOT(0xAAAA) = 0x5555 (21845)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                "AAAA",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NOT),
            ],
            0x5555,
        ),
        # Case 15: 32-Bit NOT: NOT(0x00000000) = 0xFFFFFFFF (4294967295)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                "0",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NOT),
            ],
            0xFFFFFFFF,
        ),

        # =====================================================================
        # --- NEG (TWO'S COMPLEMENT NEGATION) OPERATION ---
        # =====================================================================
        # Case 16: 8-Bit NEG: NEG(0x01) = Two's complement = 0xFF (255)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_byte),
                "01",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NEG),
            ],
            0xFF,
        ),
        # Case 17: 8-Bit NEG: NEG(0x80) = Two's complement of -128 = 0x80 (128)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_byte),
                "80",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NEG),
            ],
            0x80,
        ),
        # Case 18: 16-Bit NEG: NEG(0x0005) = Two's complement = 0xFFFB (65531)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                "5",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NEG),
            ],
            0xFFFB,
        ),
        # Case 19: 64-Bit NEG: NEG(0x1) = 0xFFFFFFFFFFFFFFFF (18446744073709551615)
        (
            [
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                "1",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.NEG),
            ],
            0xFFFFFFFFFFFFFFFF,
        ),
    ],
)
def test_logic_operations(
    main_window, qtbot, key_sequence, expected_int
):
    """
    Test bitwise and logical operations (AND, NAND, XOR, XNOR, OR, NOR, NOT, NEG)
    across various word sizes in base-N hexadecimal mode.
    """
    input_box = AppGlobals.input_box
    input_imag_box = AppGlobals.input_imag_box

    # Backup original application globals
    original_calc_mode = AppGlobals.calc_mode
    original_word_size = AppGlobals.current_word_size
    original_number_base = AppGlobals.number_base

    # Set up initial test environment state
    AppGlobals.calc_mode = CalcMode.base_n
    AppGlobals.current_word_size = WordSize.BIT8
    AppGlobals.number_base = NumberBase.HEX

    input_box.button_clicked(CalcOperations.number_base_hexadecimal)
    main_window.update_keyboard()

    assertion_error = None

    try:
        qtbot.wait(50)
        input_box.clear()
        input_imag_box.clear()
        input_box.setFocus()
        qtbot.wait(50)

        # Process each key press or button click action sequentially
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

        # Parse output hex value to integer for evaluation
        int_val = int(input_box.text(), 16)

        try:
            assert int_val == expected_int
        except AssertionError as err:
            assertion_error = err

    finally:
        # Keep window open for manual inspection / Alt+F4 even if assertion failed
        # wait_for_manual_close(main_window)

        # Restore original global application state
        AppGlobals.calc_mode = original_calc_mode
        AppGlobals.current_word_size = original_word_size
        AppGlobals.number_base = original_number_base

        if assertion_error:
            raise assertion_error