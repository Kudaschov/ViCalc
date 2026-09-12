import pytest
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QLineEdit
from vicalc.AppGlobals import AppGlobals
from vicalc.vicalc import MainWindow
from vicalc.NumberBase import NumberBase


@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    return window

def fill_and_accept_dialog(qtbot, input_value: str):
    """Wait for the modal dialog to appear, fill in the input, and accept it."""
    # Dynamically wait until the dialog is rendered (prevents flaky tests)
    qtbot.waitUntil(lambda: QApplication.activeModalWidget() is not None, timeout=1000)
    top_widget = QApplication.activeModalWidget()
    assert top_widget is not None

    line_edit = top_widget.findChild(QLineEdit, "numberLineEdit")
    assert line_edit is not None, "QLineEdit 'numberLineEdit' not found in dialog."

    line_edit.clear()
    qtbot.keyClicks(line_edit, input_value)
    top_widget.accept()


@pytest.mark.parametrize(
    "exec_method_name, input_value, expected_result",
    [
        ("exec_from_binary", "10011", "10011"),
        ("exec_from_octal", "24", "10100"),
        ("exec_from_decimal", "21", "10101"),
        ("exec_from_hexadecimal", "16", "10110")
    ],
)

def test_binary_conversion(main_window, qtbot, exec_method_name, input_value, expected_result):
    input_box = AppGlobals.input_box
    AppGlobals.number_base = NumberBase.BIN
    input_box.clear()

    # Schedule the handler to execute as soon as the modal dialog opens its event loop
    QTimer.singleShot(0, lambda: fill_and_accept_dialog(qtbot, input_value))

    # Trigger the modal dialog method (e.g., exec_from_binary, exec_from_octal)
    exec_method = getattr(input_box, exec_method_name)
    exec_method()

    assert input_box.text() == expected_result