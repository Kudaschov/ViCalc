import pytest
from vicalc.vicalc import MainWindow
from vicalc.AppGlobals import AppGlobals
from PySide6.QtCore import QCoreApplication
import os

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)
    return window

def test_addition(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    # Step-by-step Eingabe "12+34="
    for char in "12":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "+")
    qtbot.wait(20)

    for char in "34":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "=")
    qtbot.wait(50)

    # Statt toPlainText() die Methode verwenden, die ViCalc für die Anzeige benutzt
    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "46"

def test_subtraction(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    # Step-by-step Eingabe "12+34="
    for char in "56":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "-")
    qtbot.wait(20)

    for char in "78":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "=")
    qtbot.wait(50)

    # Statt toPlainText() die Methode verwenden, die ViCalc für die Anzeige benutzt
    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "-22"

def test_multiplication(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    # Step-by-step Eingabe "-1,23456789e-10*1e11"
    for char in "_1.23456789e_10":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "*")
    qtbot.wait(20)

    for char in "1e11":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "=")
    qtbot.wait(50)

    # Statt toPlainText() die Methode verwenden, die ViCalc für die Anzeige benutzt
    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "-12.3456789"

def test_division(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    AppGlobals.input_replace_decimal_separator = True

    for char in "12,34E1":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "/")
    qtbot.wait(20)

    for char in "_2":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "=")
    qtbot.wait(50)

    # Statt toPlainText() die Methode verwenden, die ViCalc für die Anzeige benutzt
    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "-61.7"

def test_factorial(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    for char in "6":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "!")
    qtbot.wait(50)

    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "720"

def test_brackets(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    for char in "2*(3+4)":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "=")
    qtbot.wait(50)

    # Statt toPlainText() die Methode verwenden, die ViCalc für die Anzeige benutzt
    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "14"

def test_pow(main_window, qtbot):
    input_box = AppGlobals.input_box

    qtbot.wait(50)
    input_box.clear()
    qtbot.wait(50)

    # Step-by-step Eingabe "-1,23456789e-10*1e11"
    for char in "2^3":
        qtbot.keyClick(input_box, char)
        qtbot.wait(20)

    qtbot.keyClick(input_box, "=")
    qtbot.wait(50)

    # Statt toPlainText() die Methode verwenden, die ViCalc für die Anzeige benutzt
    result = input_box.text()  # oder input_box.getText(), je nachdem was existiert
    assert result == "8"

    # print("ORG:", QCoreApplication.organizationName())
    # print("APP:", QCoreApplication.applicationName())

    if os.getenv("VICALC_DEBUG"):
        qtbot.wait(10_000)