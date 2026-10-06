from unittest import case
from PySide6.QtWidgets import QApplication, QLineEdit, QStyleOptionFrame
from PySide6.QtCore import QUrl, Qt, Signal, QDate, QTime
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QFont, QGuiApplication
from PySide6.QtGui import QKeyEvent, QFocusEvent, QKeySequence, QShortcut
from PySide6.QtCore import QLocale
from PySide6.QtCore import QTimer
from PySide6.QtCore import QEvent

from ..QuadraticEquationExpression import QuadraticEquationExpression
from ..QuadraticEquationDialog import QuadraticEquationDialog
from ..QuadraticEquationExpression import QuadraticEquationExpression
from ..CalcOperations import CalcOperations
import math, cmath
import locale
import ctypes
import random
import time
from ..AdditionExpression import AdditionExpression
from ..SubtractionExpression import SubtractionExpression
from ..MultiplicationExpression import MultiplicationExpression
from ..DivisionExpression import DivisionExpression
from ..BracketExpression import BracketExpression
from ..TrigMode import TrigMode
from ..AngleUnit import AngleUnit
from ..DegUnitProtocol import DegUnitProtocol
from ..RadUnitProtocol import RadUnitProtocol
from ..GraUnitProtocol import GraUnitProtocol
from ..SinExpression import SinExpression
from ..ArcSinExpression import ArcSinExpression
from ..CosExpression import CosExpression
from ..ArcCosExpression import ArcCosExpression
from ..TanExpression import TanExpression
from ..ArcTanExpression import ArcTanExpression
from ..LnExpression import LnExpression
from ..EPowerXExpression import EPowerXExpression
from ..LogExpression import LogExpression
from ..TenPowerXExpression import TenPowerXExpression
from ..MSExpression import MSExpression
from ..MPlusExpression import MPlusExpression
from ..MMinusExpression import MMinusExpression
from ..ReciprocalExpression import ReciprocalExpression
from ..AbsExpression import AbsExpression
from ..CommentDialog import CommentDialog
from ..ConvertFromBaseDialog import ConvertFromBaseDialog
from ..FactorialExpression import FactorialExpression
from ..PowExpression import PowExpression
from ..SquareExpression import SquareExpression
from ..CubeExpression import CubeExpression
from ..SqrtExpression import SqrtExpression
from ..CubeRootExpression import CubeRootExpression
from ..MMultiplyExpression import MMultiplyExpression
from ..MDisivionExpression import MDisivionExpression
from ..PercentExpression import PercentExpression
from ..PercentChangeExpression import PercentChangeExpression
from ..ConvertToBasesExpression import ConvertToBasesExpression
from ..BaseExpression import BaseExpression
from ..AppGlobals import AppGlobals
from ..UiGlobals import UiGlobals
from ..DMSExpression import DMSExpression
from ..DMStoDD_Dialog import DMStoDD_Dialog
from ..DDExpression import DDExpression
from ..ResultCellValue import ResultCellValue
from ..SinhExpression import SinhExpression
from ..CoshExpression import CoshExpression
from ..TanhExpression import TanhExpression
from ..ArsinhExpression import ArsinhExpression
from ..ArcoshExpression import ArcoshExpression
from ..ArtanhExpression import ArtanhExpression
from ..RectangularToPolarDialog import RectangularToPolarDialog
from ..RectangularToPolarExpression import RectangularToPolarExpression
from ..PolarToRectangularDialog import PolarToRectangularDialog
from ..PolarToRectangularExpression import PolarToRectangularExpression
from ..CombinationDialog import CombinationDialog
from ..CombinationExpression import CombinationExpression
from ..PermutationExpression import PermutationExpression
from ..FourthRootExpression import FourthRootExpression
from ..FourthPowerExpression import FourthPowerExpression
from ..NumFormatDialog import NumFormatDialog
from ..NumericFormat import NumericFormat
from ..CellValue import CellValue
from ..CommentCellValue import CommentCellValue
from ..StringCellValue import StringCellValue
from ..FloatCellValue import FloatCellValue
from ..ResultCellValue import ResultCellValue
from ..PhyConstDialog import PhyConstDialog
from ..unit_conversion import ConversionDialog
from ..RatioCDialog import RatioCDialog
from ..RatioDDialog import RatioDDialog
from ..RatioCExpression import RatioCExpression
from ..RatioDExpression import RatioDExpression
from ..LinearTwoPointsDialog import LinearTwoPointsDialog
from ..LinearTwoPointsExpression import LinearTwoPointsExpression
from ..LinearYfromXDialog import LinearYfromXDialog
from ..LinearYfromXExpression import LinearYfromXExpression
from ..LinearSystemDialog import LinearSystemDialog
from ..LinearSystemExpression import LinearSystemExpression
import re
from ..LogBaseExpression import LogBaseExpression
from ..AwgToMm2Dialog import AwgToMm2Dialog
from ..AwgToMm2Expression import AwgToMm2Expression
from ..Mm2ToAwgDialog import Mm2ToAwgDialog
from ..Mm2ToAwgExpression import Mm2ToAwgExpression
from ..FracPartExpression import FracPartExpression
from ..IntPartExpression import IntPartExpression
from ..ModExpression import ModExpression
from ..ANDExpression import ANDExpression
from ..NANDExpression import NANDExpression
from ..ORExpression import ORExpression
from ..NORExpression import NORExpression
from ..XORExpression import XORExpression
from ..XNORExpression import XNORExpression
from ..NOTExpression import NOTExpression
from ..NEGExpression import NEGExpression
from ..WordSize import WordSize
from ..NumberBase import NumberBase
from ..IntegerResultCellValue import IntegerResultCellValue
from ..CalcMode import CalcMode
from ..ResultStringCellValue import ResultStringCellValue
from ..ComplexNumberForm import ComplexNumberForm
from ..InputRectangularForm import InputRectangularForm
from ..InputPolarForm import InputPolarForm
from ..ComplexRectPolarHistoryExpression import ComplexRectPolarHistoryExpression
from ..UnaryExpression import UnaryExpression
from ..ConjugateExpression import ConjugateExpression
from ..ShiftRotateOperation import ShiftRotateOperation
from ..LeftShiftCircularExpression import LeftShiftCircularExpression
from ..RightShiftCircularExpression import RightShiftCircularExpression
from ..LeftShiftArithmeticExpression import LeftShiftArithmeticExpression
from ..RightShiftArithmeticExpression import RightShiftArithmeticExpression
from ..LeftShiftLogicalExpression import LeftShiftLogicalExpression
from ..RightShiftLogicalExpression import RightShiftLogicalExpression
from ..LeftShiftRotateCarryExpression import LeftShiftRotateCarryExpression
from ..RightShiftRotateCarryExpression import RightShiftRotateCarryExpression

class InputTextEdit(QLineEdit):
    # Define a custom signal that carries a boolean indicating if Shift is pressed
    shiftStatusChanged = Signal(bool)
    ctrlStatusChanged = Signal(bool)
    shiftHold = Signal()
    physicalShiftStatusChanged = Signal(bool)
    memory_changed = Signal(str)
    focusOut = Signal()
    focusIn = Signal()
    statusbar_changed = Signal()
    statusbar_message = Signal(str)
    trig_mode_changed = Signal()
    keyboard_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.number: float = None  # Holds the parsed number
        self._memory: float = 0
        AppGlobals.angle_unit = DegUnitProtocol()
        self.key = None
        self.modifiers = None
        self.scan_code = None
        self.char_pressed = None
        self.resultFont = QFont()
        self.resultFont.setBold(True)
        self._last_shift_state = False # Keep track of the last shift state
        self._last_ctrl_state = False # Keep track of the last ctrl state
        self._last_physical_shift_state = False # Keep track of the last physical shift state
        self.current_shift_state = False
        self.current_ctrl_state = False
        self.current_physical_shift_state = False
        # Define a list to store CalcButton objects
        self.button_list = []
        self.locale = AppGlobals.locale

        # Set default base mode
        self.set_base(AppGlobals.number_base)        

        # Threshold time in seconds between two key presses
        self.double_press_interval = 0.35

        # Timestamps for tracking consecutive key presses
        self.last_shift_time = 0.0
        self.last_ctrl_time = 0.0
        self.last_ctrl_shift_time = 0.0

        # State tracking flag for Ctrl+Shift combination
        self.was_ctrl_shift_active = False        

    def keyPressEvent(self, event):
        self.key = event.key()
        self.modifiers = event.modifiers()
        self.scan_code = event.nativeScanCode()
        # 📚 Character (text)
        # The 'text()' method returns the Unicode text of the key.
        # This is the actual character generated by the key press, considering modifiers.
        self.char_pressed = event.text()

        # 🏷️ Name (text representation of the key)
        # For non-character keys (like F1, Enter, Shift), 'text()' might be empty.
        # 'key()' returns a Qt.Key constant, which can be converted to a string.
        key_name = Qt.Key(event.key()).name

        # ⌨️ Scan Code
        # 'nativeScanCode()' returns the hardware-dependent scan code.
        # This is specific to the keyboard hardware and operating system.

        output = f"Char Pressed: '{self.char_pressed}' | Qt.Key: " \
                 f"{key_name} | " \
                 f"Virtual Key Code (int): {self.key} | " \
                 f"Scan Code (Native): {self.scan_code}"
        
        print(output)

        # Check current Shift state
        self.current_shift_state = bool(self.modifiers & Qt.ShiftModifier)
        self.current_ctrl_state = bool(self.modifiers & Qt.ControlModifier)
        self.current_physical_shift_state = self.get_physical_shift_state()
        # Emit signal only if the shift state has actually changed
        if self.current_shift_state != self._last_shift_state:
            self.shiftStatusChanged.emit(self.current_shift_state)
            self._last_shift_state = self.current_shift_state
            print(f"Shift status changed to: {'Pressed' if self.current_shift_state else 'Released'}")        

        # Emit signal only if the shift state has actually changed
        if self.current_ctrl_state != self._last_ctrl_state:
            self.ctrlStatusChanged.emit(self.current_ctrl_state)
            self._last_ctrl_state = self.current_ctrl_state
            print(f"Ctrl status changed to: {'Pressed' if self.current_ctrl_state else 'Released'}")        

        # Emit signal only if the physical shift state has actually changed
        if self.current_physical_shift_state != self._last_physical_shift_state:
            self.physicalShiftStatusChanged.emit(self.current_physical_shift_state)
            self._last_physical_shift_state = self.current_physical_shift_state
            print(f"Physical Shift status changed to: {'Pressed' if self.current_physical_shift_state else 'Released'}")

        if self.current_shift_state or self.current_ctrl_state or self.current_physical_shift_state:
            self.reset_hold_flags()

        current_time = time.time()
        key = event.key()
        modifiers = event.modifiers()

        is_ctrl = bool(modifiers & Qt.KeyboardModifier.ControlModifier)
        is_shift = bool(modifiers & Qt.KeyboardModifier.ShiftModifier)
        is_both = is_ctrl and is_shift

        # Track if both Ctrl and Shift are pressed simultaneously
        if is_both:
            if not self.was_ctrl_shift_active:
                time_diff = current_time - self.last_ctrl_shift_time

                if time_diff <= self.double_press_interval:
                    self.on_double_ctrl_shift()
                    self.last_ctrl_shift_time = 0.0
                else:
                    self.last_ctrl_shift_time = current_time

                self.was_ctrl_shift_active = True

            # Suppress single Ctrl/Shift logic while doing the combination
            self.last_shift_time = 0.0
            self.last_ctrl_time = 0.0

        # --- Single Shift Handling ---
        if key == Qt.Key.Key_Shift:
            time_diff = current_time - self.last_shift_time

            if is_ctrl:
                # Ctrl held down while double-pressing Shift
                if time_diff <= self.double_press_interval:
                    self.exec_ctrl_double_shift()
                    self.last_shift_time = 0.0
                else:
                    self.last_shift_time = current_time
            else:
                # Standalone Double-Shift
                if time_diff <= self.double_press_interval:
                    self.exec_double_shift()
                    self.last_shift_time = 0.0
                else:
                    self.last_shift_time = current_time

            self.last_ctrl_time = 0.0

        # --- Single Ctrl Handling ---
        elif key == Qt.Key.Key_Control:
            time_diff = current_time - self.last_ctrl_time

            if time_diff <= self.double_press_interval:
                self.exec_double_ctrl()
                self.last_ctrl_time = 0.0
            else:
                self.last_ctrl_time = current_time

            self.last_shift_time = 0.0

        else:
            # Reset all timers on regular key press
            self.last_shift_time = 0.0
            self.last_ctrl_time = 0.0
            self.last_ctrl_shift_time = 0.0

        self.handle_keys_check_errors(event)

    # You also need to override keyReleaseEvent to detect when Shift is released
    def keyReleaseEvent(self, event):
        self.modifiers = event.modifiers()
        self.current_shift_state = bool(self.modifiers & Qt.ShiftModifier)
        self.current_ctrl_state = bool(self.modifiers & Qt.ControlModifier)
        self.current_physical_shift_state = bool(self.modifiers & Qt.ShiftModifier)  # Assuming physical shift is the same as logical shift
        
        if self.current_shift_state != self._last_shift_state:
            self.shiftStatusChanged.emit(self.current_shift_state)
            self._last_shift_state = self.current_shift_state
            print(f"Shift status changed to: {'Pressed' if self.current_shift_state else 'Released'}")

        if self.current_ctrl_state != self._last_ctrl_state:
            self.ctrlStatusChanged.emit(self.current_ctrl_state)
            self._last_ctrl_state = self.current_ctrl_state
            print(f"Ctrl status changed to: {'Pressed' if self.current_ctrl_state else 'Released'}")

        if self.current_physical_shift_state != self._last_physical_shift_state:
            self.physicalShiftStatusChanged.emit(self.current_physical_shift_state)
            self._last_physical_shift_state = self.current_physical_shift_state
            print(f"Physical Shift status changed to: {'Pressed' if self.current_physical_shift_state else 'Released'}")

        is_ctrl = bool(self.modifiers & Qt.KeyboardModifier.ControlModifier)
        is_shift = bool(self.modifiers & Qt.KeyboardModifier.ShiftModifier)

        # Reset active combo flag when either key is released
        if not (is_ctrl and is_shift):
            self.was_ctrl_shift_active = False            

        super().keyReleaseEvent(event)                

    def store_number(self):
        result = False
        ok = False

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            AppGlobals.input_box.number, ok = AppGlobals.input_box.locale.toDouble(AppGlobals.input_box.text())
            if ok:
                AppGlobals.input_imag_box.number, ok = AppGlobals.input_imag_box.toDouble(AppGlobals.input_imag_box.text())

            # ToDo VK
            AppGlobals.input_box.selectAll()
            result = ok
        else:
            try:
                if AppGlobals.calc_mode == CalcMode.base_n:
                    if AppGlobals.number_base == NumberBase.DEC:
                        self.number, ok = self.locale.toDouble(self.text())
                    elif AppGlobals.number_base == NumberBase.BIN:
                        self.number = int(self.text(), 2)
                        ok = True
                    elif AppGlobals.number_base == NumberBase.OCT:
                        self.number = int(self.text(), 8)
                        ok = True
                    elif AppGlobals.number_base == NumberBase.HEX:
                        self.number = int(self.text(), 16)
                        ok = True
                else:
                    self.number, ok = self.locale.toDouble(self.text())
                if ok:
                    self.selectAll()
                    result = True
                else:
                    raise ValueError(
                        f"Could not convert '{self.text()}' to float using the current locale "
                        f"('{self.locale.name()}'). Please ensure the format matches the locale's "
                        f"decimal separator (e.g., '.' or ',') and thousands separator."
                    )
            except ValueError:
                self._show_error("Invalid input. Please enter a valid number.")
            except Exception as e:
                self._show_error(f"Unexpected error: {str(e)}")
        return result

    def store_integer_number(self):
        result = False
        try:
            ok = False
            if AppGlobals.calc_mode == CalcMode.base_n:
                if AppGlobals.number_base == NumberBase.DEC:
                    self.number, ok = self.locale.toDouble(self.text())
                elif AppGlobals.number_base == NumberBase.BIN:
                    self.number = int(self.text(), 2)
                    ok = True
                elif AppGlobals.number_base == NumberBase.OCT:
                    self.number = int(self.text(), 8)
                    ok = True
                elif AppGlobals.number_base == NumberBase.HEX:
                    self.number = int(self.text(), 16)
                    ok = True
            else:
                self.number, ok = self.locale.toDouble(self.text())

            ok = ok and self.number.is_integer()  # Ensure the number is an integer

            if ok:
                self.selectAll()
                result = True
            else:
                raise ValueError(
                    f"Could not convert '{self.text()}' to an integer. Please ensure the input is a valid integer."
                )

        except ValueError:
            self._show_error("Invalid input. Please enter a valid integer.")
        except Exception as e:
            self._show_error(f"Unexpected error: {str(e)}")

        return result

    def _show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def toString(self, number):
        return AppGlobals.to_normal_string(number)
    
    def memory_to_string(self):
        return self.toString(self.memory)

    def memory_to_format_string(self):
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            z = complex(AppGlobals.input_box.memory, AppGlobals.input_imag_box.memory)
            return AppGlobals.to_format_string(z)
        else:
            return AppGlobals.to_format_string(self.memory)

    def toDouble(self, text):
        return self.locale.toDouble(text)
    
    def exec_factorial(self):
        try:
            i = int(self.text())
            f = FactorialExpression().calculate(float(i))
            self.setText(str(f))
            self.selectAll()
        except ValueError:
            self._show_error("Invalid input: nonnegative integer expected.")

    def normal_unary_operation(self, event):
        if self.key == Qt.Key.Key_Escape:
            self.exec_ac()
            return True
            # Special case, because Shift is suppressed: Shift + Period on numeric pad
        return False
    
    def shift_unary_operation(self, event):
        if self.key == Qt.Key.Key_Minus:
            super().keyPressEvent(event)
            return True
        return False
    
    def exec_c(self):
        self.selectAll()

    def exec_ac(self):
        if self == AppGlobals.input_imag_box:
            AppGlobals.input_box.exec_ac()
            return
        
        AppGlobals.root_expression = None
        self.update_expression_label()
        self.selectAll()
        self.reset_hold_flags()

    def create_expression_node(self, expression):
        if AppGlobals.root_expression == None:
            AppGlobals.root_expression = expression
            self.update_expression_label()
        else:
            last_expression_temp = self.last_expression()
            if (expression.operation_prio > last_expression_temp.operation_prio or
                isinstance(expression, BracketExpression)):
                last_expression_temp.next_expression = expression
                expression.prev_expression = last_expression_temp
                self.update_expression_label()
            else:
                if isinstance(last_expression_temp, BracketExpression):
                    # bracket before, add a node
                    expression.prev_expression = last_expression_temp
                    last_expression_temp.next_expression = expression
                    self.update_expression_label()
                else:
                    # prio of expression is lower or equal of last expression
                    if (last_expression_temp.prev_expression
                            and last_expression_temp.prev_expression.operation_prio >= expression.operation_prio):
                            #last_expression_temp.prev_expression is greater or equal to expression
                            #chain calculation
                            self.create_expression_node_chain(AppGlobals.get_number(), expression)
                    else:
                        # calculate last expression and change this last expression with expression
                        expression.first_number = last_expression_temp.calculate(AppGlobals.get_number())
                        expression.prev_expression = last_expression_temp.prev_expression
                        expression.next_expression = last_expression_temp.next_expression

                        if last_expression_temp == AppGlobals.root_expression:
                            AppGlobals.root_expression = expression
                        else:
                            last_expression_temp.prev_expression.next_expression = expression
                        self.update_expression_label()

    def create_expression_node_chain(self, number: float, expression):
        last_expression_temp = self.last_expression()
        if isinstance(last_expression_temp.prev_expression, BracketExpression):
            # expression 1 / (2 * 3 + 4) = 0.1
            expression.first_number = last_expression_temp.calculate(number)
            last_expression_temp.prev_expression.next_expression = None
            self.create_expression_node(expression)
            self.update_expression_label()
        else:
            # expression 25 - 5 * 15 + 116 = 66
            # expression 1 + 2 * 3 ^ 4 + 5 = 168
            # expression 1 + 2 * 3 ^ 4 * 5 = 811
            expression.first_number = last_expression_temp.calculate(number)

            if last_expression_temp.prev_expression:
                last_expression_temp.prev_expression.next_expression = None
                if expression.operation_prio <= last_expression_temp.prev_expression.operation_prio:
                    self.create_expression_node_chain(expression.first_number, expression)
                else:
                    self.create_expression_node(expression)
            else:
                AppGlobals.root_expression = None
                self.create_expression_node(expression)

    def update_expression_label(self):
        s = ""
        currect_expression = AppGlobals.root_expression
        while currect_expression != None:
            s += currect_expression.text()
            currect_expression = currect_expression.next_expression
        AppGlobals.expressionLabel.setText(s)
        self.selectAll()

    def setTextSelect(self, text):
        self.setText(text)
        self.selectAll()

    def exec_addition(self):
        if self.store_number():
            self.create_expression_node(AdditionExpression(AppGlobals.get_number()))

    def exec_pow(self):
        if self.store_number():
            self.create_expression_node(PowExpression(AppGlobals.get_number()))

    def exec_opening_bracket(self):
        self.create_expression_node(BracketExpression())

    def exec_subtraction(self):
        if self.store_number():
            self.create_expression_node(SubtractionExpression(AppGlobals.get_number()))

    def exec_multiplication(self):
        if self.store_number():
            self.create_expression_node(MultiplicationExpression(AppGlobals.get_number()))

    def exec_AND(self):
        if self.store_integer_number():
            self.create_expression_node(ANDExpression(self.number))

    def exec_NAND(self):            
        if self.store_integer_number():
            self.create_expression_node(NANDExpression(self.number))

    def exec_OR(self):
        if self.store_integer_number():
            self.create_expression_node(ORExpression(self.number))

    def exec_NOR(self):
        if self.store_integer_number():
            self.create_expression_node(NORExpression(self.number))

    def exec_XOR(self):
        if self.store_integer_number():
            self.create_expression_node(XORExpression(self.number))

    def exec_XNOR(self):
        if self.store_integer_number():
            self.create_expression_node(XNORExpression(self.number))

    def exec_NOT(self):
        if self.store_integer_number():
            expr = NOTExpression()
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_NEG(self):
        if self.store_integer_number():
            expr = NEGExpression()
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_division(self):
        if self.store_number():
            self.create_expression_node(DivisionExpression(AppGlobals.get_number()))

    def exec_mod(self):
        if self.store_number():
            self.create_expression_node(ModExpression(self.number))

    def execute(self):
        store_number = AppGlobals.input_box.store_number()

        if (AppGlobals.root_expression == None):
            if store_number:
                ue = UnaryExpression()
                ue.calculate(AppGlobals.get_number())
        elif store_number:
            # go to last expression

            current_expression = self.last_expression()

            last_number = AppGlobals.get_number()

            while current_expression != None:
                last_number = current_expression.calculate(last_number)
                current_expression = current_expression.prev_expression

            if (AppGlobals.root_expression != None):
                AppGlobals.number_to_input_box(last_number)
                AppGlobals.root_expression = None
                self.update_expression_label()

    def exec_percent(self):
        if self.store_number():
            if self.last_expression() != None:
                if isinstance(self.last_expression(), PercentChangeExpression):
                    # it is already a percent change expression, calculate it
                    self.execute()
                else:
                    percent = PercentExpression(self.last_expression())
                    result = percent.calculate(self.number)
                    if result is not None:
                        self.setTextSelect(self.toString(result))
                    # remove the node, because it is processed
                    if (self.last_expression().prev_expression != None):
                        self.last_expression().prev_expression.next_expression = None
                    else:
                        AppGlobals.root_expression = None
                    self.update_expression_label()
            else:
                if self.store_number():
                    self.create_expression_node(PercentChangeExpression(self.number))

    def exec_closing_bracket(self):
        if self.store_number():
            current_expression = self.last_expression()

            last_number = AppGlobals.get_number()

            while current_expression != None:
                if isinstance(current_expression, BracketExpression):
                    break
                last_number = current_expression.calculate(last_number)
                current_expression = current_expression.prev_expression

            # bracket expression is no longer required, exclude it from chain
            if current_expression == None:
                AppGlobals.root_expression = None
            else:
                current_expression = current_expression.prev_expression
                if current_expression == None:
                    AppGlobals.root_expression = None
                else:
                    current_expression.next_expression = None

            AppGlobals.number_to_input_box(last_number)
            self.update_expression_label()

    def exec_pi(self):
        self.setText(self.toString(math.pi))
        self.selectAll()

    def last_expression(self):
        current_expression = None
        if AppGlobals.root_expression != None:
            current_expression = AppGlobals.root_expression
            while current_expression.next_expression != None:
                current_expression = current_expression.next_expression
        return current_expression

    def button_clicked(self, calc_operation):
        # Set of operations that do not change focus
        EXCLUDED_OPERATIONS = {
            CalcOperations.C,
            CalcOperations.comma,
            CalcOperations.sign_change,
            CalcOperations.insert_minus,
            CalcOperations.backspace,
            CalcOperations.number_0,
            CalcOperations.number_1,
            CalcOperations.number_2,
            CalcOperations.number_3,
            CalcOperations.number_4,
            CalcOperations.number_5,
            CalcOperations.number_6,
            CalcOperations.number_7,
            CalcOperations.number_8,
            CalcOperations.number_9,
            CalcOperations.number_A,
            CalcOperations.number_B,
            CalcOperations.number_C,
            CalcOperations.number_D,
            CalcOperations.number_E,
            CalcOperations.number_F,
            CalcOperations.exponent,
            CalcOperations.shift_hold,
            CalcOperations.ctrl_hold,
            CalcOperations.ctrl_shift_hold,
            CalcOperations.int_part,
            CalcOperations.frac_part,
            CalcOperations.random,
            CalcOperations.round,
            CalcOperations.convert_to_deg,
            CalcOperations.convert_to_rad,
            CalcOperations.convert_to_gra,
            CalcOperations.trig_mode_deg,
            CalcOperations.trig_mode_rad,
            CalcOperations.trig_mode_gra,
            CalcOperations.pi,
            CalcOperations.copy_to_clipboard
        }
        try:
            match calc_operation:
                case CalcOperations.calculate:
                    self.execute()
                case CalcOperations.C:
                    self.exec_c()
                case CalcOperations.AC:
                    self.exec_ac()
                case CalcOperations.backspace:
                    self.exec_backspace()
                case CalcOperations.number_0:
                    self.exec_number_0()
                case CalcOperations.number_1:
                    self.exec_number_1()
                case CalcOperations.number_2:
                    self.exec_number_2()
                case CalcOperations.number_3:
                    self.exec_number_3()
                case CalcOperations.number_4:
                    self.exec_number_4()
                case CalcOperations.number_5:
                    self.exec_number_5()
                case CalcOperations.number_6:
                    self.exec_number_6()
                case CalcOperations.number_7:
                    self.exec_number_7()
                case CalcOperations.number_8:
                    self.exec_number_8()
                case CalcOperations.number_9:
                    self.exec_number_9()
                case CalcOperations.number_A:
                    self.exec_number_A()
                case CalcOperations.number_B:
                    self.exec_number_B()
                case CalcOperations.number_C:
                    self.exec_number_C()
                case CalcOperations.number_D:
                    self.exec_number_D()
                case CalcOperations.number_E:
                    self.exec_number_E()
                case CalcOperations.number_F:
                    self.exec_number_F()
                case CalcOperations.Plus:
                    self.exec_addition()
                case CalcOperations.Minus:
                    self.exec_subtraction()
                case CalcOperations.square:
                    self.exec_square()
                case CalcOperations.cube:
                    self.exec_cube()
                case CalcOperations.sqrt:
                    self.exec_sqrt()
                case CalcOperations.cube_root:
                    self.exec_cube_root()
                case CalcOperations.pow:
                    self.exec_pow()
                case CalcOperations.ln:
                    self.exec_ln()
                case CalcOperations.ex:
                    self.exec_ex()
                case CalcOperations.log:
                    self.exec_log()
                case CalcOperations.log_base:
                    self.exec_log_base()
                case CalcOperations.ten_power_x:
                    self.exec_ten_power_x()
                case CalcOperations.factorial:
                    self.exec_factorial()
                case CalcOperations.pi:
                    self.exec_pi()
                case CalcOperations.comma:
                    self.exec_decimal_separator()
                case CalcOperations.sin:
                    self.exec_sin()
                case CalcOperations.arcsin:
                    self.exec_arcsin()
                case CalcOperations.cos:
                    self.exec_cos()
                case CalcOperations.arccos:
                    self.exec_arccos()
                case CalcOperations.tan:
                    self.exec_tan()
                case CalcOperations.arctan:
                    self.exec_arctan()
                case CalcOperations.MC:
                    self.exec_MC()
                case CalcOperations.MS:
                    self.exec_MS()
                case CalcOperations.MR:
                    self.exec_MR()
                case CalcOperations.M_plus:
                    self.exec_M_plus()
                case CalcOperations.M_minus:
                    self.exec_M_minus()
                case CalcOperations.M_multiply:
                    self.exec_m_multiply()
                case CalcOperations.M_division:
                    self.exec_m_division()
                case CalcOperations.Multiply:
                    self.exec_multiplication()
                case CalcOperations.opening_bracket:
                    self.exec_opening_bracket()
                case CalcOperations.closing_bracket:
                    self.exec_closing_bracket()
                case CalcOperations.Division:
                    self.exec_division()
                case CalcOperations.mod:
                    self.exec_mod()
                case CalcOperations.reciprocal:
                    self.exec_reciprocal()
                case CalcOperations.sign_change:
                    self.exec_sign_change()
                case CalcOperations.abs:
                    self.exec_abs()
                case CalcOperations.insert_minus:
                    self.exec_insert_minus()
                case CalcOperations.exponent:
                    self.exec_exponent()
                case CalcOperations.comment:
                    self.exec_comment()
                case CalcOperations.cut_to_clipboard:
                    self.exec_cut_to_clipboard()
                case CalcOperations.copy_to_clipboard:
                    self.exec_copy_to_clipboard()
                case CalcOperations.paste_from_clipboard:
                    self.exec_paste_from_clipboard()
                case CalcOperations.undo:
                    self.exec_undo()
                case CalcOperations.redo:
                    self.exec_redo()
                case CalcOperations.swap:
                    self.exec_swap()
                case CalcOperations.memory_swap:
                    self.exec_memory_swap()
                case CalcOperations.percent:
                    self.exec_percent()
                case CalcOperations.convert_to_bases:
                    self.exec_convert_to_bases()
                case CalcOperations.convert_to_dms:
                    self.exec_convert_to_dms()
                case CalcOperations.convert_to_dd:
                    self.exec_convert_to_dd()
                case CalcOperations.sinh:
                    self.exec_sinh()
                case CalcOperations.cosh:
                    self.exec_cosh()
                case CalcOperations.tanh:
                    self.exec_tanh()
                case CalcOperations.arsinh:
                    self.exec_arsinh()
                case CalcOperations.arcosh:
                    self.exec_arcosh()
                case CalcOperations.artanh:
                    self.exec_artanh()
                case CalcOperations.rectangular_to_polar:
                    self.exec_rectangular_to_polar()
                case CalcOperations.polar_to_rectangular:
                    self.exec_polar_to_rectangular()
                case CalcOperations.combination:
                    self.exec_combination()
                case CalcOperations.permutation:
                    self.exec_permutation()
                case CalcOperations.fourth_root:
                    self.exec_fourth_root()
                case CalcOperations.fourth_power:
                    self.exec_fourth_power()
                case CalcOperations.convert_to_deg:
                    self.exec_convert_to_deg()
                case CalcOperations.convert_to_rad:
                    self.exec_convert_to_rad()
                case CalcOperations.convert_to_gra:
                    self.exec_convert_to_gra()
                case CalcOperations.convert_from_binary:
                    self.exec_from_binary()
                case CalcOperations.convert_from_octal:
                    self.exec_from_octal()
                case CalcOperations.convert_from_decimal:
                    self.exec_from_decimal()
                case CalcOperations.convert_from_hexadecimal:
                    self.exec_from_hexadecimal()
                case CalcOperations.toggle_table:
                    self.exec_toggle_table()
                case CalcOperations.numeric_format:
                    self.exec_numeric_format()
                case CalcOperations.round:
                    self.exec_round()
                case CalcOperations.random:
                    self.exec_random()
                case CalcOperations.date_time_stamp:
                    self.exec_date_time_stamp()
                case CalcOperations.phy_const:
                    self.exec_phy_const()
                case CalcOperations.unit_conversion:
                    self.exec_unit_conversion()
                case CalcOperations.del_operation:
                    self.exec_del_operation()
                case CalcOperations.int_part:
                    self.exec_int_part()
                case CalcOperations.frac_part:
                    self.exec_frac_part()
                case CalcOperations.trig_mode_deg:
                    self.exec_trig_mode_deg()
                case CalcOperations.trig_mode_rad:
                    self.exec_trig_mode_rad()
                case CalcOperations.trig_mode_gra:
                    self.exec_trig_mode_gra()
                case CalcOperations.AND:
                    self.exec_AND()
                case CalcOperations.NAND:
                    self.exec_NAND()
                case CalcOperations.XOR:
                    self.exec_XOR()
                case CalcOperations.XNOR:
                    self.exec_XNOR()
                case CalcOperations.OR:
                    self.exec_OR()
                case CalcOperations.NOR:
                    self.exec_NOR()
                case CalcOperations.NOT:
                    self.exec_NOT()
                case CalcOperations.NEG:
                    self.exec_NEG()
                case CalcOperations.word_size_byte:
                    self.exec_word_size_byte()
                case CalcOperations.word_size_word:
                    self.exec_word_size_word()
                case CalcOperations.word_size_dword:
                    self.exec_word_size_dword()
                case CalcOperations.word_size_qword:
                    self.exec_word_size_qword()
                case CalcOperations.number_base_binary:
                    self.set_base(NumberBase.BIN)
                case CalcOperations.number_base_octal:
                    self.set_base(NumberBase.OCT)
                case CalcOperations.number_base_decimal:
                    self.set_base(NumberBase.DEC)
                case CalcOperations.number_base_hexadecimal:
                    self.set_base(NumberBase.HEX)
                case CalcOperations.calc_mode_scientific:
                    self.exec_scientific_mode()
                case CalcOperations.calc_mode_base_n:
                    self.exec_base_n_mode()
                case CalcOperations.calc_mode_complex_numbers:
                    self.exec_complex_numbers_mode()
                case CalcOperations.rectangular_form_complex_number:
                    self.exec_rectangular_form_complex_number()
                case CalcOperations.polar_form_complex_number:
                    self.exec_polar_form_complex_number()
                case CalcOperations.input_complex_number_in_rectangular_form:
                    self.exec_input_complex_number_in_rectangular_form()
                case CalcOperations.input_complex_number_in_polar_form:
                    self.exec_input_complex_number_in_polar_form()
                case CalcOperations.complex_rect_polar_history:
                    self.exec_complex_rect_polar_history()
                case CalcOperations.shift_hold:
                    self.exec_double_shift()
                case CalcOperations.ctrl_hold:
                    self.exec_double_ctrl()
                case CalcOperations.ctrl_shift_hold:
                    self.exec_ctrl_double_shift()
                case CalcOperations.conjugate:
                    self.exec_conjugate()
                case CalcOperations.bitwise_shift_arithmetic:
                    self.exec_bitwise_shift_arithmetic()
                case CalcOperations.bitwise_shift_logical:
                    self.exec_bitwise_shift_logical()
                case CalcOperations.bitwise_shift_circular:
                    self.exec_bitwise_shift_circular()
                case CalcOperations.bitwise_shift_circular_carry:
                    self.exec_bitwise_shift_circular_carry()
                case CalcOperations.left_shift:
                    self.exec_left_shift()
                case CalcOperations.right_shift:
                    self.exec_right_shift()
                case CalcOperations.toggle_carry_flag:
                    self.exec_toggle_carry_flag()
                case CalcOperations.toggle_base_n_sign:
                    self.exec_toggle_base_n_sign()
                case _:
                    self.statusbar_message.emit("No operation configured")
        except Exception as e:
            self._show_error(f"{str(e)}")

        if calc_operation == CalcOperations.toggle_table:
            AppGlobals.history.setFocus()
        else:
            # Determine if input_image_box should receive focus
            focus_flag = calc_operation not in EXCLUDED_OPERATIONS
            if focus_flag:
                AppGlobals.real_part_focus()

        if ((calc_operation is not CalcOperations.shift_hold)
            and (calc_operation is not CalcOperations.ctrl_hold)
            and (calc_operation is not CalcOperations.ctrl_shift_hold)):
            self.reset_hold_flags()

    def exec_decimal_separator(self):
        # decimal separator is always .
        self.insert(self.locale.decimalPoint())

    def focusInEvent(self, event: QFocusEvent):
        self.focusIn.emit()
        super().focusInEvent(event) # Call the base class implementation

    def focusOutEvent(self, event: QFocusEvent):
        self.focusOut.emit()
        super().focusOutEvent(event) # Call the base class implementation        

    @property
    def trig_mode(self):
        return AppGlobals.trig_mode
    
    @trig_mode.setter
    def trig_mode(self, value):
        number, ok = self.locale.toDouble(self.text())

        AppGlobals.trig_mode = value

        match value:
            case TrigMode.RAD:
                if ok and AppGlobals.convert_angle_on_unit_change:
                    self.setTextSelect(self.toString(AppGlobals.angle_unit.to_rad_with_protocol(number)))
                AppGlobals.angle_unit = RadUnitProtocol(self.statusbar_message)
            case TrigMode.GRA:
                if ok and AppGlobals.convert_angle_on_unit_change:
                    self.setTextSelect(self.toString(AppGlobals.angle_unit.to_gra_with_protocol(number)))
                AppGlobals.angle_unit = GraUnitProtocol(self.statusbar_message)
            case _:
                if ok and AppGlobals.convert_angle_on_unit_change:
                    self.setTextSelect(self.toString(AppGlobals.angle_unit.to_deg_with_protocol(number)))
                AppGlobals.angle_unit = DegUnitProtocol(self.statusbar_message)

    def exec_trig_mode_deg(self):
        self.trig_mode = TrigMode.DEG
        self.trig_mode_changed.emit()

    def exec_trig_mode_rad(self):
        self.trig_mode = TrigMode.RAD
        self.trig_mode_changed.emit()

    def exec_trig_mode_gra(self):
        self.trig_mode = TrigMode.GRA
        self.trig_mode_changed.emit()

    def exec_convert_to_deg(self):
        if self.store_number():
            self.setTextSelect(self.toString(AppGlobals.angle_unit.to_deg_with_protocol(self.number)))

    def exec_convert_to_rad(self):
        if self.store_number():
            self.setTextSelect(self.toString(AppGlobals.angle_unit.to_rad_with_protocol(self.number)))

    def exec_convert_to_gra(self):
        if self.store_number():
            self.setTextSelect(self.toString(AppGlobals.angle_unit.to_gra_with_protocol(self.number)))

    def trig_mode_init(self, value):
        if (value is None):
            value = TrigMode.DEG
        else:
            AppGlobals.trig_mode = TrigMode(value)

        match TrigMode(value):
            case TrigMode.RAD:
                AppGlobals.angle_unit = RadUnitProtocol(self.statusbar_message)
            case TrigMode.GRA:
                AppGlobals.angle_unit = GraUnitProtocol(self.statusbar_message)
            case _:
                AppGlobals.angle_unit = DegUnitProtocol(self.statusbar_message)

    def exec_ln(self):
        if (self.store_number()):
            expr = LnExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_ex(self):
        if self.store_number():
            expr = EPowerXExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_complex_rect_polar_history(self):
        if AppGlobals.calc_mode != CalcMode.complex_numbers:
            self.statusbar_message.emit("Only for Compex Numbers Mode")
            return
        if AppGlobals.input_box.store_number() and AppGlobals.input_imag_box.store_number():
            expr = ComplexRectPolarHistoryExpression()
            result = expr.calculate(AppGlobals.get_complex_number())

    def exec_log(self):
        if (self.store_number()):
            expr = LogExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_ten_power_x(self):
        if (self.store_number()):
            expr = TenPowerXExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_sin(self):
        if (self.store_number()):
            expr = SinExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_arcsin(self):
        if (self.store_number()):
            expr = ArcSinExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_cos(self):
        if (self.store_number()):
            expr = CosExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_arccos(self):
        if (self.store_number()):
            expr = ArcCosExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_tan(self):
        if (self.store_number()):
            expr = TanExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_arctan(self):
        if (self.store_number()):
            expr = ArcTanExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def handle_keys_check_errors(self, event):
        try:
            self.handle_keys(event)
        except Exception as e:
            self._show_error(f"{str(e)}")

    def exec_number_0(self):
        self.insert("0")

    def exec_number_1(self):
        self.insert("1")

    def exec_number_2(self):
        self.insert("2")

    def exec_number_3(self):
        self.insert("3")

    def exec_number_4(self):
        self.insert("4")

    def exec_number_5(self):
        self.insert("5")        

    def exec_number_6(self):
        self.insert("6")        

    def exec_number_7(self):
        self.insert("7")        

    def exec_number_8(self):
        self.insert("8")        

    def exec_number_9(self):
        self.insert("9")        

    def exec_number_A(self):
        self.insert("A")        

    def exec_number_B(self):
        self.insert("B")        

    def exec_number_C(self):
        self.insert("C")        

    def exec_number_D(self):
        self.insert("D")        

    def exec_number_E(self):
        self.insert("E")        

    def exec_number_F(self):
        self.insert("F")        

    @property
    def memory(self):
        return self._memory
    
    @memory.setter
    def memory(self, value: float):
        self._memory = value
        self.memory_changed.emit(self.memory_to_format_string())
        
    def exec_MS(self):
        if self.store_number():
            AppGlobals.set_memory(AppGlobals.get_number())
            # show in protocol
            MSExpression().calculate(AppGlobals.get_number())

    def exec_MC(self):
        AppGlobals.input_box.memory = 0
        AppGlobals.input_imag_box.memory = 0
        MSExpression().calculate(AppGlobals.get_memory())

    def exec_MR(self):
        AppGlobals.number_to_input_box(AppGlobals.get_memory())

    def exec_M_plus(self):
        if self.store_number():
            expr = MPlusExpression(AppGlobals.get_memory())
            AppGlobals.set_memory(expr.calculate(AppGlobals.get_number()))

    def exec_M_minus(self):
        if self.store_number():
            expr = MMinusExpression(AppGlobals.get_memory())
            AppGlobals.set_memory(expr.calculate(AppGlobals.get_number()))

    def exec_m_multiply(self):
        if self.store_number():
            expr = MMultiplyExpression(AppGlobals.get_memory())
            AppGlobals.set_memory(expr.calculate(AppGlobals.get_number()))

    def exec_m_division(self):
        if self.store_number():
            expr = MDisivionExpression(AppGlobals.get_memory())
            AppGlobals.set_memory(expr.calculate(AppGlobals.get_number()))

    def exec_backspace(self):
        self.backspace()

    def exec_reciprocal(self):
        if (self.store_number()):
            expr = ReciprocalExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_sign_change(self):
        if (self.store_number()):
            self.setTextSelect(self.toString(-1.0 * self.number))

    def exec_abs(self):
        if (self.store_number()):
            expr = AbsExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_conjugate(self):
        if (self.store_number()):
            expr = ConjugateExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_insert_minus(self):
        self.insert("-")

    def exec_exponent(self):
        self.insert("e")

    def exec_comment(self):
        dialog = CommentDialog()
        dialog.ui.lineEdit.setText(self.text())
        if dialog.exec():
            comment = dialog.get_comment()
            CommentCellValue(comment, is_bold=True)

    def get_key_state(self, key_code):
        return bool(ctypes.windll.user32.GetKeyState(key_code) & 0x0001)
    
    def numlock_state(self):
        return self.get_key_state(0x90)

    def handle_numpad_keys(self, event):
        if (self.current_physical_shift_state and self.current_ctrl_state) or AppGlobals.ctrl_shift_hold:
            match self.key:
                case Qt.Key_Plus:
                    self.button_clicked(UiGlobals.pushButtonPlusNumpad.ctrl_shift_operation)
                case Qt.Key_Minus:
                    self.button_clicked(UiGlobals.pushButtonMinusNumpad.ctrl_shift_operation)
                case Qt.Key.Key_Asterisk:
                    self.button_clicked(UiGlobals.pushButtonMultiplyNumpad.ctrl_shift_operation)
                case Qt.Key.Key_Delete: # Numpad comma
                    self.button_clicked(UiGlobals.pushButtonCommaNumpad.ctrl_shift_operation)
                case Qt.Key.Key_Slash:
                    self.button_clicked(UiGlobals.pushButtonDivideNumpad.ctrl_shift_operation)
                case Qt.Key.Key_Insert: # Numpad 0
                    self.button_clicked(UiGlobals.pushButton0numpad.ctrl_shift_operation)
                case Qt.Key.Key_End:
                    self.button_clicked(UiGlobals.pushButton1numpad.ctrl_shift_operation)
                case Qt.Key.Key_Down:
                    self.button_clicked(UiGlobals.pushButton2numpad.ctrl_shift_operation)
                case Qt.Key.Key_PageDown:
                    self.button_clicked(UiGlobals.pushButton3numpad.ctrl_shift_operation)
                case Qt.Key.Key_Home: # Numpad 7
                    self.button_clicked(UiGlobals.pushButton7numpad.ctrl_shift_operation)
                case Qt.Key.Key_Up:
                    self.button_clicked(UiGlobals.pushButton8numpad.ctrl_shift_operation)
                case Qt.Key.Key_PageUp:
                    self.button_clicked(UiGlobals.pushButton9numpad.ctrl_shift_operation)
                case Qt.Key.Key_Left:
                    self.button_clicked(UiGlobals.pushButton4numpad.ctrl_shift_operation)
                case Qt.Key.Key_Clear:
                    self.button_clicked(UiGlobals.pushButton5numpad.ctrl_shift_operation)
                case Qt.Key.Key_Right:
                    self.button_clicked(UiGlobals.pushButton6numpad.ctrl_shift_operation)
                case Qt.Key.Key_Enter:
                    self.button_clicked(UiGlobals.pushButtonEnterNumpad.ctrl_shift_operation)
                case Qt.Key.Key_Comma:
                    self.button_clicked(UiGlobals.pushButtonCommaNumpad.ctrl_shift_operation)
                case Qt.Key.Key_0: # Numpad 0
                    self.button_clicked(UiGlobals.pushButton0numpad.ctrl_shift_operation)
                case Qt.Key.Key_1: # Numpad 1
                    self.button_clicked(UiGlobals.pushButton1numpad.ctrl_shift_operation)
                case Qt.Key.Key_2: # Numpad 2
                    self.button_clicked(UiGlobals.pushButton2numpad.ctrl_shift_operation)
                case Qt.Key.Key_3: # Numpad 3
                    self.button_clicked(UiGlobals.pushButton3numpad.ctrl_shift_operation)
                case Qt.Key.Key_4: # Numpad 4
                    self.button_clicked(UiGlobals.pushButton4numpad.ctrl_shift_operation)
                case Qt.Key.Key_5: # Numpad 5
                    self.button_clicked(UiGlobals.pushButton5numpad.ctrl_shift_operation)
                case Qt.Key.Key_6: # Numpad 6
                    self.button_clicked(UiGlobals.pushButton6numpad.ctrl_shift_operation)
                case Qt.Key.Key_7: # Numpad 7
                    self.button_clicked(UiGlobals.pushButton7numpad.ctrl_shift_operation)
                case Qt.Key.Key_8: # Numpad 8
                    self.button_clicked(UiGlobals.pushButton8numpad.ctrl_shift_operation)
                case Qt.Key.Key_9: # Numpad 9
                    self.button_clicked(UiGlobals.pushButton9numpad.ctrl_shift_operation)
                case _:
                    # Call base class to keep normal behavior
                    super().keyPressEvent(event)
                    self.statusbar_message.emit("No operation configured")
        elif self.current_ctrl_state or AppGlobals.ctrl_hold:
            # ctrl is pressed
            # And possible Shift special case, because Shift is suppressed by os
            match self.key:
                case Qt.Key_Enter | Qt.Key_Return | Qt.Key_Equal:         
                    self.button_clicked(UiGlobals.pushButtonEnterNumpad.ctrl_operation)
                case Qt.Key.Key_Comma:
                    self.button_clicked(UiGlobals.pushButtonCommaNumpad.ctrl_operation)
                case Qt.Key.Key_0: # Numpad 0
                    self.button_clicked(UiGlobals.pushButton0numpad.ctrl_operation)
                case Qt.Key.Key_1: # Numpad 1
                    self.button_clicked(UiGlobals.pushButton1numpad.ctrl_operation)
                case Qt.Key.Key_2: # Numpad 2
                    self.button_clicked(UiGlobals.pushButton2numpad.ctrl_operation)
                case Qt.Key.Key_3: # Numpad 3
                    self.button_clicked(UiGlobals.pushButton3numpad.ctrl_operation)
                case Qt.Key.Key_4: # Numpad 4
                    self.button_clicked(UiGlobals.pushButton4numpad.ctrl_operation)
                case Qt.Key.Key_5: # Numpad 5
                    self.button_clicked(UiGlobals.pushButton5numpad.ctrl_operation)
                case Qt.Key.Key_6: # Numpad 6
                    self.button_clicked(UiGlobals.pushButton6numpad.ctrl_operation)
                case Qt.Key.Key_7: # Numpad 7
                    self.button_clicked(UiGlobals.pushButton7numpad.ctrl_operation)
                case Qt.Key.Key_8: # Numpad 8
                    self.button_clicked(UiGlobals.pushButton8numpad.ctrl_operation)
                case Qt.Key.Key_9: # Numpad 9
                    self.button_clicked(UiGlobals.pushButton9numpad.ctrl_operation)
                case Qt.Key_Plus:
                    self.button_clicked(UiGlobals.pushButtonPlusNumpad.ctrl_operation)
                case Qt.Key_Minus:
                    self.button_clicked(UiGlobals.pushButtonMinusNumpad.ctrl_operation)
                case Qt.Key.Key_Asterisk:
                    self.button_clicked(UiGlobals.pushButtonMultiplyNumpad.ctrl_operation)
                case Qt.Key.Key_Slash:
                    self.button_clicked(UiGlobals.pushButtonDivideNumpad.ctrl_operation)
                case _:
                    # Call base class to keep normal behavior
                    super().keyPressEvent(event)
                    self.statusbar_message.emit("No operation configured")
        elif self.current_shift_state or AppGlobals.shift_hold:
            # shift was pressed
            match self.key:
                case Qt.Key.Key_NumLock:
                    if AppGlobals.numlock_ac:
                        self.button_clicked(UiGlobals.pushButtonAC.shift_operation)
                    super().keyPressEvent(event)
                case Qt.Key_Enter | Qt.Key_Return | Qt.Key_Equal:         
                    self.button_clicked(UiGlobals.pushButtonEnterNumpad.shift_operation)
                case Qt.Key.Key_Comma:
                    self.button_clicked(UiGlobals.pushButtonCommaNumpad.shift_operation)
                case Qt.Key.Key_0: # Numpad 0
                    self.button_clicked(UiGlobals.pushButton0numpad.shift_operation)
                case Qt.Key.Key_1: # Numpad 1
                    self.button_clicked(UiGlobals.pushButton1numpad.shift_operation)
                case Qt.Key.Key_2: # Numpad 2
                    self.button_clicked(UiGlobals.pushButton2numpad.shift_operation)
                case Qt.Key.Key_3: # Numpad 3
                    self.button_clicked(UiGlobals.pushButton3numpad.shift_operation)
                case Qt.Key.Key_4: # Numpad 4
                    self.button_clicked(UiGlobals.pushButton4numpad.shift_operation)
                case Qt.Key.Key_5: # Numpad 5
                    self.button_clicked(UiGlobals.pushButton5numpad.shift_operation)
                case Qt.Key.Key_6: # Numpad 6
                    self.button_clicked(UiGlobals.pushButton6numpad.shift_operation)
                case Qt.Key.Key_7: # Numpad 7
                    self.button_clicked(UiGlobals.pushButton7numpad.shift_operation)
                case Qt.Key.Key_8: # Numpad 8
                    self.button_clicked(UiGlobals.pushButton8numpad.shift_operation)
                case Qt.Key.Key_9: # Numpad 9
                    self.button_clicked(UiGlobals.pushButton9numpad.shift_operation)
                case Qt.Key.Key_Plus:
                    self.button_clicked(UiGlobals.pushButtonPlusNumpad.shift_operation)
                case Qt.Key_Minus:
                    self.button_clicked(UiGlobals.pushButtonMinusNumpad.shift_operation)
                case Qt.Key.Key_Asterisk:
                    self.button_clicked(UiGlobals.pushButtonMultiplyNumpad.shift_operation)
                case Qt.Key.Key_Slash:
                    self.button_clicked(UiGlobals.pushButtonDivideNumpad.shift_operation)
                case _:
                    # Call base class to keep normal behavior
                    super().keyPressEvent(event)
                    self.statusbar_message.emit("No operation configured")
        else:
            # no shift and no ctrl was pressed or shift is supressed by os
            match self.key:
                case Qt.Key.Key_NumLock:
                    if AppGlobals.numlock_ac:
                        self.button_clicked(UiGlobals.pushButtonAC.base_operation)
                    super().keyPressEvent(event)
                case Qt.Key.Key_Insert: # Numpad 0
                    self.button_clicked(UiGlobals.pushButton0numpad.shift_operation)
                case Qt.Key.Key_Comma: # Numpad decimal separator
                    self.button_clicked(UiGlobals.pushButtonCommaNumpad.base_operation)
                case Qt.Key.Key_Delete: # Numpad comma
                    self.button_clicked(UiGlobals.pushButtonCommaNumpad.shift_operation)
                case Qt.Key.Key_End: # Numpad 1
                    self.button_clicked(UiGlobals.pushButton1numpad.shift_operation)
                case Qt.Key.Key_Down: # Numpad 2
                    self.button_clicked(UiGlobals.pushButton2numpad.shift_operation)
                case Qt.Key.Key_PageDown: # Numpad 3
                    self.button_clicked(UiGlobals.pushButton3numpad.shift_operation)
                case Qt.Key.Key_Left: # Numpad 4
                    self.button_clicked(UiGlobals.pushButton4numpad.shift_operation)
                case Qt.Key.Key_Clear: #Numpad 5
                    self.button_clicked(UiGlobals.pushButton5numpad.shift_operation)
                case Qt.Key.Key_Right: # Numpad 6
                    self.button_clicked(UiGlobals.pushButton6numpad.shift_operation)
                case Qt.Key.Key_Home: # Numpad 7
                    self.button_clicked(UiGlobals.pushButton7numpad.shift_operation)
                case Qt.Key.Key_Up: # Numpad 8
                    self.button_clicked(UiGlobals.pushButton8numpad.shift_operation)
                case Qt.Key.Key_PageUp: # Numpad 9
                    self.button_clicked(UiGlobals.pushButton9numpad.shift_operation)
                case Qt.Key.Key_Plus:
                    self.button_clicked(UiGlobals.pushButtonPlusNumpad.base_operation)
                case Qt.Key.Key_Minus:
                    self.button_clicked(UiGlobals.pushButtonMinusNumpad.base_operation)
                case Qt.Key.Key_multiply | Qt.Key.Key_Asterisk:
                    self.button_clicked(UiGlobals.pushButtonMultiplyNumpad.base_operation)
                case Qt.Key.Key_Slash | Qt.Key.Key_division:
                    self.button_clicked(UiGlobals.pushButtonDivideNumpad.base_operation)
                case Qt.Key.Key_Enter | Qt.Key.Key_Return | Qt.Key.Key_Equal:         
                    self.button_clicked(UiGlobals.pushButtonEnterNumpad.base_operation)
                case _:
                    # Call base class to keep normal behavior
                    super().keyPressEvent(event)

    def handle_chars(self, event):
        if self.current_ctrl_state:
            # Exception for German keyboard, where ~ is on the key with + and * and requires ctrl+alt (Alt Gr) to type
            if self.char_pressed == '~':
                self.exec_NOT()
                return True
            return False # No char handling when ctrl is pressed
        
        match self.char_pressed:
            # chars '1' - '6' are moved to scancodes, because of e. g. '5'
            # by 4th function still produce number_5
            case '0':
                self.button_clicked(CalcOperations.number_0)
            case '7':
                self.button_clicked(CalcOperations.number_7)
            case '8':
                self.button_clicked(CalcOperations.number_8)
            case '9':
                self.button_clicked(CalcOperations.number_9)
            case '.':
                self.button_clicked(CalcOperations.comma)
            case ',':
                if AppGlobals.input_replace_decimal_separator:
                    self.button_clicked(CalcOperations.comma)
                else:
                    super().keyPressEvent(event)
            case '!':
                self.button_clicked(CalcOperations.factorial)
            case "%":
                self.button_clicked(CalcOperations.percent)
            case '_':
                self.button_clicked(CalcOperations.insert_minus)
            case '=':
                self.button_clicked(CalcOperations.calculate)
            case '(':
                self.button_clicked(CalcOperations.opening_bracket)
            case ')':
                self.button_clicked(CalcOperations.closing_bracket)
            case '+':
                self.button_clicked(CalcOperations.Plus)
            case '-':
                self.button_clicked(CalcOperations.Minus)
            case '*':
                self.button_clicked(CalcOperations.Multiply)
            case '/':
                self.button_clicked(CalcOperations.Division)
            case '^':
                self.button_clicked(CalcOperations.pow)
            case '|':
                self.button_clicked(CalcOperations.OR)
            case '~':
                self.button_clicked(CalcOperations.NOT)
            case _:
                return False
        return True

    def hadle_chars_virtual_key(self, event):
        match self.key:
            case Qt.Key.Key_Plus:
                self.button_clicked(CalcOperations.Plus)
            case Qt.Key.Key_Minus:
                self.button_clicked(CalcOperations.Minus)
            case Qt.Key.Key_Asterisk:
                self.button_clicked(CalcOperations.Multiply)
            case Qt.Key.Key_Slash:
                self.button_clicked(CalcOperations.Division)
            case Qt.Key.Key_ParenLeft:
                self.button_clicked(CalcOperations.opening_bracket)
            case Qt.Key.Key_ParenRight:
                self.button_clicked(CalcOperations.closing_bracket)
            case Qt.Key.Key_Equal:
                self.button_clicked(CalcOperations.calculate)
            case Qt.Key.Key_Percent:
                # Check the ctrl state for case ctrl+shift
                if self.current_ctrl_state:
                    return False
                self.button_clicked(CalcOperations.percent)
            case Qt.Key.Key_Exclam:
                # Check the ctrl state for case ctrl+shift
                if self.current_ctrl_state:
                    return False
                self.button_clicked(CalcOperations.factorial)
            case Qt.Key.Key_Underscore:
                if self.current_ctrl_state:
                    self.exec_sign_change()
                    self.button_clicked(CalcOperations.sign_change)
                else:
                    self.button_clicked(CalcOperations.insert_minus)
            case _:
                return False
        return True
    
    def handle_scan_codes(self):
        if (self.current_ctrl_state and self.current_shift_state) or AppGlobals.ctrl_shift_hold:
            # ctrl+shift pressed
            match self.scan_code:
                case 2: # Key 1
                    self.button_clicked(UiGlobals.pushButton1.ctrl_shift_operation)
                case 3: # Key 2
                    self.button_clicked(UiGlobals.pushButton2.ctrl_shift_operation)
                case 4: # Key 3
                    self.button_clicked(UiGlobals.pushButton3.ctrl_shift_operation)
                case 5: # Key 4
                    self.button_clicked(UiGlobals.pushButton4.ctrl_shift_operation)
                case 6: # Key 5
                    self.button_clicked(UiGlobals.pushButton5.ctrl_shift_operation)
                case 7: # Key 6
                    self.button_clicked(UiGlobals.pushButton6.ctrl_shift_operation)
                case 16: # Key Q
                    self.button_clicked(UiGlobals.pushButtonQ.ctrl_shift_operation)
                case 17: # Key W
                    self.button_clicked(UiGlobals.pushButtonW.ctrl_shift_operation)
                case 18: # Key E
                    self.button_clicked(UiGlobals.pushButtonE.ctrl_shift_operation)
                case 19: # Key R
                    self.button_clicked(UiGlobals.pushButtonR.ctrl_shift_operation)
                case 20: # Key T
                    self.button_clicked(UiGlobals.pushButtonT.ctrl_shift_operation)
                case 21: # Key Y in QWERTY
                    self.button_clicked(UiGlobals.pushButtonZ.ctrl_shift_operation)
                case 30: # Key A
                    self.button_clicked(UiGlobals.pushButtonA.ctrl_shift_operation)
                case 31: # Key S
                    self.button_clicked(UiGlobals.pushButtonS.ctrl_shift_operation)
                case 32: # Key D
                    self.button_clicked(UiGlobals.pushButtonD.ctrl_shift_operation)
                case 33: # Key F
                    self.button_clicked(UiGlobals.pushButtonF.ctrl_shift_operation)
                case 34: # Key G
                    self.button_clicked(UiGlobals.pushButtonG.ctrl_shift_operation)
                case 44: # Key Z in QWERTY
                    self.button_clicked(UiGlobals.pushButtonY.ctrl_shift_operation)
                case 45: # Key X
                    self.button_clicked(UiGlobals.pushButtonX.ctrl_shift_operation)
                case 46: # Key C
                    self.button_clicked(UiGlobals.pushButtonC.ctrl_shift_operation)
                case 47: # Key V
                    self.button_clicked(UiGlobals.pushButtonV.ctrl_shift_operation)
                case 48: # Key B
                    self.button_clicked(UiGlobals.pushButtonB.ctrl_shift_operation)
                case 86: # Key \ in QWERTY
                    self.button_clicked(UiGlobals.pushButtonLess.ctrl_shift_operation)
                case _:
                    return False # False is case _:
            return True
        elif self.current_shift_state or AppGlobals.shift_hold:
            # shift pressed
            match self.scan_code:
                case 2: # Key 1
                    self.button_clicked(UiGlobals.pushButton1.shift_operation)
                case 3: # Key 2
                    self.button_clicked(UiGlobals.pushButton2.shift_operation)
                case 4: # Key 3
                    self.button_clicked(UiGlobals.pushButton3.shift_operation)
                case 5: # Key 4
                    self.button_clicked(UiGlobals.pushButton4.shift_operation)
                case 6: # Key 5
                    self.button_clicked(UiGlobals.pushButton5.shift_operation)
                case 7: # Key 6
                    self.button_clicked(UiGlobals.pushButton6.shift_operation)
                case 16: # Key Q
                    self.button_clicked(UiGlobals.pushButtonQ.shift_operation)
                case 17: # Key W
                    self.button_clicked(UiGlobals.pushButtonW.shift_operation)
                case 18: # Key E
                    self.button_clicked(UiGlobals.pushButtonE.shift_operation)
                case 19: # Key R
                    self.button_clicked(UiGlobals.pushButtonR.shift_operation)
                case 20: # Key T
                    self.button_clicked(UiGlobals.pushButtonT.shift_operation)
                case 21: # Key Y in QWERTY
                    self.button_clicked(UiGlobals.pushButtonZ.shift_operation)
                case 30: # Key A
                    self.button_clicked(UiGlobals.pushButtonA.shift_operation)
                case 31: # Key S
                    self.button_clicked(UiGlobals.pushButtonS.shift_operation)
                case 32: # Key D
                    self.button_clicked(UiGlobals.pushButtonD.shift_operation)
                case 33: # Key F
                    self.button_clicked(UiGlobals.pushButtonF.shift_operation)
                case 34: # Key G
                    self.button_clicked(UiGlobals.pushButtonG.shift_operation)
                case 44: # Key Z in QWERTY
                    self.button_clicked(UiGlobals.pushButtonY.shift_operation)
                case 45: # Key X
                    self.button_clicked(UiGlobals.pushButtonX.shift_operation)
                case 46: # Key C
                    self.button_clicked(UiGlobals.pushButtonC.shift_operation)
                case 47: # Key V
                    self.button_clicked(UiGlobals.pushButtonV.shift_operation)
                case 48: # Key B
                    self.button_clicked(UiGlobals.pushButtonB.shift_operation)
                case 86: # Key \ in QWERTY
                    self.button_clicked(UiGlobals.pushButtonLess.shift_operation)
                case _:
                    return False # False is case _:
            return True
        elif self.current_ctrl_state or AppGlobals.ctrl_hold:
            # ctrl_pressed
            match self.scan_code:
                case 2: # Key 1
                    self.button_clicked(UiGlobals.pushButton1.ctrl_operation)
                case 3: # Key 2
                    self.button_clicked(UiGlobals.pushButton2.ctrl_operation)
                case 4: # Key 3
                    self.button_clicked(UiGlobals.pushButton3.ctrl_operation)
                case 5: # Key 4
                    self.button_clicked(UiGlobals.pushButton4.ctrl_operation)
                case 6: # Key 5
                    self.button_clicked(UiGlobals.pushButton5.ctrl_operation)
                case 7: # Key 6
                    self.button_clicked(UiGlobals.pushButton6.ctrl_operation)
                case 86: # Key \ in QWERTY
                    self.button_clicked(UiGlobals.pushButtonLess.ctrl_operation)
                case _:
                    return False
            return True # False is case _:
        else:
            # no shift and no ctrl pressed
            # only for the showed keys on left side of keyboard
            match self.scan_code:
                case 2: # Key 1
                    self.button_clicked(UiGlobals.pushButton1.base_operation)
                case 3: # Key 2
                    self.button_clicked(UiGlobals.pushButton2.base_operation)
                case 4: # Key 3
                    self.button_clicked(UiGlobals.pushButton3.base_operation)
                case 5: # Key 4
                    self.button_clicked(UiGlobals.pushButton4.base_operation)
                case 6: # Key 5
                    self.button_clicked(UiGlobals.pushButton5.base_operation)
                case 7: # Key 6
                    self.button_clicked(UiGlobals.pushButton6.base_operation)
                case 16: # Key Q
                    self.button_clicked(UiGlobals.pushButtonQ.base_operation)
                case 17: # Key W
                    self.button_clicked(UiGlobals.pushButtonW.base_operation)
                case 18: # Key E
                    self.button_clicked(UiGlobals.pushButtonE.base_operation)
                case 19: # Key R
                    self.button_clicked(UiGlobals.pushButtonR.base_operation)
                case 20: # Key T
                    self.button_clicked(UiGlobals.pushButtonT.base_operation)
                case 21: # Key Y in QWERTY
                    self.button_clicked(UiGlobals.pushButtonZ.base_operation)
                case 30: # Key A
                    self.button_clicked(UiGlobals.pushButtonA.base_operation)
                case 31: # Key S
                    self.button_clicked(UiGlobals.pushButtonS.base_operation)
                case 32: # Key D
                    self.button_clicked(UiGlobals.pushButtonD.base_operation)
                case 33: # Key F
                    self.button_clicked(UiGlobals.pushButtonF.base_operation)
                case 34: # Key G
                    self.button_clicked(UiGlobals.pushButtonG.base_operation)
                case 44: # Key Z in QWERTY
                    self.button_clicked(UiGlobals.pushButtonY.base_operation)
                case 45: # Key X
                    self.button_clicked(UiGlobals.pushButtonX.base_operation)
                case 46: # Key C
                    self.button_clicked(UiGlobals.pushButtonC.base_operation)
                case 47: # Key V
                    self.button_clicked(UiGlobals.pushButtonV.base_operation)
                case 48: # Key B
                    self.button_clicked(UiGlobals.pushButtonB.base_operation)
                case 86: # Key \ in QWERTY
                    self.button_clicked(UiGlobals.pushButtonLess.base_operation)
                case _:
                    return False
            return True # False is case _:

    def handle_keys(self, event):
        allowed_chars = "+-.0123456789eE"
        if AppGlobals.calc_mode is CalcMode.base_n and AppGlobals.number_base is NumberBase.HEX:
            allowed_chars = "+-.0123456789aAbBcCdDeEfF"
        if (event.modifiers() & Qt.KeypadModifier) and self.numlock_state(): # keypad keys
            self.handle_numpad_keys(event)
        else: # usual keys (no keypad keys)
            print("usual keys (no keypad keys)")
            if self.handle_chars(event):
                return # it was a char, no further handling
            if self.hadle_chars_virtual_key(event):
                return # it was a char_virtual_key, no further handling
            if self.handle_scan_codes():
                return

            if (self.current_shift_state and self.current_ctrl_state) or AppGlobals.ctrl_shift_hold:
                # Shift+Ctrl pressed
                match self.key:
                    case Qt.Key_Enter | Qt.Key_Return:
                        self.button_clicked(UiGlobals.pushButtonEnter.ctrl_shift_operation)
                    case Qt.Key.Key_Escape:
                        self.button_clicked(CalcOperations.AC)
                    case Qt.Key.Key_PageUp:
                        # 4th function is active, aktivate 3rd function
                        self.button_clicked(CalcOperations.ctrl_hold)
                    case Qt.Key.Key_PageDown:
                        # 4th function is active, deactivate it
                        self.button_clicked(CalcOperations.ctrl_shift_hold)
            elif self.current_shift_state or AppGlobals.shift_hold:
                # Shift pressed
                match self.key:
                    case Qt.Key.Key_Backspace:
                        self.button_clicked(UiGlobals.pushButtonBackspace.shift_operation)
                    case Qt.Key.Key_Space:
                        self.button_clicked(UiGlobals.pushButtonSpace.shift_operation)
                    case Qt.Key_Enter | Qt.Key_Return:
                        self.button_clicked(UiGlobals.pushButtonEnter.shift_operation)
                    case Qt.Key_Delete:
                        # Call base class to keep normal behavior
                        super().keyPressEvent(event)
                    case Qt.Key.Key_Escape:
                        self.button_clicked(CalcOperations.AC)
                    case Qt.Key.Key_PageUp:
                        # 2nd function is active, make 3th function
                        self.button_clicked(CalcOperations.ctrl_hold)
                    case Qt.Key.Key_PageDown:
                        # 2nd function is active, make 4th function
                        self.button_clicked(CalcOperations.ctrl_shift_hold)
                    case _:
                        if not self.char_pressed in allowed_chars:
                            self.statusbar_message.emit("Symbol ignored: " + self.char_pressed)
                        else:
                            # Call base class to keep normal behavior
                            super().keyPressEvent(event)
                            print("Default operation")
            elif self.current_ctrl_state or AppGlobals.ctrl_hold:
                # ctrl pressed
                match self.key:
                    case Qt.Key.Key_Q:
                        self.button_clicked(UiGlobals.pushButtonQ.ctrl_operation)
                    case Qt.Key.Key_W:
                        self.button_clicked(UiGlobals.pushButtonW.ctrl_operation)
                    case Qt.Key.Key_E:
                        self.button_clicked(UiGlobals.pushButtonE.ctrl_operation)
                    case Qt.Key.Key_R:
                        self.button_clicked(UiGlobals.pushButtonR.ctrl_operation)
                    case Qt.Key.Key_T:
                        self.button_clicked(UiGlobals.pushButtonT.ctrl_operation)
                    case Qt.Key.Key_A:
                        self.button_clicked(UiGlobals.pushButtonA.ctrl_operation)
                    case Qt.Key.Key_S:
                        self.button_clicked(UiGlobals.pushButtonS.ctrl_operation)
                    case Qt.Key.Key_D:
                        self.button_clicked(UiGlobals.pushButtonD.ctrl_operation)
                    case Qt.Key.Key_G:
                        self.button_clicked(UiGlobals.pushButtonG.ctrl_operation)
                    # handle copy/paste with possible replacing            
                    case Qt.Key.Key_X:
                        self.button_clicked(UiGlobals.pushButtonX.ctrl_operation)
                    case Qt.Key.Key_C:
                        self.button_clicked(UiGlobals.pushButtonC.ctrl_operation)
                    case Qt.Key.Key_V:
                        self.button_clicked(UiGlobals.pushButtonV.ctrl_operation)
                    case Qt.Key.Key_B:
                        self.button_clicked(UiGlobals.pushButtonB.ctrl_operation)
                    case Qt.Key.Key_Space:
                        self.button_clicked(UiGlobals.pushButtonSpace.ctrl_operation)
                    case Qt.Key.Key_Backspace:
                        self.button_clicked(UiGlobals.pushButtonBackspace.ctrl_operation)
                    case Qt.Key_Enter | Qt.Key_Return:
                        self.button_clicked(UiGlobals.pushButtonEnter.ctrl_operation)
                    case Qt.Key.Key_Escape:
                        self.button_clicked(CalcOperations.AC)
                    case Qt.Key_Delete:
                        # Call base class to keep normal behavior
                        super().keyPressEvent(event)
                    case Qt.Key.Key_Z:
                        self.button_clicked(UiGlobals.pushButtonZ.ctrl_operation)
                    case Qt.Key.Key_Y:
                        self.button_clicked(UiGlobals.pushButtonY.ctrl_operation)
                    case Qt.Key.Key_PageUp:
                        # 3rd function is active, deactivate it
                        self.button_clicked(CalcOperations.ctrl_hold)
                    case Qt.Key.Key_PageDown:
                        # 3rd function is active, make 2nd function
                        self.button_clicked(CalcOperations.shift_hold)
                    case _:
                        if not self.char_pressed in allowed_chars:
                            self.statusbar_message.emit("Symbol ignored: " + self.char_pressed)
                        else:
                            # Call base class to keep normal behavior
                            super().keyPressEvent(event)
                            print("Default operation")
            else:
                # just keys, no shift, no ctrl
                match self.key:
                    case Qt.Key.Key_Comma:
                        if AppGlobals.input_replace_decimal_separator:
                            # Simulate point press instead
                            super().keyPressEvent(QKeyEvent(
                                QKeyEvent.KeyPress,
                                Qt.Key_Comma,
                                Qt.NoModifier,
                                "."
                            ))
                        else:
                            super().keyPressEvent(event)
                    case Qt.Key.Key_Up:
                        self.button_clicked(CalcOperations.toggle_table)
                    case Qt.Key.Key_Escape:
                        self.button_clicked(CalcOperations.AC)
                    case Qt.Key_Enter | Qt.Key_Return | Qt.Key_Equal:
                        self.button_clicked(CalcOperations.calculate)
                    case Qt.Key.Key_Space:
                        self.exec_comment()
                    case Qt.Key.Key_Backspace:
                        # Call base class to keep normal behavior
                        super().keyPressEvent(event)
                    case Qt.Key_Delete:
                        # Call base class to keep normal behavior
                        super().keyPressEvent(event)
                    case Qt.Key.Key_PageUp:
                        self.button_clicked(CalcOperations.ctrl_hold)
                    case Qt.Key.Key_PageDown:
                        self.button_clicked(CalcOperations.shift_hold)
                    case _:
                        if not self.char_pressed in allowed_chars:
                            self.statusbar_message.emit("Symbol ignored: " + self.char_pressed)
                        else:
                            # Call base class to keep normal behavior
                            super().keyPressEvent(event)
                            print("Default operation")

    def exec_cut_to_clipboard(self):
        self.cut()

    def exec_copy_to_clipboard(self):
        self.handle_copy()

    def exec_paste_from_clipboard(self):
        self.handle_paste()

    def exec_undo(self):
        self.undo()
    
    def exec_redo(self):
        self.redo()

    def exec_square(self):
        if (self.store_number()):
            expr = SquareExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_cube(self):
        if (self.store_number()):
            expr = CubeExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_fourth_power(self):
        if self.store_number():
            expr = FourthPowerExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_sqrt(self):
        if self.store_number():
            expr = SqrtExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_cube_root(self):
        if self.store_number():
            expr = CubeRootExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_fourth_root(self):
        if self.store_number():
            expr = FourthRootExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_memory_swap(self):
        if self.store_number():
            temp_number = AppGlobals.get_number()
            self.setTextSelect(self.memory_to_string())
            AppGlobals.number_to_input_box(AppGlobals.get_memory())
            AppGlobals.set_memory(temp_number)
            MSExpression().calculate(AppGlobals.get_memory())

    def exec_swap(self):
        if AppGlobals.root_expression != None:
            if self.store_number():
                temp_number = self.last_expression().first_number
                self.last_expression().first_number = AppGlobals.get_number()
                AppGlobals.number_to_input_box(temp_number)
                self.update_expression_label()

    def exec_convert_to_bases(self):
        if self.store_integer_number():
            ConvertToBasesExpression().calculate(self.number)
            self.selectAll()

    def exec_convert_to_dms(self):
        if self.store_number():
            DMSExpression().calculate(self.number)

    def exec_convert_to_dd(self):
        dialog = DMStoDD_Dialog()

        number, ok = self.locale.toDouble(self.text())

        if ok:
            is_negative = number < 0
            decimal_deg = abs(number)
            degrees = int(decimal_deg)
            minutes_float = (decimal_deg - degrees) * 60
            minutes = int(minutes_float)
            seconds = (minutes_float - minutes) * 60
            if is_negative:
                degrees = -1 * degrees

            dialog.ui.degreesLineEdit.setText(str(degrees))
            dialog.ui.minutesLineEdit.setText(str(minutes))
            dialog.ui.secondsLineEdit.setText(AppGlobals.to_normal_string(seconds))
            dialog.ui.degreesLineEdit.setFocus()

        dialog.ui.degreesLineEdit.setFocus()
        if not dialog.exec():
            return
        
        degrees, ok = self.locale.toInt(dialog.ui.degreesLineEdit.text())
        minutes, ok  = self.locale.toInt(dialog.ui.minutesLineEdit.text())
        seconds, ok = self.locale.toDouble(dialog.ui.secondsLineEdit.text())
        self.setTextSelect(self.toString(DDExpression().calculate(degrees, minutes, seconds)))

    def exec_from_binary(self):
        dialog = ConvertFromBaseDialog(None, BaseExpression(2))
        dialog.setWindowTitle("Input in Binary format")
        dialog.ui.number_label.setText("&Binary:")
        i_number = 0

        i_number, ok = AppGlobals.to_number(self.text())

        if ok and i_number.is_integer():
            dialog.ui.numberLineEdit.setText(format(int(i_number), 'b'))
        else:
            dialog.ui.numberLineEdit.setText("")
        dialog.ui.numberLineEdit.setFocus()

        if dialog.exec():
            success, str_value = dialog.add_to_log()
            if success:
                self.setTextSelect(str_value)
        self.update_shift_ctrl_status()

    def update_shift_ctrl_status(self):
        mods = QApplication.keyboardModifiers()
        self.current_shift_state = bool(mods & Qt.ShiftModifier)
        self.current_ctrl_state = bool(mods & Qt.ControlModifier)

        # Emit signal only if the shift state has actually changed
        if self.current_shift_state != self._last_shift_state:
            self.shiftStatusChanged.emit(self.current_shift_state)
            self._last_shift_state = self.current_shift_state
            print(f"Shift status changed to: {'Pressed' if self.current_shift_state else 'Released'}")        

        # Emit signal only if the shift state has actually changed
        if self.current_ctrl_state != self._last_ctrl_state:
            self.ctrlStatusChanged.emit(self.current_ctrl_state)
            self._last_ctrl_state = self.current_ctrl_state
            print(f"Ctrl status changed to: {'Pressed' if self.current_ctrl_state else 'Released'}")        

    def exec_from_octal(self):
        dialog = ConvertFromBaseDialog(None, BaseExpression(8))
        dialog.setWindowTitle("Input in Octal format")
        dialog.ui.number_label.setText("&Octal:")
        i_number = 0

        i_number, ok = AppGlobals.to_number(self.text())
                
        if ok and i_number.is_integer():
            dialog.ui.numberLineEdit.setText(format(int(i_number), 'o'))
        else:
            dialog.ui.numberLineEdit.setText("")
        dialog.ui.numberLineEdit.setFocus()

        if dialog.exec():
            success, str_value = dialog.add_to_log()
            if success:
                self.setTextSelect(str_value)
        self.update_shift_ctrl_status()

    def exec_from_decimal(self):
        dialog = ConvertFromBaseDialog(None, BaseExpression(10))
        dialog.setWindowTitle("Input in Decimal format")
        dialog.ui.number_label.setText("&Decimal:")
        i_number = 0

        i_number, ok = AppGlobals.to_number(self.text())
                
        if ok and i_number.is_integer():
            dialog.ui.numberLineEdit.setText(format(int(i_number), 'd'))
        else:
            dialog.ui.numberLineEdit.setText("")
        dialog.ui.numberLineEdit.setFocus()

        if dialog.exec():
            success, str_value = dialog.add_to_log()
            if success:
                self.setTextSelect(str_value)
        self.update_shift_ctrl_status()

    def exec_from_hexadecimal(self):
        dialog = ConvertFromBaseDialog(None, BaseExpression(16))
        dialog.setWindowTitle("Input in Hexadecimal format")
        i_number = 0

        i_number, ok = AppGlobals.to_number(self.text())
                
        if ok and i_number.is_integer():
            dialog.ui.numberLineEdit.setText(f"{int(i_number):X}")
        else:
            dialog.ui.numberLineEdit.setText("")
        dialog.ui.numberLineEdit.setFocus()

        if dialog.exec():
            success, str_value = dialog.add_to_log()
            if success:
                self.setTextSelect(str_value)
        self.update_shift_ctrl_status()

    def exec_sinh(self):
        if self.store_number():
            expr = SinhExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_cosh(self):
        if self.store_number():
            expr = CoshExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_tanh(self):
        if self.store_number():
            expr = TanhExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_arsinh(self):
        if self.store_number():
            expr = ArsinhExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_arcosh(self):
        if self.store_number():
            expr = ArcoshExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_artanh(self):
        if self.store_number():
            expr = ArtanhExpression()
            AppGlobals.number_to_input_box(expr.calculate(AppGlobals.get_number()))

    def exec_rectangular_to_polar(self):
        dialog = RectangularToPolarDialog()
        x, ok = self.locale.toDouble(self.text())
        if ok:
            dialog.ui.xLineEdit.setText(self.text())

        dialog.ui.xLineEdit.setFocus()

        if dialog.exec():
            x, ok = self.locale.toDouble(dialog.ui.xLineEdit.text())
            y, ok = self.locale.toDouble(dialog.ui.yLineEdit.text())
            expr = RectangularToPolarExpression(x)
            self.setTextSelect(AppGlobals.to_normal_string(expr.calculate(y)))
            self.update_shift_ctrl_status()

        self.update_shift_ctrl_status()
    
    def exec_polar_to_rectangular(self):
        dialog = PolarToRectangularDialog()
        r, ok = self.locale.toDouble(self.text())
        if ok:
            dialog.ui.radiusLineEdit.setText(self.text())

        dialog.ui.radiusLineEdit.setFocus()

        if dialog.exec():
            r, ok = self.locale.toDouble(dialog.ui.radiusLineEdit.text())
            a, ok = self.locale.toDouble(dialog.ui.angleLineEdit.text())
            expr = PolarToRectangularExpression(r)
            self.setTextSelect(AppGlobals.to_normal_string(expr.calculate(a)))
            self.update_shift_ctrl_status()

        self.update_shift_ctrl_status()

    def exec_combination(self):
        dialog = CombinationDialog()
        n, n_valid = self.locale.toInt(self.text())
        if n_valid:
            dialog.ui.nLineEdit.setText(str(n))

        dialog.ui.nLineEdit.setFocus()

        if dialog.exec():
            expr = CombinationExpression(int(dialog.ui.nLineEdit.text()))
            result = float(expr.calculate(int(dialog.ui.rLineEdit.text())))
            self.setTextSelect(AppGlobals.to_normal_string(result))
        self.update_shift_ctrl_status()

    def exec_permutation(self):
        dialog = CombinationDialog()
        dialog.setWindowTitle("Permutation nPr")
        n, n_valid = self.locale.toInt(self.text())
        if n_valid:
            dialog.ui.nLineEdit.setText(str(n))

        dialog.ui.nLineEdit.setFocus()

        if dialog.exec():
            expr = PermutationExpression(int(dialog.ui.nLineEdit.text()))
            result = float(expr.calculate(int(dialog.ui.rLineEdit.text())))
            self.setTextSelect(AppGlobals.to_normal_string(result))

        self.update_shift_ctrl_status()

    def exec_ratio_c(self):
        dialog = RatioCDialog()
        dialog.ui.aLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.ratio_c_a))
        dialog.ui.bLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.ratio_c_b))
        dialog.ui.dLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.ratio_c_d))

        dialog.ui.aLineEdit.setFocus()

        if dialog.exec():
            AppGlobals.ratio_c_a, ok = self.locale.toDouble(dialog.ui.aLineEdit.text())
            AppGlobals.ratio_c_b, ok = self.locale.toDouble(dialog.ui.bLineEdit.text())
            AppGlobals.ratio_c_d, ok = self.locale.toDouble(dialog.ui.dLineEdit.text())
            expr = RatioCExpression()
            result = float(expr.calculate())
            self.setTextSelect(AppGlobals.to_normal_string(result))

        self.update_shift_ctrl_status()

    def exec_ratio_d(self):
        dialog = RatioDDialog()
        dialog.ui.aLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.ratio_d_a))
        dialog.ui.bLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.ratio_d_b))
        dialog.ui.cLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.ratio_d_c))

        dialog.ui.aLineEdit.setFocus()

        if dialog.exec():
            AppGlobals.ratio_d_a, ok = self.locale.toDouble(dialog.ui.aLineEdit.text())
            AppGlobals.ratio_d_b, ok = self.locale.toDouble(dialog.ui.bLineEdit.text())
            AppGlobals.ratio_d_c, ok = self.locale.toDouble(dialog.ui.cLineEdit.text())
            expr = RatioDExpression()
            result = float(expr.calculate())
            self.setTextSelect(AppGlobals.to_normal_string(result))

        self.update_shift_ctrl_status()

    def handle_paste(self):
        modified_text = QGuiApplication.clipboard().text()

        if AppGlobals.paste_from_clipboard_replace:
            modified_text = modified_text.replace(',', '.')

        # Keep only allowed characters +-.,0123456789eE
        modified_text = re.sub(r'[^+\-\.,0-9eE]', '', modified_text)
        self.insert(modified_text)

    def handle_cut(self):
        selected_text = self.selectedText()
        if not selected_text:
            return

        if AppGlobals.copy_to_clipboard_replace:
            modified = selected_text.replace('.', ',')
            QGuiApplication.clipboard().setText(modified)

            # markierten Text entfernen (Cut)
            self.del_()
        else:
            self.cut()

    def handle_copy(self):
        if AppGlobals.copy_to_clipboard_replace:
            selected_text = self.selectedText()
            modified = selected_text.replace('.', ',')
            QGuiApplication.clipboard().setText(modified)            
        else:
            self.copy()

    def exec_numeric_format(self):
        dialog = NumFormatDialog()

        match AppGlobals.numeric_format:
            case NumericFormat.normal:
                dialog.ui.normRadioButton.setChecked(True)
            case NumericFormat.fixed:
                dialog.ui.fixRadioButton.setChecked(True)
            case NumericFormat.scientific:
                dialog.ui.sciRadioButton.setChecked(True)
            case NumericFormat.engineering:
                dialog.ui.engRadioButton.setChecked(True)
            case _:
                dialog.ui.generalRadioButton.setChecked(True)

        dialog.ui.precisionSpinBox.setValue(AppGlobals.numeric_precision)

        if dialog.exec() != True:
            self.update_shift_ctrl_status()
            return
        
        AppGlobals.numeric_precision = dialog.ui.precisionSpinBox.value()
        if dialog.ui.generalRadioButton.isChecked():
            AppGlobals.numeric_format = NumericFormat.general
        elif dialog.ui.fixRadioButton.isChecked():
            AppGlobals.numeric_format = NumericFormat.fixed
        elif dialog.ui.sciRadioButton.isChecked():
            AppGlobals.numeric_format = NumericFormat.scientific
        elif dialog.ui.engRadioButton.isChecked():
            AppGlobals.numeric_format = NumericFormat.engineering
        else:
            AppGlobals.numeric_format = NumericFormat.normal

        self.statusbar_changed.emit()
        self.update_shift_ctrl_status()

    def exec_toggle_table(self):
        if self.hasFocus():
            AppGlobals.history.setFocus()
        else:
            QTimer.singleShot(0, self.setFocus)
            QTimer.singleShot(0, self.selectAll)

    def exec_round(self):
        if self.store_number():
            self.setTextSelect(AppGlobals.to_format_string(self.number))

    def exec_random(self):
        f = random.random()
        AppGlobals.history.append("")  # Ensure a new line before the header
        StringCellValue("Random: ")
        ResultCellValue(f)
        self.setTextSelect(AppGlobals.to_normal_string(f))

    def exec_date_time_stamp(self):
        """Inserts a formatted date and time header line into the QTextBrowser history."""
        date_str = QLocale().toString(QDate.currentDate(), QLocale.ShortFormat)
        day_name = QLocale().toString(QDate.currentDate(), "dddd")
        time_str = QLocale().toString(QTime.currentTime(), QLocale.ShortFormat)
        cw, _ = QDate.currentDate().weekNumber()

        # Combine all parts with tab or space spacing
        header_text = (
            f"{date_str} - {day_name} - {time_str} - CW {cw}"
        )

        # Insert a line break before the header if needed, then append the string cell
        AppGlobals.history.append("")  # Ensure a new line before the header
        StringCellValue(header_text, is_bold=True)

        # Ensure view scrolls to bottom
        AppGlobals.history.ensureCursorVisible()

    def exec_phy_const(self):
        dlg = PhyConstDialog(AppGlobals.phy_const_index)
        if dlg.exec() == QDialog.Accepted:
            const, AppGlobals.phy_const_index = dlg.get_selection_by_index()
            self.setTextSelect(AppGlobals.to_normal_string(const['value']))
        self.update_shift_ctrl_status()

    def exec_unit_conversion(self):
        self.number, ok = self.locale.toDouble(self.text())
        f: float = 1.0
        if ok:
            f = self.number
        dlg = ConversionDialog(initial_value=f, initial_unit=AppGlobals.unit_conversion_from, result_unit=AppGlobals.unit_conversion_to)
        if dlg.exec() == QDialog.Accepted:
            v_from, AppGlobals.unit_conversion_from, v_to, AppGlobals.unit_conversion_to = dlg.get_results()
            self.setTextSelect(AppGlobals.to_normal_string(v_to))
            AppGlobals.history.append("")  # Ensure a new line before the header
            FloatCellValue(v_from)
            StringCellValue(f" {AppGlobals.unit_conversion_from} = ")
            ResultCellValue(v_to)
            StringCellValue(f" {AppGlobals.unit_conversion_to}")
        self.update_shift_ctrl_status()

    def exec_del_operation(self):
        if self.last_expression():
            if self.last_expression().prev_expression:
                self.last_expression().prev_expression.next_expression = None
            else:
                AppGlobals.root_expression = None
            self.update_expression_label()

    def exec_linear_func_two_points(self):
        dialog = LinearTwoPointsDialog()

        if dialog.exec():
            AppGlobals.linear_x0, ok = self.locale.toDouble(dialog.ui.x0LineEdit.text())
            AppGlobals.linear_y0, ok = self.locale.toDouble(dialog.ui.y0LineEdit.text())
            AppGlobals.linear_x1, ok = self.locale.toDouble(dialog.ui.x1LineEdit.text())
            AppGlobals.linear_y1, ok = self.locale.toDouble(dialog.ui.y1LineEdit.text())

            expr = LinearTwoPointsExpression()
            result = float(expr.calculate())
            self.setTextSelect(AppGlobals.to_normal_string(result))

        self.update_shift_ctrl_status()

    def exec_calculate_y_from_linear_func(self):
        dialog = LinearYfromXDialog()
        number, ok = AppGlobals.toDouble(self.text())
        if ok:
            dialog.ui.xLineEdit.setText(self.text())

        if dialog.exec():
            AppGlobals.linear_a, ok = self.locale.toDouble(dialog.ui.aLineEdit.text())
            AppGlobals.linear_b, ok = self.locale.toDouble(dialog.ui.bLineEdit.text())
            x, ok = self.locale.toDouble(dialog.ui.xLineEdit.text())

            expr = LinearYfromXExpression()
            result = float(expr.calculate(x))
            self.setTextSelect(AppGlobals.to_normal_string(result))

        self.update_shift_ctrl_status()

    def exec_quadratic_equation(self):
        dialog = QuadraticEquationDialog()

        if dialog.exec():
            AppGlobals.quadratic_a, ok = AppGlobals.toDouble(dialog.ui.aLineEdit.text())
            AppGlobals.quadratic_b, ok = AppGlobals.toDouble(dialog.ui.bLineEdit.text())
            AppGlobals.quadratic_c, ok = AppGlobals.toDouble(dialog.ui.cLineEdit.text())

            expr = QuadraticEquationExpression()
            self.setTextSelect(AppGlobals.to_normal_string(expr.calculate()))

        self.update_shift_ctrl_status()

    def exec_linear_system_two_equations(self):
        dialog = LinearSystemDialog()

        if dialog.exec():
            AppGlobals.lse_a1, ok = AppGlobals.toDouble(dialog.ui.a1LineEdit.text())
            AppGlobals.lse_b1, ok = AppGlobals.toDouble(dialog.ui.b1LineEdit.text())
            AppGlobals.lse_c1, ok = AppGlobals.toDouble(dialog.ui.c1LineEdit.text())
            AppGlobals.lse_a2, ok = AppGlobals.toDouble(dialog.ui.a2LineEdit.text())
            AppGlobals.lse_b2, ok = AppGlobals.toDouble(dialog.ui.b2LineEdit.text())
            AppGlobals.lse_c2, ok = AppGlobals.toDouble(dialog.ui.c2LineEdit.text())

            expr = LinearSystemExpression()
            self.setTextSelect(AppGlobals.to_normal_string(expr.calculate()))

        self.update_shift_ctrl_status()

    def exec_log_base(self):
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            if AppGlobals.input_box.store_number() and AppGlobals.input_imag_box.store_number():
                self.create_expression_node(LogBaseExpression(AppGlobals.get_complex_number()))
        else:
            if self.store_number():
                self.create_expression_node(LogBaseExpression(self.number))

    def exec_awg_to_mm2(self):
        dialog = AwgToMm2Dialog()

        number, ok = AppGlobals.toDouble(self.text())
        if ok:
            dialog.ui.awgLineEdit.setText(self.text())

        if dialog.exec():
            awg, ok = AppGlobals.toDouble(dialog.ui.awgLineEdit.text())

            expr = AwgToMm2Expression()
            self.setTextSelect(AppGlobals.to_normal_string(expr.calculate(awg)))

        self.update_shift_ctrl_status()

    def exec_mm2_to_awg(self):
        dialog = Mm2ToAwgDialog()

        number, ok = AppGlobals.toDouble(self.text())
        if ok:
            dialog.ui.areaMm2LineEdit.setText(self.text())

        if dialog.exec():
            mm2, ok = AppGlobals.toDouble(dialog.ui.areaMm2LineEdit.text())

            expr = Mm2ToAwgExpression()
            self.setTextSelect(AppGlobals.to_normal_string(expr.calculate(mm2)))

        self.update_shift_ctrl_status()

    def event(self, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab:
            print("TAB key intercepted")

            if AppGlobals.calc_mode is CalcMode.complex_numbers:
                if self == AppGlobals.input_box:
                    if AppGlobals.input_imag_box:
                        AppGlobals.input_imag_box.setFocus()
                        AppGlobals.input_imag_box.selectAll()
                elif self == AppGlobals.input_imag_box:
                    self.exec_toggle_table()
            else:
                self.exec_toggle_table()
            return True  # Event handled
        return super().event(event)
    
    def exec_frac_part(self):
        if self.store_number():
            expr = FracPartExpression()
            self.setTextSelect(AppGlobals.to_normal_string(expr.calculate(self.number)))

    def exec_int_part(self):
        if self.store_number():
            expr = IntPartExpression()
            self.setTextSelect(AppGlobals.to_normal_string(expr.calculate(self.number)))

    def get_physical_shift_state(self):
        if self.current_shift_state:
            return True
        
        # Check if Shift is supressed by os
        if self.scan_code == 72 and self.key == Qt.Key_Up:
            return True
        if self.scan_code == 80 and self.key == Qt.Key_Down:
            return True
        if self.scan_code == 75 and self.key == Qt.Key_Left:
            return True
        if self.scan_code == 77 and self.key == Qt.Key_Right:
            return True
        if self.scan_code == 71 and self.key == Qt.Key_Home:
            return True
        if self.scan_code == 79 and self.key == Qt.Key_End:
            return True
        if self.scan_code == 73 and self.key == Qt.Key_PageUp:
            return True
        if self.scan_code == 81 and self.key == Qt.Key_PageDown:
            return True
        if self.scan_code == 82 and self.key == Qt.Key_Insert:
            return True
        if self.scan_code == 83 and self.key == Qt.Key_Delete:
            return True
        if self.scan_code == 76 and self.key == Qt.Key_Clear:
            return True
        else:
            return False

    def exec_word_size_byte(self):
        AppGlobals.current_word_size = WordSize.BIT8

    def exec_word_size_word(self):
        AppGlobals.current_word_size = WordSize.BIT16

    def exec_word_size_dword(self):
        AppGlobals.current_word_size = WordSize.BIT32

    def exec_word_size_qword(self):
        AppGlobals.current_word_size = WordSize.BIT64

    def set_base(self, base: NumberBase):
        if AppGlobals.calc_mode != CalcMode.base_n:
            self.exec_base_n_mode()
        number, ok = AppGlobals.to_number(self.text())
        AppGlobals.number_base = base
        self.update_bg_color()
        self.update_keyboard()

        if ok:
            self.setTextSelect(AppGlobals.to_normal_string(number))

    def exec_scientific_mode(self):
        number, ok = AppGlobals.to_number(self.text())
        AppGlobals.calc_mode = CalcMode.scientific
        self.update_bg_color()
        self.update_keyboard()

        if ok:
            self.setTextSelect(AppGlobals.to_normal_string(number))

    def exec_base_n_mode(self):
        number, ok = AppGlobals.to_number(self.text())
        AppGlobals.calc_mode = CalcMode.base_n
        self.update_bg_color()
        self.update_keyboard()

        if ok:
            self.setTextSelect(AppGlobals.to_normal_string(number))

    def exec_bitwise_shift_arithmetic(self):
        AppGlobals.bitwise_shift = ShiftRotateOperation.arithmetic

    def exec_bitwise_shift_logical(self):
        AppGlobals.bitwise_shift = ShiftRotateOperation.logical

    def exec_bitwise_shift_circular(self):
        AppGlobals.bitwise_shift = ShiftRotateOperation.circular

    def exec_bitwise_shift_circular_carry(self):
        AppGlobals.bitwise_shift = ShiftRotateOperation.circular_carry_bit

    def exec_left_shift(self):
        if self.store_number():
            match AppGlobals.bitwise_shift:
                case ShiftRotateOperation.circular:
                    expr = LeftShiftCircularExpression()
                    self.setTextSelect(self.toString(expr.calculate(self.number)))
                case  ShiftRotateOperation.circular_carry_bit:
                    expr = LeftShiftRotateCarryExpression()
                    self.setTextSelect(self.toString(expr.calculate(self.number)))
                case ShiftRotateOperation.arithmetic:
                    if self.store_number():
                        self.create_expression_node(LeftShiftArithmeticExpression(self.number))
                case _:
                    if self.store_number():
                        self.create_expression_node(LeftShiftLogicalExpression(self.number))

    def exec_right_shift(self):
        if self.store_number():
            match AppGlobals.bitwise_shift:
                case ShiftRotateOperation.circular:
                    expr = RightShiftCircularExpression()
                    self.setTextSelect(self.toString(expr.calculate(self.number)))
                case  ShiftRotateOperation.circular_carry_bit:
                    expr = RightShiftRotateCarryExpression()
                    self.setTextSelect(self.toString(expr.calculate(self.number)))
                case ShiftRotateOperation.arithmetic:
                    if self.store_number():
                        self.create_expression_node(RightShiftArithmeticExpression(self.number))
                case _:
                    if self.store_number():
                        self.create_expression_node(RightShiftLogicalExpression(self.number))

    def exec_toggle_carry_flag(self):
        if AppGlobals.carry_flag == 0:
            AppGlobals.carry_flag = 1
        else:
            AppGlobals.carry_flag = 0

    def exec_toggle_base_n_sign(self):
        AppGlobals.base_n_signed = not AppGlobals.base_n_signed

    def update_keyboard(self):
        self.keyboard_changed.emit()

    def exec_complex_numbers_mode(self):
        number, ok = AppGlobals.to_number(AppGlobals.input_box.text())
        AppGlobals.calc_mode = CalcMode.complex_numbers
        AppGlobals.input_box.update_bg_color()
        AppGlobals.input_imag_box.update_bg_color()
        self.update_keyboard()

        if ok:
            AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(number))

    def exec_rectangular_form_complex_number(self):
        if AppGlobals.complex_number_form == ComplexNumberForm.rectangular:
            self.statusbar_message.emit("Already Rectrangular Form")
            return
        
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            if AppGlobals.input_box.store_number() and AppGlobals.input_imag_box.store_number():
                z = cmath.rect(AppGlobals.real_part(), AppGlobals.angle_unit.to_rad(AppGlobals.imag_part()))
                AppGlobals.input_box.setTextSelect(AppGlobals.input_box.toString(z.real))
                AppGlobals.input_imag_box.setText(AppGlobals.input_box.toString(z.imag))
        AppGlobals.complex_number_form = ComplexNumberForm.rectangular
        AppGlobals.real_part_focus()

    def exec_polar_form_complex_number(self):
        if AppGlobals.complex_number_form == ComplexNumberForm.polar:
            self.statusbar_message.emit("Already Polar Form")
            return
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            if AppGlobals.input_box.store_number() and AppGlobals.input_imag_box.store_number():
                z = complex(complex(AppGlobals.real_part(), AppGlobals.imag_part()))
                r, phi_rad = cmath.polar(z)
                AppGlobals.input_box.setTextSelect(AppGlobals.input_box.toString(r))
                AppGlobals.input_imag_box.setText(AppGlobals.input_box.toString(AppGlobals.angle_unit.from_rad(phi_rad)))
        AppGlobals.complex_number_form = ComplexNumberForm.polar
        AppGlobals.real_part_focus()

    def exec_input_complex_number_in_rectangular_form(self):
        if AppGlobals.calc_mode is not CalcMode.complex_numbers:
            self.statusbar_message.emit("Change to Complex Numbers Mode")
            return

        if AppGlobals.complex_number_form is ComplexNumberForm.rectangular:
            self.statusbar_message.emit("Complex Number Form is already Rectangular")
            return
        
        dialog = InputRectangularForm()

        r, ok = AppGlobals.toDouble(AppGlobals.input_box.text())
        theta, theta_ok = AppGlobals.toDouble(AppGlobals.input_imag_box.text())

        if ok and theta_ok:
            z = cmath.rect(r, AppGlobals.angle_unit.to_rad(theta))
            dialog.ui.realPartLineEdit.setText(AppGlobals.to_normal_string(z.real))
            dialog.ui.imagPartLineEdit.setText(AppGlobals.to_normal_string(z.imag))

        if dialog.exec():
            real_part, real_part_ok = AppGlobals.toDouble(dialog.ui.realPartLineEdit.text())
            imag_part, imag_part_ok = AppGlobals.toDouble(dialog.ui.imagPartLineEdit.text())
            z = complex(real_part, imag_part)

            if real_part_ok and imag_part_ok:
                r, theta = cmath.polar(z)
                AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(r))
                AppGlobals.input_imag_box.setText(AppGlobals.to_normal_string(AppGlobals.angle_unit.from_rad(theta)))
                self.button_clicked(CalcOperations.complex_rect_polar_history)

        AppGlobals.input_box.setFocus()
        AppGlobals.input_box.selectAll()
        self.update_shift_ctrl_status()

    def exec_input_complex_number_in_polar_form(self):
        if AppGlobals.calc_mode is not CalcMode.complex_numbers:
            self.statusbar_message.emit("Change to Complex Numbers Mode")
            return

        if AppGlobals.complex_number_form is ComplexNumberForm.polar:
            self.statusbar_message.emit("Complex Number Form is already Polar")
            return
        
        dialog = InputPolarForm()

        real_part, real_ok = AppGlobals.toDouble(AppGlobals.input_box.text())
        imag_part, imag_ok = AppGlobals.toDouble(AppGlobals.input_imag_box.text())

        if real_ok and imag_ok:
            z = complex(real_part, imag_part)
            r, theta = cmath.polar(z)
            dialog.ui.rLineEdit.setText(AppGlobals.to_normal_string(r))
            dialog.ui.thetaLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.angle_unit.from_rad(theta)))

        if dialog.exec():
            r, r_ok = AppGlobals.toDouble(dialog.ui.rLineEdit.text())
            theta, theta_ok = AppGlobals.toDouble(dialog.ui.thetaLineEdit.text())
            z = complex(real_part, imag_part)

            if r_ok and theta_ok:
                z = cmath.rect(r, AppGlobals.angle_unit.to_rad(theta))
                AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(z.real))
                AppGlobals.input_imag_box.setText(AppGlobals.to_normal_string(z.imag))
                self.button_clicked(CalcOperations.complex_rect_polar_history)

        AppGlobals.input_box.setFocus()
        AppGlobals.input_box.selectAll()
        self.update_shift_ctrl_status()

    def update_bg_color(self):
        if AppGlobals.calc_mode == CalcMode.base_n:
            """Updates the background color based on the selected NumberBase enum value."""
            bg_color = AppGlobals.BASE_COLORS.get(AppGlobals.number_base, "#FFFFFF")
        else:
            bg_color = "#FFFFFF"
        
        # Update stylesheet while maintaining dark text contrast
        self.setStyleSheet(f"""
            QLineEdit {{
                background-color: {bg_color};
                color: #000000;
                border: 1px solid #717171;
                padding: 4px;
            }}
        """)

    def exec_double_shift(self):
        # Action to execute when double-Shift is detected
        print("Double-Shift detected!")

        if AppGlobals.shift_hold:
            AppGlobals.shift_hold = False
        else:
            AppGlobals.shift_hold = True

        AppGlobals.ctrl_hold = False
        AppGlobals.ctrl_shift_hold = False

        self.shiftHold.emit()

    def exec_double_ctrl(self):
        # Action triggered on Double-Ctrl
        print("Detected: Double-Ctrl")

        if AppGlobals.ctrl_hold:
            AppGlobals.ctrl_hold = False
        else:
            AppGlobals.ctrl_hold = True
        AppGlobals.shift_hold = False
        AppGlobals.ctrl_shift_hold = False
        self.shiftHold.emit()

    def exec_ctrl_double_shift(self):
        # Action triggered on Ctrl + Double-Shift
        print("Detected: Ctrl + Double-Shift")
        if AppGlobals.ctrl_shift_hold:
            AppGlobals.ctrl_shift_hold = False
        else:
            AppGlobals.ctrl_shift_hold = True
        AppGlobals.shift_hold = False
        AppGlobals.ctrl_hold = False
        self.shiftHold.emit()

    def reset_hold_flags(self):
        if AppGlobals.shift_hold or AppGlobals.ctrl_hold or AppGlobals.ctrl_shift_hold:
            AppGlobals.shift_hold = False
            AppGlobals.ctrl_hold = False
            AppGlobals.ctrl_shift_hold = False
            self.shiftHold.emit()

    def on_double_ctrl_shift(self):
        # Action triggered on Double (Ctrl + Shift)
        print("Detected: Double (Ctrl + Shift)")
        self.exec_ctrl_double_shift()

    def history_link_clicked(self, url: QUrl):
        """Extracts full precision value from link URL and puts it into the input field."""
        raw_url = url.toString()
        if raw_url.startswith("calc:"):
            # Extract full precision string value
            raw_value = raw_url.split("calc:")[1]
        else:
            raw_value = raw_url

        convert_ok = False
        try:
            number_temp = int(raw_value, 10) # Try to convert to int first
            convert_ok = True
        except ValueError:
            pass  # Not an integer, try float next

        if convert_ok:
            # integer
            if AppGlobals.is_shift_pressed() and AppGlobals.calc_mode is CalcMode.complex_numbers:
                AppGlobals.input_imag_box.setTextSelect(AppGlobals.to_normal_string(number_temp))
            else:
                AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(number_temp))
        else:
            number_temp, convert_ok = AppGlobals.toDouble(raw_value) # Try to convert to float
            if AppGlobals.is_shift_pressed() and AppGlobals.calc_mode is CalcMode.complex_numbers:
                AppGlobals.input_imag_box.setTextSelect(AppGlobals.to_normal_string(number_temp))
            else:
                AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(number_temp))

        if not convert_ok:
            if AppGlobals.is_shift_pressed() and AppGlobals.calc_mode is CalcMode.complex_numbers:
                AppGlobals.input_imag_box.setTextSelect(raw_value)  # Fallback: just set the raw string
            else:
                AppGlobals.input_box.setTextSelect(raw_value)  # Fallback: just set the raw string

        if AppGlobals.is_shift_pressed() and AppGlobals.calc_mode is CalcMode.complex_numbers:
            AppGlobals.input_imag_box.setFocus()
        else:
            AppGlobals.input_box.setFocus()

    def selectAll(self):
        super().selectAll()
        if self == AppGlobals.input_box:
            AppGlobals.input_imag_box.deselect()
        else:
            AppGlobals.input_box.deselect()
        
    def setFocus(self):
        super().setFocus()
