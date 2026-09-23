import os
import pytest
import math
from PySide6.QtCore import Qt, QEventLoop
from vicalc.AppGlobals import AppGlobals
from vicalc.vicalc import MainWindow
from vicalc.CalcMode import CalcMode
from vicalc.RadUnit import RadUnit
from vicalc.DegUnit import DegUnit
from vicalc.ComplexNumberForm import ComplexNumberForm

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
        # Complex addition: (6.5∠40) + (4.2∠75) = 7 - 4j
        (["6.5", Qt.Key_Tab, "4", "0", "+", "4",".","2", Qt.Key_Tab, "7","5", "="], 10.22818173568396, 53.62273617890308),
        # Subtraction
        (["_4.5", Qt.Key_Tab, "30", "-", "2.8", Qt.Key_Tab, "_60", "="], 5.3, 178.1092081981543),
        # Complex multiplication: (3.5∠25°) * (2.0∠40°) = 7.0∠65°
        (["3.5", Qt.Key_Tab, "25", "*", "2.0", Qt.Key_Tab, "40", "="], 7.0, 65.0),
        (["3.5", Qt.Key_Tab, "25", Qt.Key_Asterisk, "2.0", Qt.Key_Tab, "40", "="], 7.0, 65.0),
        (["_2.5", Qt.Key_Tab, "120", "*", "4.0", Qt.Key_Tab, "_30", "="], 10.0, -90.0),
        # Complex division: (12.0∠80°) / (3.0∠30°) = 4.0∠50°
        (["12.0", Qt.Key_Tab, "80", "/", "3.0", Qt.Key_Tab, "30", "="], 4.0, 50.0),
        (["12.0", Qt.Key_Tab, "80", Qt.Key_Slash, "3.0", Qt.Key_Tab, "30", "="], 4.0, 50.0),
        (["8.0", Qt.Key_Tab, "_45", "/", "2.0", Qt.Key_Tab, "60", "="], 4.0, -105.0),
        # Sqrt: sqrt(25.0∠60°) = 5.0∠30°
        (["25.0", Qt.Key_Tab, "60", lambda: AppGlobals.input_box.exec_sqrt()], 5.0, 30.0),
        (["16.0", Qt.Key_Tab, "_80", lambda: AppGlobals.input_box.exec_sqrt()], 4.0, -40.0),
        # Exp: e^(2.0 + j*(pi/3 rad = 60°)) = e^2∠60° ≈ 7.38905609893065∠60°
        (["2.0", Qt.Key_Tab, "60", lambda: AppGlobals.input_box.exec_ex()], 2.718281828459046, 99.23920117592257),
    ],
)

def test_complex_keyboard_input(
    main_window, qtbot, key_sequence, expected_real, expected_imag
):
    """Test complex number entry using Tab navigation and prefix key for negative numbers."""
    input_box = AppGlobals.input_box
    input_imag_box = AppGlobals.input_imag_box

    original_calc_mode = AppGlobals.calc_mode
    AppGlobals.calc_mode = CalcMode.complex_numbers
    original_compex_number_form = AppGlobals.complex_number_form
    AppGlobals.complex_number_form = ComplexNumberForm.polar
    original_replace_decimal_separator = AppGlobals.input_replace_decimal_separator
    AppGlobals.input_replace_decimal_separator = True
    original_angle_unit = AppGlobals.angle_unit
    AppGlobals.angle_unit = DegUnit()
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