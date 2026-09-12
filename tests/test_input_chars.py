import os
import pytest
from PySide6.QtCore import QCoreApplication
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

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("12+34=", "46"),
        ("56-78=", "-22"),
        ("_1.23456789e_10*1e11=", "-12.3456789"),
        ("12,34E1/_2=", "-61.7"),
        ("6!", "720"),
        ("2*(3+4)=", "14"),
        ("2^3=", "8"),
    ],
)

def test_calculator_expressions(main_window, qtbot, expression, expected):
    input_box = AppGlobals.input_box
    AppGlobals.number_base = NumberBase.DEC

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    for char in expression:
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.wait(50)
    assert input_box.text() == expected

    if os.getenv("VICALC_DEBUG"):
        qtbot.wait(10_000)