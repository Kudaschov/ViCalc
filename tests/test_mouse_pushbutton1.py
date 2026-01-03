import pytest
from vicalc.vicalc import MainWindow
from vicalc.AppGlobals import AppGlobals
from PySide6.QtCore import QCoreApplication
import os
from PySide6.QtCore import Qt, QPoint
from PySide6.QtTest import QTest

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    return window

def test_pushbutton1_click(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.setText("6");
    qtbot.wait(50)

    button = main_window.ui.pushButton1
    # optional, aber hilfreich bei Timing-Problemen
    qtbot.waitExposed(button)

    pos = button.rect().topLeft() + QPoint(1, 1)

    # Maus über Position bewegen (Hover)
    qtbot.mouseMove(button, pos)
    qtbot.wait(50)

    pos = button.rect().topLeft() + QPoint(2, 2)
    qtbot.mouseMove(button, pos)

    # optional: Qt einen Moment Zeit für Hover-Events geben
    qtbot.wait(50)

    qtbot.mouseClick(
        button,
        Qt.LeftButton,
        pos=pos
    )

    # optional: Qt einen Moment Zeit für Hover-Events geben
    qtbot.wait(50)

    # Statt toPlainText() die Methode verwenden, die ViCalc für die Anzeige benutzt
    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "720"

    if os.getenv("VICALC_DEBUG"):
        qtbot.wait(10_000)    
