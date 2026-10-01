import os
import pytest
import math
from PySide6.QtCore import Qt, QEventLoop
from vicalc.AppGlobals import AppGlobals
from vicalc.vicalc import MainWindow
from vicalc.CalcMode import CalcMode
from vicalc.DegUnit import DegUnit
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
    "key_sequence, expected_val",
    [
        (["20.25", lambda: AppGlobals.input_box.button_clicked(CalcOperations.sqrt)], 4.5),
        (["91.125", lambda: AppGlobals.input_box.button_clicked(CalcOperations.cube_root)], 4.5),
    ],
)

def test_sqrt(
    main_window, qtbot, key_sequence, expected_val
):
    """Test trigonometric and hyperbolic calculations."""
    input_box = AppGlobals.input_box
    input_imag_box = AppGlobals.input_imag_box

    original_calc_mode = AppGlobals.calc_mode
    AppGlobals.calc_mode = CalcMode.scientific
    original_compex_number_form = AppGlobals.complex_number_form
    AppGlobals.complex_number_form = ComplexNumberForm.rectangular
    original_replace_decimal_separator = AppGlobals.input_replace_decimal_separator
    AppGlobals.input_replace_decimal_separator = True
    original_angle_unit = AppGlobals.angle_unit
    AppGlobals.angle_unit = DegUnit()
    AppGlobals.input_imag_box.memory = 5.6

    assertion_error = None

    try:
        qtbot.wait(50)
        input_box.clear()
        input_imag_box.clear()
        input_box.setFocus()
        qtbot.wait(50)

        for item in key_sequence:
            focus_widget = main_window.focusWidget() or input_box
            
            # Executing callable/method directly (e.g., input_box.exec_sin)
            if callable(item):
                item()
            elif isinstance(item, Qt.Key):
                qtbot.keyClick(focus_widget, item)
            elif isinstance(item, str) and len(item) > 1:
                # Send strings longer than 1 character directly
                qtbot.keyClicks(focus_widget, item)
            else:
                qtbot.keyClick(focus_widget, item)
                
            qtbot.wait(20)

        qtbot.wait(50)

        # Convert text results to floats and assert with absolute tolerance (abs=1e-9)
        result = float(input_box.text())

        try:
            assert result == pytest.approx(expected_val, abs=1e-9)
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

        # Re-raise the assertion failure after restoring state
        if assertion_error:
            raise assertion_error
