import pytest
from vicalc.vicalc import MainWindow
from vicalc.AppGlobals import AppGlobals
from PySide6.QtCore import QCoreApplication
import os
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    return window

def test_numpad_plus(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    # for char in "23":
    #     qtbot.keyClick(input_box, char)
    #     qtbot.wait(20)

    QTest.keyClick(input_box, Qt.Key_2, Qt.KeypadModifier)
    qtbot.wait(20)
    QTest.keyClick(input_box, Qt.Key_3, Qt.KeypadModifier)
    qtbot.wait(20)

    # Simuliere Numpad Plus
    QTest.keyClick(input_box, Qt.Key_Plus, Qt.KeypadModifier)

    for char in "45":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    # Hier: Simuliere Numpad Enter
    QTest.keyClick(input_box, Qt.Key_Enter)
    qtbot.wait(50)

    # Statt toPlainText() die Methode verwenden, die ViCalc für die Anzeige benutzt
    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "68"

    if os.getenv("VICALC_DEBUG"):
        qtbot.wait(10_000)    
