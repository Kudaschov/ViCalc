import os
import pytest
import math
from PySide6.QtCore import Qt, QEventLoop
from vicalc.AppGlobals import AppGlobals
from vicalc.vicalc import MainWindow
from vicalc.CalcMode import CalcMode
from vicalc.RadUnit import RadUnit
from vicalc.ComplexNumberForm import ComplexNumberForm
from vicalc.CalcOperations import CalcOperations

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
    "key_sequence, expected_real, expected_imag",
    [
        # Complex addition: (5 + 3j) + (2 - 7j) = 7 - 4j
        (["5", Qt.Key.Key_Tab, "3", "+", "2", Qt.Key.Key_Tab, "_", "7", "="], 7, -4),
        (["1", "2", ",", "5", Qt.Key_Tab, "3", ".", "4", Qt.Key_Plus, "2", Qt.Key_Comma, "1", Qt.Key_Tab, "_", "7", Qt.Key_Period, "8", "="], 14.6, -4.4),        
        # Subtraction
        (["8", ".", "7", "5", Qt.Key_Tab, "_", "2", ".", "2", "5", "-", "3", ".", "5", Qt.Key_Tab, "4", ".", "1", "="], 5.25, -6.35),
        (["8", ".", "7", "5", Qt.Key_Tab, "_", "2", ".", "2", "5", Qt.Key_Minus, "3", ".", "5", Qt.Key_Tab, "4", ".", "1", "="], 5.25, -6.35),
        # Complex multiplication: (3 + 2j) * (1 - 4j) = 11 - 10j
        (["3", Qt.Key_Tab, "2", "*", "1", Qt.Key_Tab, "_", "4", "="], 11, -10),
        (["2", ".", "5", Qt.Key_Tab, "1", ".", "2", Qt.Key_Asterisk, "4", ".", "0", Qt.Key_Tab, "_", "0", ".", "5", "="], 10.6, 3.55),
        # Division
        (["6", ".", "0", Qt.Key_Tab, "8", ".", "0", "/", "1", ".", "0", Qt.Key_Tab, "2", ".", "0", "="], 4.4, -0.8),
        (["6", ".", "0", Qt.Key_Tab, "8", ".", "0", Qt.Key_Slash, "1", ".", "0", Qt.Key_Tab, "2", ".", "0", "="], 4.4, -0.8),
        # Sqrt
        (["_", "5", Qt.Key_Tab, "1", "2", lambda: AppGlobals.input_box.exec_sqrt()], 2, 3),
        # Exp
        (["0", Qt.Key_Tab, str(math.pi), lambda: AppGlobals.input_box.exec_ex()], -1, 0),
        # Ln
        (["_1", Qt.Key_Tab, "0", lambda: AppGlobals.input_box.exec_ln()], 0, math.pi),
        # 10^
        (["1", Qt.Key_Tab, "2", lambda: AppGlobals.input_box.exec_ten_power_x()], -1.070134835587698, -9.942575694137897),
        # log10
        (["1", Qt.Key_Tab, "2", lambda: AppGlobals.input_box.exec_log()], 0.3494850021680094, 0.480828578784234),
        # log base n
        (["1", Qt.Key_Tab, "2", lambda: AppGlobals.input_box.button_clicked(CalcOperations.log_base), "3", Qt.Key_Tab, "4", "="], 0.6729526521196119, 0.3001811612672904),
        # Test cases for complex power of a complex number: (inputs, expected_real, expected_imag)
        # Case 1: (2.5 + 1.2i) ^ (1.5 + 0.5i) = 1.4021 + 3.4155i
        (["2", ".", "5", Qt.Key_Tab, "1", ".", "2", lambda: AppGlobals.input_box.button_clicked(CalcOperations.pow), "1", ".", "5", Qt.Key_Tab, "0", ".", "5", "="], 1.402088823721664, 3.415456895019335),
        # Case 3: (3.2 - 4.1i) ^ (1.2 + 2.3i) = -52.8561 + 24.8147i
        (["3", ".", "2", Qt.Key_Tab, "_", "4", ".", "1", lambda: AppGlobals.input_box.button_clicked(CalcOperations.pow), "1", ".", "2", Qt.Key_Tab, "2", ".", "3", "="], -52.85608480999289, 24.81473881193748),
        # Brackets
        (["1", Qt.Key.Key_Tab, "2", "*", "(", "3", Qt.Key.Key_Tab, "4", "+", "5", Qt.Key.Key_Tab, "7", ")", ")"], -14, 27),
        # Cube root
        (["_11", Qt.Key_Tab, "2", lambda: AppGlobals.input_box.exec_cube_root()], 1.232050807568877, 1.866025403784439),
    ],
)

def test_complex_keyboard_input(
    main_window, qtbot, key_sequence, expected_real, expected_imag
):
    """Test complex number entry using Tab navigation and prefix key for negative numbers."""
    input_box = AppGlobals.input_box
    input_imag_box = AppGlobals.input_imag_box

    original_calc_mode = AppGlobals.calc_mode
    input_imag_box.show()
    input_box.button_clicked(CalcOperations.calc_mode_complex_numbers)
    original_compex_number_form = AppGlobals.complex_number_form
    AppGlobals.complex_number_form = ComplexNumberForm.rectangular
    original_replace_decimal_separator = AppGlobals.input_replace_decimal_separator
    AppGlobals.input_replace_decimal_separator = True
    original_angle_unit = AppGlobals.angle_unit
    AppGlobals.angle_unit = RadUnit()

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
        real_val = float(input_box.text())
        imag_val = float(input_imag_box.text())

        try:
            assert real_val == pytest.approx(expected_real, abs=1e-9)
            assert imag_val == pytest.approx(expected_imag, abs=1e-9)
        except AssertionError as err:
            assertion_error = err

    finally:
        # Keep window open for manual inspection / Alt+F4 even if assertion failed
        # wait_for_manual_close(main_window)
        
        # Restore original state
        AppGlobals.calc_mode = original_calc_mode
        AppGlobals.input_replace_decimal_separator = original_replace_decimal_separator
        AppGlobals.angle_unit = original_angle_unit
        AppGlobals.complex_number_form = original_compex_number_form

        # Re-raise the assertion failure after closing so pytest still reports the test as failed
        if assertion_error:
            raise assertion_error