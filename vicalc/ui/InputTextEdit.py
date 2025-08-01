from PySide6.QtWidgets import QApplication, QLineEdit, QStyleOptionFrame
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtGui import QFont
from PySide6.QtGui import QKeyEvent, QFocusEvent 
from PySide6.QtCore import QLocale
from ..CalcOperations import CalcOperations
import math
import locale
import ctypes
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
from ..ConvertToBasesExpression import ConvertToBasesExpression
from ..BaseExpression import BaseExpression
from ..AppGlobals import AppGlobals
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

class InputTextEdit(QLineEdit):
    # Define a custom signal that carries a boolean indicating if Shift is pressed
    shiftStatusChanged = Signal(bool)
    ctrlStatusChanged = Signal(bool)
    memory_changed = Signal(str)
    focusOut = Signal()
    focusIn = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.number: float = None  # Holds the parsed number
        self._memory: float = 0
        self._trig_mode = TrigMode.DEG
        AppGlobals.angle_unit = DegUnitProtocol()
        self.expressionLabel = None
        self.key = None
        self.modifiers = None
        self.scan_code = None
        self.resultFont = QFont()
        self.resultFont.setBold(True)
        self._last_shift_state = False # Keep track of the last shift state
        self._last_ctrl_state = False # Keep track of the last ctrl state
        self.current_shift_state = False
        self.current_ctrl_state = False
        # Define a list to store CalcButton objects
        self.button_list = []
        self.root_expression = None
        self.locale = QLocale()

    def keyPressEvent(self, event):
        self.key = event.key()
        self.modifiers = event.modifiers()
        self.scan_code = event.nativeScanCode()

        # Check current Shift state
        self.current_shift_state = bool(self.modifiers & Qt.ShiftModifier)
        self.current_ctrl_state = bool(self.modifiers & Qt.ControlModifier)

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

        self.handle_keys_check_errors(event)

        # 📚 Character (text)
        # The 'text()' method returns the Unicode text of the key.
        # This is the actual character generated by the key press, considering modifiers.
        char_pressed = event.text()

        # 🏷️ Name (text representation of the key)
        # For non-character keys (like F1, Enter, Shift), 'text()' might be empty.
        # 'key()' returns a Qt.Key constant, which can be converted to a string.
        key_name = Qt.Key(event.key()).name

        # 💻 Virtual Key Code
        # 'key()' returns the virtual key code (Qt.Key constant)
        # This is a platform-independent code representing the key.
        virtual_key_code = event.key()

        # ⌨️ Scan Code
        # 'nativeScanCode()' returns the hardware-dependent scan code.
        # This is specific to the keyboard hardware and operating system.

        output = f"Key Pressed: '{char_pressed}' ---------------------\n" \
                 f"Key Name (Qt.Key constant): {key_name}\n" \
                 f"Virtual Key Code (int): {virtual_key_code}\n" \
                 f"Scan Code (Native): {self.scan_code}"
        
        print(output)

    # You also need to override keyReleaseEvent to detect when Shift is released
    def keyReleaseEvent(self, event):
        self.modifiers = event.modifiers()
        self.current_shift_state = bool(self.modifiers & Qt.ShiftModifier)
        self.current_ctrl_state = bool(self.modifiers & Qt.ControlModifier)

        if self.current_shift_state != self._last_shift_state:
            self.shiftStatusChanged.emit(self.current_shift_state)
            self._last_shift_state = self.current_shift_state
            print(f"Shift status changed to: {'Pressed' if self.current_shift_state else 'Released'}")

        if self.current_ctrl_state != self._last_ctrl_state:
            self.ctrlStatusChanged.emit(self.current_ctrl_state)
            self._last_ctrl_state = self.current_ctrl_state
            print(f"Ctrl status changed to: {'Pressed' if self.current_ctrl_state else 'Released'}")

        super().keyReleaseEvent(event)                

    def store_number(self):
        result = False
        try:
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

    def _show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def toString(self, number):
        return AppGlobals.to_normal_string(number)
    
    def memory_to_string(self):
        return self.toString(self.memory)

    def memory_to_format_string(self):
        return AppGlobals.to_format_string(self.memory)

    def toDouble(self, text):
        return self.locale.toDouble(text)
    
    def exec_factorial(self):
        try:
            i = int(self.text())
            f = FactorialExpression(AppGlobals.table).calculate(float(i))
            self.setText(str(f))
            self.selectAll()
        except ValueError:
            self._show_error("Invalid input: nonnegative integer expected.")

    def unary_operation(self, event):
        if self.current_shift_state:
            return self.shift_unary_operation(event)
        elif (self.current_ctrl_state):
            return self.ctrl_unary_operation(event)
        else:
            return self.normal_unary_operation(event)

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
        self.root_expression = None
        self.update_expression_label()
        self.selectAll()

    def create_expression_node(self, expression):
        if self.root_expression == None:
            self.root_expression = expression
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
                    # prio of expression prio is lower or equal of last expression
                    # calculate last expression and change this last expression with expression
                    expression.first_number = last_expression_temp.calculate(self.number)
                    expression.prev_expression = last_expression_temp.prev_expression
                    expression.next_expression = last_expression_temp.next_expression

                    if last_expression_temp == self.root_expression:
                        self.root_expression = expression
                    else:
                        last_expression_temp.prev_expression.next_expression = expression
                    self.update_expression_label()

    def update_expression_label(self):
        s = ""
        currect_expression = self.root_expression
        while currect_expression != None:
            s += currect_expression.text()
            currect_expression = currect_expression.next_expression
        self.expressionLabel.setText(s)
        self.selectAll()

    def setTextSelect(self, text):
        self.setText(text)
        self.selectAll()

    def exec_addition(self):
        if self.store_number():
            self.create_expression_node(AdditionExpression(self.number, AppGlobals.table))

    def exec_pow(self):
        if self.store_number():
            self.create_expression_node(PowExpression(self.number, AppGlobals.table))

    def exec_opening_bracket(self):
        self.create_expression_node(BracketExpression(AppGlobals.table))

    def exec_subtraction(self):
        if self.store_number():
            self.create_expression_node(SubtractionExpression(self.number, AppGlobals.table))

    def exec_multiplication(self):
        if self.store_number():
            self.create_expression_node(MultiplicationExpression(self.number, AppGlobals.table))

    def exec_division(self):
        if self.store_number():
            self.create_expression_node(DivisionExpression(self.number, AppGlobals.table))

    def execute(self):
        if (self.root_expression == None):
            # it is just a text without expression in textedit, put it in tablewidget, e. g. to notice
            row = AppGlobals.table.rowCount()
            AppGlobals.table.insertRow(row)        
            AppGlobals.table.scrollToBottom()
            self.selectAll()

            self.number, ok = self.locale.toDouble(self.text())
            if ok:
                ResultCellValue(self.number, row, 0)

        elif self.store_number():
            # go to last expression

            current_expression = self.last_expression()
            last_number = self.number

            while current_expression != None:
                last_number = current_expression.calculate(last_number)
                current_expression = current_expression.prev_expression

            if (self.root_expression != None):
                self.setTextSelect(self.toString(last_number))
                self.root_expression = None
                self.update_expression_label()

    def exec_percent(self):
        if self.store_number():
            if self.last_expression() != None:
                percent = PercentExpression(AppGlobals.table, self.last_expression())
                self.setTextSelect(self.toString(percent.calculate(self.number)))
                # remove node, because it is calculated
                if (self.last_expression().prev_expression != None):
                    self.last_expression().prev_expression.next_expression = None
                else:
                    self.root_expression = None
                self.update_expression_label()

    def exec_closing_bracket(self):
        if self.store_number():
            current_expression = self.last_expression()
            last_number = self.number

            while current_expression != None:
                if isinstance(current_expression, BracketExpression):
                    break
                last_number = current_expression.calculate(last_number)
                current_expression = current_expression.prev_expression

            # bracket expression is no longer required, exclude it from chain
            if current_expression == None:
                self.root_expression = None
            else:
                current_expression = current_expression.prev_expression
                if current_expression == None:
                    self.root_expression = None
                else:
                    current_expression.next_expression = None

            self.setTextSelect(self.toString(last_number))
            self.update_expression_label()

    def exec_pi(self):
        self.setText(self.toString(math.pi))
        self.selectAll()

    def last_expression(self):
        current_expression = None
        if self.root_expression != None:
            current_expression = self.root_expression
            while current_expression.next_expression != None:
                current_expression = current_expression.next_expression
        return current_expression

    def button_clicked(self, calc_operation):
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
                case CalcOperations.ten_power_10:
                    self.exec_ten_power_x()
                case CalcOperations.factorial:
                    self.exec_factorial()
                case CalcOperations.pi:
                    self.exec_pi()
                case CalcOperations.comma:
                    self.exec_comma()
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
                case CalcOperations.MS:
                    self.exec_MS()
                case CalcOperations.MR:
                    self.exec_MR()
                case CalcOperations.M_plus:
                    self.exec_M_plus()
                case CalcOperations.M_minus:
                    self.exec_M_minus()
                case CalcOperations.m_multiply:
                    self.exec_m_multiply()
                case CalcOperations.m_division:
                    self.exec_m_division()
                case CalcOperations.Multiply:
                    self.exec_multiplication()
                case CalcOperations.opening_bracket:
                    self.exec_opening_bracket()
                case CalcOperations.closing_bracket:
                    self.exec_closing_bracket()
                case CalcOperations.Division:
                    self.exec_division()
                case CalcOperations.reciprocal:
                    self.exec_reciprocal()
                case CalcOperations.SignChange:
                    self.exec_sign_change()
                case CalcOperations.exponent:
                    self.exec_exponent()
                case CalcOperations.del_last_line:
                    self.exec_del_last_line()
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
                case _:
                    QMessageBox.information(self, "Information", "No operation configured")
        except Exception as e:
            self._show_error(f"{str(e)}")
        self.setFocus()

    def exec_comma(self):
        # Get the current OS locale (LC_ALL affects all categories like number, date, etc.)
        locale.setlocale(locale.LC_ALL, '')  # '' = use environment / OS default

        # Get locale conventions (number formatting, currency, etc.)
        conv = locale.localeconv()

        # Extract separators
        decimal_sep = conv['decimal_point']

        self.insert(decimal_sep)

        """
        # Example: Simulating individual key presses
        QApplication.instance().postEvent(self, QKeyEvent(
            QKeyEvent.Type.KeyPress, Qt.Key.Key_Comma, Qt.KeyboardModifier.NoModifier, decimal_sep
        ))
        QApplication.instance().postEvent(self, QKeyEvent(
            QKeyEvent.Type.KeyRelease, Qt.Key.Key_Comma, Qt.KeyboardModifier.NoModifier, decimal_sep
        ))
        """

    def focusInEvent(self, event: QFocusEvent):
        self.focusOut.emit()
        super().focusInEvent(event) # Call the base class implementation

    def focusOutEvent(self, event: QFocusEvent):
        self.focusOut.emit()
        super().focusOutEvent(event) # Call the base class implementation        

    @property
    def trig_mode(self):
        return self._trig_mode
    
    @trig_mode.setter
    def trig_mode(self, value):
        number, ok = self.locale.toDouble(self.text())

        self._trig_mode = value

        match value:
            case TrigMode.RAD:
                if ok:
                    self.setTextSelect(self.toString(AppGlobals.angle_unit.to_rad_with_protocol(number)))
                AppGlobals.angle_unit = RadUnitProtocol()
            case TrigMode.GRA:
                if ok:
                    self.setTextSelect(self.toString(AppGlobals.angle_unit.to_gra_with_protocol(number)))
                AppGlobals.angle_unit = GraUnitProtocol()
            case _:
                if ok:
                    self.setTextSelect(self.toString(AppGlobals.angle_unit.to_deg_with_protocol(number)))
                AppGlobals.angle_unit = DegUnitProtocol()

    def trig_mode_init(self, value):
        self._trig_mode = TrigMode(value)

        match TrigMode(value):
            case TrigMode.RAD:
                AppGlobals.angle_unit = RadUnitProtocol()
            case TrigMode.GRA:
                AppGlobals.angle_unit = GraUnitProtocol()
            case _:
                AppGlobals.angle_unit = DegUnitProtocol()

    def exec_ln(self):
        if (self.store_number()):
            expr = LnExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_ex(self):
        if (self.store_number()):
            expr = EPowerXExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_log(self):
        if (self.store_number()):
            expr = LogExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_ten_power_x(self):
        if (self.store_number()):
            expr = TenPowerXExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_sin(self):
        if (self.store_number()):
            expr = SinExpression(AppGlobals.table, AppGlobals.angle_unit)
            self.setText(self.toString(expr.calculate(self.number)))
            self.selectAll()

    def exec_arcsin(self):
        if (self.store_number()):
            expr = ArcSinExpression(AppGlobals.table, AppGlobals.angle_unit)
            self.setText(self.toString(expr.calculate(self.number)))
            self.selectAll()

    def exec_cos(self):
        if (self.store_number()):
            expr = CosExpression(AppGlobals.table, AppGlobals.angle_unit)
            self.setText(self.toString(expr.calculate(self.number)))
            self.selectAll()

    def exec_arccos(self):
        if (self.store_number()):
            expr = ArcCosExpression(AppGlobals.table, AppGlobals.angle_unit)
            self.setText(self.toString(expr.calculate(self.number)))
            self.selectAll()

    def exec_tan(self):
        if (self.store_number()):
            expr = TanExpression(AppGlobals.table, AppGlobals.angle_unit)
            self.setTextSelect(self.toString(expr.calculate(self.number)))
            self.selectAll()

    def exec_arctan(self):
        if (self.store_number()):
            expr = ArcTanExpression(AppGlobals.table, AppGlobals.angle_unit)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

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

    @property
    def memory(self):
        return self._memory
    
    @memory.setter
    def memory(self, value: float):
        self._memory = value
        self.memory_changed.emit(self.memory_to_format_string())
        
    def exec_MS(self):
        if self.store_number():
            self.memory = self.number
            self.selectAll()
            # show in protocol
            MSExpression(AppGlobals.table).calculate(self.number)

    def exec_MR(self):
        self.setText(self.memory_to_string())
        self.selectAll()

    def exec_M_plus(self):
        if self.store_number():
            self.memory = MPlusExpression(self.memory, AppGlobals.table).calculate(self.number)

    def exec_M_minus(self):
        if self.store_number():
            self.memory = MMinusExpression(self.memory, AppGlobals.table).calculate(self.number)

    def exec_m_multiply(self):
        if self.store_number():
            self.memory = MMultiplyExpression(self.memory, AppGlobals.table).calculate(self.number)

    def exec_m_division(self):
        if self.store_number():
            self.memory = MDisivionExpression(self.memory, AppGlobals.table).calculate(self.number)

    def exec_backspace(self):
        # Create and send a backspace key event
        event = QKeyEvent(QKeyEvent.KeyPress, Qt.Key_Backspace, Qt.NoModifier)
        QApplication.sendEvent(self, event)

    def exec_reciprocal(self):
        if (self.store_number()):
            expr = ReciprocalExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_sign_change(self):
        self.insert("-")

    def exec_exponent(self):
        self.insert("e")

    def exec_del_last_line(self):
        # Remove the last row in protocol
        # Create a warning message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText("Are you sure you want to delete the last row in protocol?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.Yes)

        # Show the message box and get the user's response
        result = msg_box.exec()

        if result == QMessageBox.Yes:
            # Proceed with deletion
            last_row = AppGlobals.table.rowCount() - 1
            if last_row >= 0:
                AppGlobals.table.removeRow(last_row)

    def exec_comment(self):
        dialog = CommentDialog()
        dialog.ui.lineEdit.setText(self.text())
        if dialog.exec():
            comment = dialog.get_comment()
            row = AppGlobals.table.rowCount()
            AppGlobals.table.insertRow(row)        
            AppGlobals.table.scrollToBottom()
            AppGlobals.table.setItem(row, 0, QTableWidgetItem(comment))

    def get_key_state(self, key_code):
        return bool(ctypes.windll.user32.GetKeyState(key_code) & 0x0001)
    
    def numlock_state(self):
        return self.get_key_state(0x90)

    def handle_numpad_keys(self, event):
        if self.current_shift_state:
            # shift was pressed
            match self.key:
                case Qt.Key_Enter | Qt.Key_Return | Qt.Key_Equal:         
                    self.exec_percent()
                case Qt.Key.Key_Plus:
                    self.exec_percent()
                case Qt.Key.Key_Slash:
                    self.exec_pi()
                case Qt.Key.Key_Asterisk:
                    self.exec_pow()
                case _:
                    # Call base class to keep normal behavior
                    super().keyPressEvent(event)
        elif self.current_ctrl_state:
            # ctrl is pressed
            match self.key:
                case Qt.Key_Enter | Qt.Key_Return | Qt.Key_Equal:         
                    self.exec_percent()
                case Qt.Key.Key_Comma:
                    self.exec_factorial()
                case Qt.Key.Key_0:
                    self.exec_swap()
                case Qt.Key.Key_1:
                    self.exec_ex()
                case Qt.Key.Key_2: # Numpad 2
                    self.exec_square()
                case Qt.Key.Key_3:
                    self.exec_cube()    
                case Qt.Key.Key_4: # Numpad 4
                    self.exec_arcsin()
                case Qt.Key.Key_5: # Numpad 5
                    self.exec_arccos()
                case Qt.Key.Key_6: # Numpad 6
                    self.exec_arctan()
                case Qt.Key.Key_7: # Numpad 7
                    self.exec_ten_power_x()
                case Qt.Key.Key_8: # Numpad 8
                    self.exec_MS()
                case Qt.Key.Key_9: # Numpad 9
                    self.exec_MR()
                case Qt.Key_Plus:
                    self.exec_M_plus()
                case Qt.Key_Minus:
                    self.exec_M_minus()
                case Qt.Key.Key_Asterisk:
                    self.exec_memory_swap()
                case Qt.Key.Key_Slash:
                    self.exec_pi()
                case _:
                    # Call base class to keep normal behavior
                    super().keyPressEvent(event)
                    QMessageBox.information(self, "Information", "No operation configured")
        else:
            # no shift and no ctrl was pressed
            match self.key:
                case Qt.Key.Key_Insert: # Numpad 0
                    self.exec_reciprocal()
                case Qt.Key.Key_Delete: # Numpad comma
                    self.exec_del_last_line()
                case Qt.Key.Key_End: # Numpad 1
                    self.exec_ln()
                case Qt.Key.Key_Down: # Numpad 2
                    self.exec_sqrt()
                case Qt.Key.Key_PageDown: # Numpad 3
                    self.exec_cube_root()
                case Qt.Key.Key_Left: # Numpad 4
                    self.exec_sin()
                case Qt.Key.Key_Clear: #Numpad 5
                    self.exec_cos()
                case Qt.Key.Key_Right: # Numpad 6
                    self.exec_tan()
                case Qt.Key.Key_Home: # Numpad 7
                    self.exec_log()
                case Qt.Key.Key_Up: # Numpad 8
                    self.exec_opening_bracket()
                case Qt.Key.Key_PageUp: # Numpad 9
                    self.exec_closing_bracket();
                case Qt.Key.Key_Plus:
                    self.exec_addition()
                case Qt.Key.Key_Minus:
                    self.exec_subtraction()
                case Qt.Key.Key_multiply | Qt.Key.Key_Asterisk:
                    self.exec_multiplication()
                case Qt.Key.Key_Slash | Qt.Key.Key_division:
                    self.exec_division()
                case Qt.Key.Key_Enter | Qt.Key.Key_Return | Qt.Key.Key_Equal:         
                    self.execute()
                case _:
                    # Call base class to keep normal behavior
                    super().keyPressEvent(event)

    def handle_chars(self, event):
        match self.key:
            case Qt.Key.Key_Plus:
                self.exec_addition()
            case Qt.Key.Key_Minus:
                self.exec_subtraction()
            case Qt.Key.Key_Asterisk:
                self.exec_multiplication()
            case Qt.Key.Key_Slash:
                self.exec_division()
            case Qt.Key.Key_ParenLeft:
                self.exec_opening_bracket()
            case Qt.Key.Key_ParenRight:
                self.exec_closing_bracket()
            case Qt.Key.Key_Equal:
                self.execute()
            case Qt.Key.Key_Percent:
                self.exec_percent()
            case Qt.Key.Key_Exclam:
                self.exec_factorial()
            case Qt.Key.Key_Underscore:
                self.exec_sign_change()
            case _:
                return False
            
        return True
    
    def handle_scan_codes(self):
        if self.current_shift_state:
            match self.scan_code:
                case 3: # Key 2
                    self.exec_sqrt()
                case 4: # Key 3
                    self.exec_cube_root()
                case _:
                    return False
            return True
        else:
            return False
        
        return True

    def handle_keys(self, event):
        if (event.modifiers() & Qt.KeypadModifier) and self.numlock_state(): # keypad keys
            self.handle_numpad_keys(event)
        else: # usual keys (no keypad keys)
            if self.handle_chars(event):
                return # it was a char, no further handling
            if self.handle_scan_codes():
                return

            if self.current_shift_state:
                # Shift pressed
                match self.key:
                    # case Qt.Key.Key_Exclam:
                    #    self.exec_factorial()
                    case Qt.Key.Key_Q:
                        self.exec_M_minus()
                    case Qt.Key.Key_W:
                        self.exec_M_plus()
                    case Qt.Key.Key_R:
                        self.exec_square()
                    case Qt.Key.Key_T:
                        self.exec_cube() 
                    case Qt.Key.Key_Z:
                        self.exec_m_division()
                    case Qt.Key.Key_A:
                        self.exec_ac()
                    case Qt.Key.Key_S:
                        self.exec_arcsin()
                    case Qt.Key.Key_D:
                        self.exec_arccos()
                    case Qt.Key.Key_F:
                        self.exec_arctan()
                    case Qt.Key.Key_G:
                        self.exec_rectangular_to_polar()
                    case Qt.Key.Key_Y:
                        self.exec_ex()
                    case Qt.Key.Key_X:
                        self.exec_ten_power_x()
                    case Qt.Key.Key_C:
                        self.exec_MS()
                    case Qt.Key.Key_V:
                        self.exec_MR()
                    case Qt.Key.Key_B:
                        self.exec_convert_to_dms()
                    case Qt.Key.Key_Backspace:
                        self.exec_del_last_line()
                    case Qt.Key.Key_Greater:
                        self.exec_memory_swap()
                    case Qt.Key.Key_Space:
                        self.exec_comment()
                    case _:
                        super().keyPressEvent(event) # keep normal behavior

            elif self.current_ctrl_state:
                match self.key:
                    case Qt.Key.Key_Space:
                        self.exec_comment()
                    case Qt.Key.Key_Backspace:
                        self.exec_del_last_line()
                    case _:
                        # ctrl pressed
                        super().keyPressEvent(event)
            else:
                # just keys, no shift, no ctrl
                match self.key:
                    case Qt.Key.Key_Q:
                        self.exec_pi()
                    case Qt.Key.Key_W:
                        self.exec_pow()
                    case Qt.Key.Key_R:
                        self.exec_sqrt()
                    case Qt.Key.Key_T:
                        self.exec_cube_root()    
                    case Qt.Key.Key_Z:
                        self.exec_m_multiply()
                    case Qt.Key.Key_A:
                        self.exec_ac()
                    case Qt.Key.Key_S:
                        self.exec_sin()
                    case Qt.Key.Key_D:
                        self.exec_cos()
                    case Qt.Key.Key_F:
                        self.exec_tan()
                    case Qt.Key.Key_G:
                        self.exec_reciprocal()
                    case Qt.Key.Key_Y:
                        self.exec_ln()
                    case Qt.Key.Key_X:
                        self.exec_log()
                    case Qt.Key.Key_C:
                        self.exec_c()
                    case Qt.Key.Key_V:
                        self.exec_MR()
                    case Qt.Key.Key_B:
                        self.exec_convert_to_bases()
                    case Qt.Key.Key_Escape:
                        self.exec_ac()
                    case Qt.Key_Enter | Qt.Key_Return | Qt.Key_Equal:
                            self.execute()
                    case Qt.Key.Key_Less:
                        self.exec_swap()
                    case Qt.Key.Key_Space:
                        self.execute()    
                    case _:
                        # Call base class to keep normal behavior
                        super().keyPressEvent(event)

    def exec_cut_to_clipboard(self):
        self.cut()

    def exec_copy_to_clipboard(self):
        self.copy()

    def exec_paste_from_clipboard(self):
        self.paste()

    def exec_undo(self):
        self.undo()
    
    def exec_redo(self):
        self.redo()

    def exec_square(self):
        if (self.store_number()):
            expr = SquareExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_cube(self):
        if (self.store_number()):
            expr = CubeExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_sqrt(self):
        if (self.store_number()):
            expr = SqrtExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_cube_root(self):
        if (self.store_number()):
            expr = CubeRootExpression(AppGlobals.table)
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_memory_swap(self):
        if self.store_number():
            temp_number = self.number
            self.setTextSelect(self.memory_to_string())
            self.memory = temp_number

    def exec_swap(self):
        if self.root_expression != None:
            if self.store_number():
                temp_number = self.last_expression().first_number
                self.last_expression().first_number = self.number
                self.setTextSelect(self.toString(temp_number))
                self.update_expression_label()

    def exec_convert_to_bases(self):
        if self.store_number():
            i_number: float = int(self.text())
            ConvertToBasesExpression(AppGlobals.table).calculate(self.number)
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

        if not dialog.exec():
            return
        
        degrees, ok = self.locale.toInt(dialog.ui.degreesLineEdit.text())
        minutes, ok  = self.locale.toInt(dialog.ui.minutesLineEdit.text())
        seconds, ok = self.locale.toDouble(dialog.ui.secondsLineEdit.text())
        self.setTextSelect(self.toString(DDExpression().calculate(degrees, minutes, seconds)))

    def exec_from_binary(self):
        dialog = ConvertFromBaseDialog(None, BaseExpression(AppGlobals.table, 2))
        dialog.setWindowTitle("Convert form Binary")
        dialog.ui.number_label.setText("&Binary:")
        i_number = 0

        try:
           i_number = int(self.text())
        except Exception as e:
            print(f"{str(e)}")
                
        dialog.ui.numberLineEdit.setText(format(i_number, 'b'))
        dialog.ui.numberLineEdit.setFocus()

        if dialog.exec():
            success, str_value = dialog.add_to_log()
            if success:
                self.setTextSelect(str_value)

    def exec_from_octal(self):
        dialog = ConvertFromBaseDialog(None, BaseExpression(AppGlobals.table, 8))
        dialog.setWindowTitle("Convert form Octal")
        dialog.ui.number_label.setText("&Octal:")
        i_number = 0

        try:
           i_number = int(self.text())
        except Exception as e:
            print(f"{str(e)}")
                
        dialog.ui.numberLineEdit.setText(format(i_number, 'o'))
        dialog.ui.numberLineEdit.setFocus()

        if dialog.exec():
            success, str_value = dialog.add_to_log()
            if success:
                self.setTextSelect(str_value)

    def exec_from_decimal(self):
        dialog = ConvertFromBaseDialog(None, BaseExpression(AppGlobals.table, 10))
        dialog.setWindowTitle("Convert form Decimal")
        dialog.ui.number_label.setText("&Decimal:")
        i_number = 0

        try:
           i_number = int(self.text())
        except Exception as e:
            print(f"{str(e)}")
                
        dialog.ui.numberLineEdit.setText(format(i_number, 'd'))
        dialog.ui.numberLineEdit.setFocus()

        if dialog.exec():
            success, str_value = dialog.add_to_log()
            if success:
                self.setTextSelect(str_value)

    def exec_from_hexadecimal(self):
        dialog = ConvertFromBaseDialog(None, BaseExpression(AppGlobals.table, 16))
        dialog.setWindowTitle("Convert form Hexadecimal")
        i_number = 0

        try:
           i_number = int(self.text())
        except Exception as e:
            print(f"{str(e)}")
                
        dialog.ui.numberLineEdit.setText(f"{i_number:X}")
        dialog.ui.numberLineEdit.setFocus()

        if dialog.exec():
            success, str_value = dialog.add_to_log()
            if success:
                self.setTextSelect(str_value)

    def exec_sinh(self):
        if self.store_number():
            expr = SinhExpression()
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_cosh(self):
        if self.store_number():
            expr = CoshExpression()
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_tanh(self):
        if self.store_number():
            expr = TanhExpression()
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_arsinh(self):
        if self.store_number():
            expr = ArsinhExpression()
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_arcosh(self):
        if self.store_number():
            expr = ArcoshExpression()
            self.setTextSelect(self.toString(expr.calculate(self.number)))

    def exec_artanh(self):
        if self.store_number():
            expr = ArtanhExpression()
            self.setTextSelect(self.toString(expr.calculate(self.number)))

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
