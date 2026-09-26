import os
import pytest
import math
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
        # Case 1: AshL 0b 1010 0010 << 1 = 0b 0100 0100
        (["A2", lambda:AppGlobals.input_box.button_clicked(CalcOperations.left_shift), "1="], 68),
        # Case 2: AshR 0b 1010 0010 >> 2 = 0b 1110 1000, on the left added 11
        (["A2", lambda:AppGlobals.input_box.button_clicked(CalcOperations.right_shift), "2="], 232),
        # Case 3: AshR 0b 0101 0001 >> 2 = 0b 0001 0100, on the left added 00
        (["51", lambda:AppGlobals.input_box.button_clicked(CalcOperations.right_shift), "2="], 20),
        # Case 4: AshL 0b 1010 0011 << 1 = 0b 0100 0110, on the right added 0
        (["A3", lambda:AppGlobals.input_box.button_clicked(CalcOperations.left_shift), "1="], 70),
        # Case 5: AshL 0b 1010 0010 << 1 = 0b 1 0100 0100
        (["A2", lambda:AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
          lambda:AppGlobals.input_box.button_clicked(CalcOperations.left_shift), "1="], 324),
        # Case 6: AshR 0x8000 >> 2 = 0xE000 (57344) - MSB (Bit 15) ist 1, Sign Extension auf 16 Bit mit 11
        (
            [
                "8000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            57344,
        ),
        # Case 7: AshR 0x7000 >> 2 = 0x1C00 (7168) - MSB (Bit 15) ist 0, Auffüllen mit 00 auf 16 Bit
        (
            [
                "7000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            7168,
        ),
        # Case 8: AshL 0x00FF << 4 = 0x0FF0 (4080) - Verschiebung über die Byte-Grenze hinweg
        (
            [
                "FF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "4=",
            ],
            4080,
        ),
        # Case 9: AshL 0x8001 << 1 = 0x0002 (2) - Überlauf / Maskierung bei 16 Bit (Bit 15 wird herausgeschoben)
        (
            [
                "8001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_word),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "1=",
            ],
            2,
        ),
# --- DWORD-Breite (32-Bit) ---
        # Case 10: AshL 0x0000FFFF << 4 = 0x000FFFF0 (1048560) - Verschiebung über Word-Grenze (Bit 16) hinweg
        (
            [
                "FFFF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "4=",
            ],
            1048560,
        ),
        # Case 11: AshR 0x80000000 >> 2 = 0xE0000000 (3758096384) - MSB (Bit 31) ist 1, Sign Extension auf 32 Bit
        (
            [
                "80000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            3758096384,
        ),
        # Case 12: AshR 0x70000000 >> 2 = 0x1C000000 (469762048) - MSB (Bit 31) ist 0
        (
            [
                "70000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            469762048,
        ),
        # Case 13: AshL 0x80000001 << 1 = 0x00000002 (2) - Überlauf / Maskierung auf 32 Bit (Bit 31 wird herausgeschoben)
        (
            [
                "80000001",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_dword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "1=",
            ],
            2,
        ),
# --- QWORD-Breite (64-Bit) ---
        # Case 14: AshL 0x00000000FFFFFFFF << 4 = 0x0000000FFFFFFFF0 (68719476720) - Verschiebung über DWORD-Grenze (Bit 32)
        (
            [
                "FFFFFFFF",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.left_shift),
                "4=",
            ],
            68719476720,
        ),
        # Case 15: AshR 0x8000000000000000 >> 2 = 0xE000000000000000 (16140901064495857664) - MSB (Bit 63) ist 1
        (
            [
                "8000000000000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            16140901064495857664,
        ),
        # Case 16: AshR 0x7000000000000000 >> 2 = 0x1C00000000000000 (2017612633061982208) - MSB (Bit 63) ist 0
        (
            [
                "7000000000000000",
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.word_size_qword),
                lambda: AppGlobals.input_box.button_clicked(CalcOperations.right_shift),
                "2=",
            ],
            2017612633061982208,
        ),
        # Case 17: AshL 0x8000000000000001 << 1 = 0x0000000000000002 (2) - Maskierung auf 64 Bit (Bit 63 wird herausgeschoben)
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

def test_function(
    main_window, qtbot, key_sequence, expected_int,
):
    """Test complex number entry using Tab navigation and prefix key for negative numbers."""
    input_box = AppGlobals.input_box
    input_imag_box = AppGlobals.input_imag_box

    original_calc_mode = AppGlobals.calc_mode
    AppGlobals.calc_mode = CalcMode.base_n
    original_word_size = AppGlobals.current_word_size
    AppGlobals.current_word_size = WordSize.BIT8
    original_number_base = AppGlobals.number_base
    AppGlobals.number_base = NumberBase.HEX
    original_bitwise_shift = AppGlobals.bitwise_shift
    AppGlobals.bitwise_shift = ShiftRotateOperation.arithmetic
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
            
            # Executing callable/method directly (e.g., input_box.exec_sqrt)
            if callable(item):
                item()
            elif isinstance(item, Qt.Key):
                qtbot.keyClick(focus_widget, item)
            elif isinstance(item, str) and len(item) > 1:
                    # Sendet lange Strings wie "3.141592653589793" am Stück
                    qtbot.keyClicks(focus_widget, item)
            else:
                qtbot.keyClick(focus_widget, item)
                
            qtbot.wait(20)

        qtbot.wait(50)

        # Convert text results to floats and assert with absolute tolerance (abs=1e-9)
        int_val = int(input_box.text(), 16)

        try:
            assert int_val == expected_int
        except AssertionError as err:
            assertion_error = err

    finally:
        # Keep window open for manual inspection / Alt+F4 even if assertion failed
        # wait_for_manual_close(main_window)
        
        # Restore original state
        AppGlobals.calc_mode = original_calc_mode
        AppGlobals.current_word_size = original_word_size
        AppGlobals.bitwise_shift = original_bitwise_shift

        # Re-raise the assertion failure after closing so pytest still reports the test as failed
        if assertion_error:
            raise assertion_error