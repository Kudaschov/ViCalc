import os
import sys
import json
import ctypes
import webbrowser
from PySide6.QtCore import Qt, QSize
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QMessageBox, QStyleFactory, QMenu
from PySide6.QtGui import QActionGroup, QIcon
from PySide6.QtCore import QSettings, QByteArray, QSize, QPoint
from .ui.mainWindow import Ui_MainWindow # Make sure this path is correct
from PySide6.QtCore import QTimer
from PySide6.QtCore import QStandardPaths
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtGui import QFont, QColor
from .ui.InputTextEdit import InputTextEdit
from .CalcOperations import CalcOperations
from .TrigMode import TrigMode
from PySide6.QtCore import QUrl
from .ui.ClicableLabel import ClickableLabel
from .AboutDialog import AboutDialog
from .NumFormatDialog import NumFormatDialog
from .NumericFormat import NumericFormat
from .CellValue import CellValue
from .AppGlobals import AppGlobals
from .NumericCellValue import NumericCellValue
from PySide6.QtCore import QLocale, QDate, QTime
from .OptionsDialog import OptionsDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.trig_mode_group = QActionGroup(self)
        self.trig_mode_group.setExclusive(True)
        self.trig_mode_group.addAction(self.ui.action_DEG)
        self.trig_mode_group.addAction(self.ui.action_RAD)
        self.trig_mode_group.addAction(self.ui.action_GRA)

        # background color of C and AC buttons
        self.c_ac_bg_color = QColor("#D8D8FF")
        self.arithmetic_operation_color = QColor("#FEFEFE")

        layout = self.ui.verticalLayout
        old_widget = self.ui.inputTextEdit
        index = layout.indexOf(old_widget)
        layout.removeWidget(old_widget)
        old_widget.deleteLater()

        self.ui.inputTextEdit = InputTextEdit(self)
        self.ui.inputTextEdit.setObjectName("inputTextEdit")
        self.ui.inputTextEdit.setFont(old_widget.font())
        self.ui.inputTextEdit.setMaximumSize(old_widget.maximumSize())
        self.ui.inputTextEdit.expressionLabel = self.ui.expressionLabel
        layout.insertWidget(index, self.ui.inputTextEdit)

        self.ui.action_DEG.triggered.connect(self.mode_deg)
        self.ui.action_RAD.triggered.connect(self.mode_rad)
        self.ui.action_GRA.triggered.connect(self.mode_gra)

        self.ui.action_convert_from_binary.triggered.connect(self.convert_from_binary)
        self.ui.action_convert_from_octal.triggered.connect(self.convert_from_octal)
        self.ui.action_convert_from_decimal.triggered.connect(self.convert_from_decimal)
        self.ui.action_convert_from_hexadecimal.triggered.connect(self.convert_from_hexadecimal)

        self.ui.action_dms_to_dd.triggered.connect(self.dms_to_dd)

        self.ui.action_About.triggered.connect(self.show_about_dialog)
        self.ui.action_Help.triggered.connect(self.show_help)
        self.ui.action_numeric_format.triggered.connect(self.numeric_format)

        self.ui.actionInsertDateTime.triggered.connect(self.date_time_stamp)

        self.ui.action_sinh.triggered.connect(self.sinh)
        self.ui.action_cosh.triggered.connect(self.cosh)
        self.ui.action_tanh.triggered.connect(self.tanh)
        self.ui.action_arsinh.triggered.connect(self.arsinh)
        self.ui.action_arcosh.triggered.connect(self.arcosh)
        self.ui.action_artanh.triggered.connect(self.artanh)

        self.ui.action_rectangular_to_polar.triggered.connect(self.rectangular_to_polar)
        self.ui.action_polar_to_rectangular.triggered.connect(self.polar_to_rectangular)
        self.ui.action_combination.triggered.connect(self.combination)
        self.ui.action_permutaton.triggered.connect(self.permutation)

        self.ui.action_options.triggered.connect(self.options)

        # important: set tableWidget before read_settings because of angle units
        AppGlobals.table = self.ui.tableWidget
        self.settings = QSettings("Kudaschov", "ViCalc")
        self.read_settings()
        self.ui.inputTextEdit.setFocus()
        self.ui.inputTextEdit.selectAll()

        # connect mouse double click on table
        AppGlobals.table.cellDoubleClicked.connect(self.table_cell_double_clicked)

        # context menu
        AppGlobals.table.setContextMenuPolicy(Qt.CustomContextMenu)
        AppGlobals.table.customContextMenuRequested.connect(self.show_context_menu)

        # Define a list to store QPushButton objects
        self.button_list = []
        self.leftside_button_list = [] # for arrange position and size
        self.numpad_button_list = [] # for arrange position and size

        self.ui.pushButton0numpad.row = 4
        self.ui.pushButton0numpad.column = 0
        self.ui.pushButton0numpad.norm_width = 2
        self.ui.pushButton0numpad.shift_text = "<>"
        self.ui.pushButton0numpad.ctrl_text = "X<>M"
        self.ui.pushButton0numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton0numpad.base_operation = CalcOperations.number_0
        self.ui.pushButton0numpad.shift_operation = CalcOperations.swap
        self.ui.pushButton0numpad.ctrl_operation = CalcOperations.memory_swap
        self.numpad_button_list.append(self.ui.pushButton0numpad)

        self.ui.pushButton1numpad.row = 3
        self.ui.pushButton1numpad.column = 0
        self.ui.pushButton1numpad.shift_text = "ln"
        self.ui.pushButton1numpad.ctrl_text = "e^x"
        self.ui.pushButton1numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton1numpad.base_operation = CalcOperations.number_1
        self.ui.pushButton1numpad.shift_operation = CalcOperations.ln
        self.ui.pushButton1numpad.ctrl_operation = CalcOperations.ex
        self.numpad_button_list.append(self.ui.pushButton1numpad)

        self.ui.pushButton2numpad.row = 3
        self.ui.pushButton2numpad.column = 1
        self.ui.pushButton2numpad.shift_text = "√"
        self.ui.pushButton2numpad.ctrl_text = "x²"
        self.ui.pushButton2numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton2numpad.base_operation = CalcOperations.number_2
        self.ui.pushButton2numpad.shift_operation = CalcOperations.sqrt
        self.ui.pushButton2numpad.ctrl_operation = CalcOperations.square
        self.numpad_button_list.append(self.ui.pushButton2numpad)

        self.ui.pushButton3numpad.row = 3
        self.ui.pushButton3numpad.column = 2
        self.ui.pushButton3numpad.shift_text = "³√x"
        self.ui.pushButton3numpad.ctrl_text = "x³"
        self.ui.pushButton3numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton3numpad.base_operation = CalcOperations.number_3
        self.ui.pushButton3numpad.shift_operation = CalcOperations.cube_root
        self.ui.pushButton3numpad.ctrl_operation = CalcOperations.cube
        self.numpad_button_list.append(self.ui.pushButton3numpad)

        self.ui.pushButton4numpad.row = 2
        self.ui.pushButton4numpad.column = 0
        self.ui.pushButton4numpad.shift_text = "sin"
        self.ui.pushButton4numpad.ctrl_text = "-1"
        self.ui.pushButton4numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton4numpad.base_operation = CalcOperations.number_4
        self.ui.pushButton4numpad.shift_operation = CalcOperations.sin
        self.ui.pushButton4numpad.ctrl_operation = CalcOperations.arcsin
        self.numpad_button_list.append(self.ui.pushButton4numpad)

        self.ui.pushButton5numpad.row = 2
        self.ui.pushButton5numpad.column = 1
        self.ui.pushButton5numpad.shift_text = "cos"
        self.ui.pushButton5numpad.ctrl_text = "-1"
        self.ui.pushButton5numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton5numpad.base_operation = CalcOperations.number_5
        self.ui.pushButton5numpad.shift_operation = CalcOperations.cos
        self.ui.pushButton5numpad.ctrl_operation = CalcOperations.arccos
        self.numpad_button_list.append(self.ui.pushButton5numpad)

        self.ui.pushButton6numpad.row = 2
        self.ui.pushButton6numpad.column = 2
        self.ui.pushButton6numpad.shift_text = "tan"
        self.ui.pushButton6numpad.ctrl_text = "-1"
        self.ui.pushButton6numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton6numpad.base_operation = CalcOperations.number_6
        self.ui.pushButton6numpad.shift_operation = CalcOperations.tan
        self.ui.pushButton6numpad.ctrl_operation = CalcOperations.arctan
        self.numpad_button_list.append(self.ui.pushButton6numpad)

        self.ui.pushButton7numpad.row = 1
        self.ui.pushButton7numpad.column = 0
        self.ui.pushButton7numpad.shift_text = "log"
        self.ui.pushButton7numpad.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButton7numpad.ctrl_text = "10^X"
        self.ui.pushButton7numpad.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButton7numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton7numpad.base_operation = CalcOperations.number_7
        self.ui.pushButton7numpad.shift_operation = CalcOperations.log
        self.ui.pushButton7numpad.ctrl_operation = CalcOperations.ten_power_10
        self.numpad_button_list.append(self.ui.pushButton7numpad)

        self.ui.pushButton8numpad.row = 1
        self.ui.pushButton8numpad.column = 1
        self.ui.pushButton8numpad.shift_text = "("
        self.ui.pushButton8numpad.ctrl_text = "MS"
        self.ui.pushButton8numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton8numpad.base_operation = CalcOperations.number_8
        self.ui.pushButton8numpad.shift_operation = CalcOperations.opening_bracket
        self.ui.pushButton8numpad.ctrl_operation = CalcOperations.MS
        self.numpad_button_list.append(self.ui.pushButton8numpad)

        self.ui.pushButton9numpad.row = 1
        self.ui.pushButton9numpad.column = 2
        self.ui.pushButton9numpad.shift_text = ")"
        self.ui.pushButton9numpad.ctrl_text = "MR"
        self.ui.pushButton9numpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton9numpad.base_operation = CalcOperations.number_9
        self.ui.pushButton9numpad.shift_operation = CalcOperations.closing_bracket
        self.ui.pushButton9numpad.ctrl_operation = CalcOperations.MR
        self.numpad_button_list.append(self.ui.pushButton9numpad)

        self.ui.pushButtonAC.row = 0
        self.ui.pushButtonAC.column = 0
        self.ui.pushButtonAC.setText("AC")
        self.ui.pushButtonAC.bg_color = self.c_ac_bg_color
        self.ui.pushButtonAC.shift_text = "C"
        self.ui.pushButtonAC.ctrl_text = "C"
        self.ui.pushButtonAC.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButtonAC.base_operation = CalcOperations.AC
        self.ui.pushButtonAC.shift_operation = CalcOperations.C
        self.ui.pushButtonAC.ctrl_operation = CalcOperations.C
        self.numpad_button_list.append(self.ui.pushButtonAC)

        self.ui.pushButtonBackspace.row = 0
        self.ui.pushButtonBackspace.column = 6
        self.ui.pushButtonBackspace.bg_color = self.c_ac_bg_color
        self.ui.pushButtonBackspace.shift_text = "Del Line"
        self.ui.pushButtonBackspace.ctrl_text = "Del Line"
        self.ui.pushButtonBackspace.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButtonBackspace.base_operation = CalcOperations.backspace
        self.ui.pushButtonBackspace.shift_operation = CalcOperations.del_last_line
        self.ui.pushButtonBackspace.ctrl_operation = CalcOperations.del_last_line
        self.leftside_button_list.append(self.ui.pushButtonBackspace)

        self.ui.pushButtonCommaNumpad.row = 4
        self.ui.pushButtonCommaNumpad.column = 2
        self.ui.pushButtonCommaNumpad.shift_text = "<-"
        self.ui.pushButtonCommaNumpad.ctrl_text = "DL"
        self.ui.pushButtonCommaNumpad.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButtonCommaNumpad.base_operation = CalcOperations.comma
        self.ui.pushButtonCommaNumpad.shift_operation = CalcOperations.backspace
        self.ui.pushButtonCommaNumpad.ctrl_operation = CalcOperations.del_last_line
        self.numpad_button_list.append(self.ui.pushButtonCommaNumpad)

        self.ui.pushButtonMinusNumpad.row = 0
        self.ui.pushButtonMinusNumpad.column = 3
        self.ui.pushButtonMinusNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonMinusNumpad.shift_text = "(-)"
        self.ui.pushButtonMinusNumpad.ctrl_text = "M-"
        self.ui.pushButtonMinusNumpad.base_operation = CalcOperations.Minus
        self.ui.pushButtonMinusNumpad.shift_operation = CalcOperations.SignChange
        self.ui.pushButtonMinusNumpad.ctrl_operation = CalcOperations.M_minus
        self.ui.pushButtonMinusNumpad.input_text_edit = self.ui.inputTextEdit
        self.numpad_button_list.append(self.ui.pushButtonMinusNumpad)

        self.ui.pushButtonEnter.row = 2
        self.ui.pushButtonEnter.column = 6
#        self.ui.pushButtonEnter.norm_width = 1
        self.ui.pushButtonEnter.bg_color = self.arithmetic_operation_color
#        self.ui.pushButtonEnter.shift_text = "MS"
#        self.ui.pushButtonEnter.ctrl_text = "MR"
        self.ui.pushButtonEnter.base_operation = CalcOperations.calculate
        self.ui.pushButtonEnter.shift_operation = CalcOperations.calculate
        self.ui.pushButtonEnter.ctrl_operation = CalcOperations.calculate
        self.ui.pushButtonEnter.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonEnter)

        self.ui.pushButtonEnterNumpad.row = 2
        self.ui.pushButtonEnterNumpad.column = 3
        self.ui.pushButtonEnterNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonEnterNumpad.shift_text = "%"
        self.ui.pushButtonEnterNumpad.ctrl_text = "%"
        self.ui.pushButtonEnterNumpad.base_operation = CalcOperations.calculate
        self.ui.pushButtonEnterNumpad.shift_operation = CalcOperations.percent
        self.ui.pushButtonEnterNumpad.ctrl_operation = CalcOperations.percent
        self.ui.pushButtonEnterNumpad.input_text_edit = self.ui.inputTextEdit
        self.numpad_button_list.append(self.ui.pushButtonEnterNumpad)

        self.ui.pushButtonPlusNumpad.row = 1
        self.ui.pushButtonPlusNumpad.column = 3
        self.ui.pushButtonPlusNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonPlusNumpad.shift_text = "M+"
        self.ui.pushButtonPlusNumpad.ctrl_text = "M+"
        self.ui.pushButtonPlusNumpad.base_operation = CalcOperations.Plus
        self.ui.pushButtonPlusNumpad.shift_operation = CalcOperations.M_plus
        self.ui.pushButtonPlusNumpad.ctrl_operation = CalcOperations.M_plus
        self.ui.pushButtonPlusNumpad.input_text_edit = self.ui.inputTextEdit
        self.numpad_button_list.append(self.ui.pushButtonPlusNumpad)

        self.ui.pushButtonMultiplyNumpad.row = 0
        self.ui.pushButtonMultiplyNumpad.column = 2
        self.ui.pushButtonMultiplyNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonMultiplyNumpad.shift_text = "x^y"
        #self.ui.pushButtonMultiplyNumpad.shift_font = QFont("Helvetica", 8)
        #self.ui.pushButtonMultiplyNumpad.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButtonMultiplyNumpad.ctrl_text = "n!"
        #self.ui.pushButtonMultiplyNumpad.ctrl_font = QFont("Helvetica", 8)
        #self.ui.pushButtonMultiplyNumpad.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonMultiplyNumpad.base_operation = CalcOperations.Multiply
        self.ui.pushButtonMultiplyNumpad.shift_operation = CalcOperations.pow
        self.ui.pushButtonMultiplyNumpad.ctrl_operation = CalcOperations.factorial
        self.ui.pushButtonMultiplyNumpad.input_text_edit = self.ui.inputTextEdit
        self.numpad_button_list.append(self.ui.pushButtonMultiplyNumpad)

        self.ui.pushButtonDivisionNumpad.row = 0
        self.ui.pushButtonDivisionNumpad.column = 1
        self.ui.pushButtonDivisionNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonDivisionNumpad.shift_text = "1/x"
        self.ui.pushButtonDivisionNumpad.ctrl_text = "Pi"
        self.ui.pushButtonDivisionNumpad.base_operation = CalcOperations.Division
        self.ui.pushButtonDivisionNumpad.shift_operation = CalcOperations.reciprocal
        self.ui.pushButtonDivisionNumpad.ctrl_operation = CalcOperations.pi
        self.ui.pushButtonDivisionNumpad.input_text_edit = self.ui.inputTextEdit
        self.numpad_button_list.append(self.ui.pushButtonDivisionNumpad)

        self.ui.pushButtonSpace.row = 4
        self.ui.pushButtonSpace.column = 0.5
        self.ui.pushButtonSpace.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonSpace.norm_width = 5.93
        self.ui.pushButtonSpace.setText("=")
        self.ui.pushButtonSpace.shift_text = "Comment"
        self.ui.pushButtonSpace.ctrl_text = "Comment"
        self.ui.pushButtonSpace.base_operation = CalcOperations.calculate
        self.ui.pushButtonSpace.shift_operation = CalcOperations.comment
        self.ui.pushButtonSpace.ctrl_operation = CalcOperations.comment
        self.ui.pushButtonSpace.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonSpace)

        self.numbers_row_keyboard()
        self.first_row_keyboard()
        self.second_row_keyboard()
        self.third_row_keyboard()
        self.arrange_keyboard()

        self.ui.inputTextEdit.button_list = self.button_list

        AppGlobals.table.verticalHeader().setStyleSheet("QHeaderView::section { color: gray; }")
        AppGlobals.table.setColumnCount(7)
        AppGlobals.table.setHorizontalHeaderLabels(["A", "B", "C", "D", "E", "F", "G"])
        self.connect_table_signals()

        self.memory_label = ClickableLabel("Memory:")
        self.memory_label.clicked.connect(self.memory_label_clicked)
        self.ui.statusbar.addWidget(self.memory_label)

        self.numeric_format_label = ClickableLabel("Numeric Format:")
        self.numeric_format_label.clicked.connect(self.numeric_format_clicked)
        self.ui.statusbar.addWidget(self.numeric_format_label)

        self.capslock_label = QLabel("CapsLock")
        self.ui.statusbar.addWidget(self.capslock_label)
        self.numlock_label = QLabel("Numlock")
        self.ui.statusbar.addWidget(self.numlock_label)
        self.status_label_current_stylesheet = "font-size: 15px;"
        self.mode_label = QLabel("Mode")
        self.ui.statusbar.addWidget(self.mode_label)

        self.save_path = os.path.join(
        QStandardPaths.writableLocation(QStandardPaths.AppDataLocation), "vicalc_data.vic")
        self.load_table_data()         

        self.start_key_state_monitor()     

        # --- Connect the custom signal from InputTextEdit ---
        self.ui.inputTextEdit.shiftStatusChanged.connect(self.updateButtonsForShift)
        self.ui.inputTextEdit.ctrlStatusChanged.connect(self.updateButtonsForCtrl)
        self.ui.inputTextEdit.focusOut.connect(self.change_mode)
        self.ui.inputTextEdit.memory_changed.connect(self.memory_changed)
        # --- End custom signal connection ---       

        # Exit-Menüaktion verbinden
        self.ui.actionExit.triggered.connect(self.close)     
        self.ui.actionToggle_Protocol.triggered.connect(self.toggle_protocol)
        self.ui.action_delete_full_protocol.triggered.connect(self.delete_full_protocol)

    def show_context_menu(self, pos):
        global_pos = AppGlobals.table.viewport().mapToGlobal(pos)
        item = AppGlobals.table.itemAt(pos)
        if item:
            menu = QMenu(self)
            action_paste_to_calculator = menu.addAction("Paste to calculator")
            action_delete = menu.addAction("Delete row(s)")
            action = menu.exec(global_pos)
            if action == action_paste_to_calculator:
                val = item.data(Qt.UserRole)
                str = item.data(Qt.DisplayRole)
                if val:
                    if isinstance(val, NumericCellValue):
                        self.ui.inputTextEdit.setText(AppGlobals.to_normal_string(val.value()))
                else:
                    self.ui.inputTextEdit.setText(item.text())
                self.ui.inputTextEdit.setFocus()
                self.ui.inputTextEdit.selectAll()
            elif action == action_delete:
                # Create a warning message box
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Warning")
                msg_box.setText("Are you sure you want to delete row(s)?")
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg_box.setDefaultButton(QMessageBox.No)

                # Show the message box and get the user's response
                result = msg_box.exec()

                if result == QMessageBox.Yes:
                    selected_ranges = AppGlobals.table.selectedRanges()
                    rows_to_delete = set()
                    for r in selected_ranges:
                        rows_to_delete.update(range(r.topRow(), r.bottomRow() + 1))

                    for row in sorted(rows_to_delete, reverse=True):
                        AppGlobals.table.removeRow(row)

    def delete_full_protocol(self):                        
        # Create a warning message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText("Are you sure you want to Delete Full Log?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        # Show the message box and get the user's response
        result = msg_box.exec()

        if result == QMessageBox.Yes:
            AppGlobals.table.setRowCount(0)

    def connect_table_signals(self):
        AppGlobals.table.enterPressed.connect(self.cell_enter_pressed)
        AppGlobals.table.escPressed.connect(self.cell_esc_pressed)

    def cell_esc_pressed(self):
        if (self.is_tableWidget_editing() == False):
            # tableWidget is not editing, go in calculator mode
            self.ui.inputTextEdit.setFocus()
            self.ui.inputTextEdit.selectAll()

    def cell_enter_pressed(self, row, col):
        if (self.is_tableWidget_editing() == False):
            # tableWidget is not editing, put the current value in inputTextEdit
            item = AppGlobals.table.item(row, col)
            val = item.data(Qt.UserRole)
            str = item.data(Qt.DisplayRole)
            if val:
                if isinstance(val, NumericCellValue):
                    self.ui.inputTextEdit.setText(AppGlobals.to_normal_string(val.value()))
            else:
                self.ui.inputTextEdit.setText(item.text())
            self.ui.inputTextEdit.setFocus()
            self.ui.inputTextEdit.selectAll()

    def is_tableWidget_editing(self) -> bool:
        # is the tableWidget in edit mode
        current_item = AppGlobals.table.currentItem()
        if current_item:
            return AppGlobals.table.isPersistentEditorOpen(current_item)
        return False         

    def read_settings(self):
        saved_text = self.settings.value("inputText", "")
        try:
            self.ui.inputTextEdit.setText(saved_text)
            self.ui.inputTextEdit.trig_mode_init(self.settings.value("trig_mode"))
            self.ui.inputTextEdit.memory = self.settings.value("memory", type=float)

            AppGlobals.numeric_precision = self.settings.value("numeric_precision", type=int)
            AppGlobals.numeric_format = NumericFormat(self.settings.value("numeric_format"))
            AppGlobals.timestamp_at_start = self.settings.value("timestamp_at_start", True, type=bool)

            match self.ui.inputTextEdit.trig_mode:
                case TrigMode.RAD:
                    self.ui.action_RAD.setChecked(True)
                case TrigMode.GRA:
                    self.ui.action_GRA.setChecked(True)
                case _:
                    self.ui.action_DEG.setChecked(True)

            geometry = self.settings.value("MainWindow/geometry", QByteArray())
            if not geometry.isEmpty():
                self.restoreGeometry(geometry)
            else:
                self.resize(800, 600)
                self.move(100, 100)

            state = self.settings.value("MainWindow/windowState", QByteArray())
            if not state.isEmpty():
                self.restoreState(state)       
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

    def start_key_state_monitor(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_key_states)
        self.timer.start(500)   # Check every 500 ms

    def check_key_states(self):
        caps = self.get_key_state(0x14)      # CapsLock
        num = self.get_key_state(0x90)       # NumLock
        shift = self.get_async_state(0x10)   # Shift
        ctrl = self.get_async_state(0x11)    # Ctrl
        alt = self.get_async_state(0x12)     # Alt

        msg = f"CapsLock: {'ON' if caps else 'OFF'} | NumLock: {'ON' if num else 'OFF'} | " \
              f"Shift: {'DOWN' if shift else 'UP'} | Ctrl: {'DOWN' if ctrl else 'UP'} | Alt: {'DOWN' if alt else 'UP'}"
        
        if num:
            self.numlock_label.setText("")
        else:
            self.numlock_label.setStyleSheet(self.status_label_current_stylesheet + "background-color: yellow;")
            self.numlock_label.setText("Numlock: OFF")

        if caps:
            self.capslock_label.setStyleSheet(self.status_label_current_stylesheet + "background-color: yellow;")
            self.capslock_label.setText("Capslock: ON")
        else:
            self.capslock_label.setText("")

        """
        # Get the currently focused widget from the QApplication
        focused_widget = QApplication.focusWidget()

        if focused_widget:
            # You can check its objectName for identification
            print(f"Focused widget objectName: {focused_widget.objectName()}")
            # Or check its class type
            print(f"Focused widget class: {focused_widget.__class__.__name__}")
        else:
            print("No widget currently has focus.")
#        self.ui.statusbar.showMessage(msg)
        """

    def get_key_state(self, key_code):
        return bool(ctypes.windll.user32.GetKeyState(key_code) & 0x0001)

    def get_async_state(self, key_code):
        return bool(ctypes.windll.user32.GetAsyncKeyState(key_code) & 0x8000)         

    def show_about_dialog(self):
        about_dialog = AboutDialog(self)
#        about_dialog.setWindowTitle("Über die Anwendung")
        about_dialog.exec()

    def numeric_format(self):
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

        self.update_numeric_format_label()

        # update table
        rows = AppGlobals.table.rowCount()
        cols = AppGlobals.table.columnCount()

        for row in range(rows):
            for col in range(cols):
                item = AppGlobals.table.item(row, col)
                if item:
                    cell_value = item.data(Qt.UserRole)
                    if item.text().strip() or cell_value != None:  # Zelle ist vorhanden und nicht leer
                        if isinstance(cell_value, CellValue):
                            item.setText(cell_value.to_string())
        # update memory
        self.memory_changed(self.ui.inputTextEdit.memory_to_format_string())

    def update_numeric_format_label(self):
        match AppGlobals.numeric_format:
            case NumericFormat.general:
                self.numeric_format_label.setText("General format: " + str(AppGlobals.numeric_precision))
            case NumericFormat.fixed:
                self.numeric_format_label.setText("Fixed point format: " + str(AppGlobals.numeric_precision))
            case NumericFormat.scientific:
                self.numeric_format_label.setText("Scientific format: " + str(AppGlobals.numeric_precision))
            case NumericFormat.engineering:
                self.numeric_format_label.setText("Engineerig format: " + str(AppGlobals.numeric_precision))
            case _:
                self.numeric_format_label.setText("")

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.abspath(relative_path)

    def show_help(self):
        help_path = self.resource_path("help/site/index.html")

        if os.path.exists(help_path):
            webbrowser.open(f"file:///{help_path}")
        else:
            # Optional: Add a warning dialog here
            print("Help file not found. Run `mkdocs build` first.")
            QMessageBox.information(self, "Path not found!", help_path)

    def closeEvent(self, event):
        self.settings.setValue("inputText", self.ui.inputTextEdit.text())
        self.settings.setValue("trig_mode", self.ui.inputTextEdit.trig_mode.value)
        self.settings.setValue("memory", self.ui.inputTextEdit.memory)

        self.settings.setValue("numeric_format", AppGlobals.numeric_format.value)
        self.settings.setValue("numeric_precision", AppGlobals.numeric_precision)
        self.settings.setValue("timestamp_at_start", AppGlobals.timestamp_at_start)

        self.save_table_data()

        self.settings.setValue("MainWindow/geometry", self.saveGeometry())
        self.settings.setValue("MainWindow/windowState", self.saveState())

        super().closeEvent(event)

    def save_table_data(self):
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
        AppGlobals.table.save_to_file(self.save_path)

    def load_table_data(self):
        try:
            if os.path.exists(self.save_path):
                AppGlobals.table.load_from_file(self.save_path)
            AppGlobals.table.scrollToBottom()
        except Exception as err:
            print(f"Possible for the first reading {err=}, {type(err)=}")

  # --- New Slot Method to update buttons ---
    def updateButtonsForShift(self, is_shift_pressed: bool):
        print(f"MainWindow received Shift status: {is_shift_pressed}")

        if is_shift_pressed:
            for button in self.button_list:
                button.shift = True
        else:
            for button in self.button_list:
                button.shift = False

    # --- End New Slot Method ---            

  # --- New Slot Method to update buttons ---
    def updateButtonsForCtrl(self, is_ctrl_pressed: bool):
        """
        Slot to update the state or text of buttons in MainWindow
        based on the Shift key's pressed status.
        """
        print(f"MainWindow received Ctrl status: {is_ctrl_pressed}")

        if is_ctrl_pressed:
            for button in self.button_list:
                button.ctrl = True
        else:
            for button in self.button_list:
                button.ctrl = False

    # --- End New Slot Method ---        

    def memory_changed(self, sMemory: str):
        if self.ui.inputTextEdit.memory == 0:
            self.memory_label.setText("")
        else:
            self.memory_label.setText("Memory: " + sMemory)

    def change_mode(self):
        if AppGlobals.table.hasFocus():
            self.mode_label.setStyleSheet(self.status_label_current_stylesheet + "background-color: yellow;")
            self.mode_label.setText("Log")
        else:
            self.mode_label.setText("")

    def mode_deg(self):
        self.ui.inputTextEdit.trig_mode = TrigMode.DEG

    def mode_rad(self):
        self.ui.inputTextEdit.trig_mode = TrigMode.RAD

    def mode_gra(self):
        self.ui.inputTextEdit.trig_mode = TrigMode.GRA

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(0, self.after_mainwindow_show)

    def after_mainwindow_show(self):
        self.memory_changed(self.ui.inputTextEdit.memory_to_format_string())
        self.update_numeric_format_label()
        if AppGlobals.timestamp_at_start:
            self.date_time_stamp()

    def date_time_stamp(self):
        separator = "**********"
        if AppGlobals.table.columnCount() < 5:
            AppGlobals.table.setColumnCount(5)
        row = AppGlobals.table.rowCount()
        AppGlobals.table.insertRow(row)

        item = QTableWidgetItem()
        item.setText(separator)
        AppGlobals.table.setItem(row, 0, item)
        
        item = QTableWidgetItem()
        item.setText(QLocale().toString(QDate.currentDate(), QLocale.ShortFormat))
        AppGlobals.table.setItem(row, 1, item)

        item = QTableWidgetItem()
        item.setText(separator)
        AppGlobals.table.setItem(row, 2, item)

        item = QTableWidgetItem()
        item.setText(QLocale().toString(QTime.currentTime(), QLocale.ShortFormat))
        AppGlobals.table.setItem(row, 3, item)

        item = QTableWidgetItem()
        item.setText(separator)
        AppGlobals.table.setItem(row, 4, item)

        AppGlobals.table.scrollToBottom()

    def memory_label_clicked(self):
        self.ui.inputTextEdit.exec_MR()

    def numeric_format_clicked(self):
        self.numeric_format()

    def toggle_protocol(self):
        if self.ui.inputTextEdit.hasFocus():
            AppGlobals.table.setFocus()
            if -1 != AppGlobals.current_row and -1 != AppGlobals.current_column:
                AppGlobals.table.setCurrentCell(AppGlobals.current_row, AppGlobals.current_column)
        else:
            self.ui.inputTextEdit.setFocus()

    def numbers_row_keyboard(self):
        self.ui.pushButton1.row = 0
        self.ui.pushButton1.column = 0
        self.ui.pushButton1.shift_text = "n!"
        self.ui.pushButton1.ctrl_text = ""
        self.ui.pushButton1.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton1.base_operation = CalcOperations.number_1
        self.ui.pushButton1.shift_operation = CalcOperations.factorial
        self.ui.pushButton1.ctrl_operation = CalcOperations.factorial
        self.leftside_button_list.append(self.ui.pushButton1)

        self.ui.pushButton2.row = 0
        self.ui.pushButton2.column = 1
        self.ui.pushButton2.shift_text = "√"
        self.ui.pushButton2.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton2.base_operation = CalcOperations.number_2
        self.ui.pushButton2.shift_operation = CalcOperations.sqrt
        self.ui.pushButton2.ctrl_operation = CalcOperations.sqrt
        self.leftside_button_list.append(self.ui.pushButton2)

        self.ui.pushButton3.row = 0
        self.ui.pushButton3.column = 2
        self.ui.pushButton3.shift_text = "³√x"
        #self.ui.pushButton3.ctrl_text = "n!"
        self.ui.pushButton3.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton3.base_operation = CalcOperations.number_3
        self.ui.pushButton3.shift_operation = CalcOperations.cube_root
        self.ui.pushButton3.ctrl_operation = CalcOperations.cube_root
        self.leftside_button_list.append(self.ui.pushButton3)

        self.ui.pushButton4.row = 0
        self.ui.pushButton4.column = 3
        #self.ui.pushButton4.shift_text = "n!"
        #self.ui.pushButton4.ctrl_text = "n!"
        self.ui.pushButton4.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton4.base_operation = CalcOperations.number_4
        self.ui.pushButton4.shift_operation = CalcOperations.number_4
        self.ui.pushButton4.ctrl_operation = CalcOperations.number_4
        self.leftside_button_list.append(self.ui.pushButton4)

        self.ui.pushButton5.row = 0
        self.ui.pushButton5.column = 4
        self.ui.pushButton5.shift_text = "%"
        #self.ui.pushButton5.ctrl_text = "n!"
        self.ui.pushButton5.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton5.base_operation = CalcOperations.number_5
        self.ui.pushButton5.shift_operation = CalcOperations.percent
        self.ui.pushButton5.ctrl_operation = CalcOperations.percent
        self.leftside_button_list.append(self.ui.pushButton5)

        self.ui.pushButton6.row = 0
        self.ui.pushButton6.column = 5
        #self.ui.pushButton6.shift_text = "n!"
        #self.ui.pushButton6.ctrl_text = "n!"
        self.ui.pushButton6.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButton6.base_operation = CalcOperations.number_6
        self.ui.pushButton6.shift_operation = CalcOperations.number_6
        self.ui.pushButton6.ctrl_operation = CalcOperations.number_6
        self.leftside_button_list.append(self.ui.pushButton6)

    def first_row_keyboard(self):
        self.ui.pushButtonQ.row = 1
        self.ui.pushButtonQ.column = 0.5
        self.ui.pushButtonQ.setText("Pi")
        self.ui.pushButtonQ.original_keyboard_text = "Q"
        self.ui.pushButtonQ.shift_text = "M-"
        self.ui.pushButtonQ.ctrl_text = "nCr"
        self.ui.pushButtonQ.base_operation = CalcOperations.pi
        self.ui.pushButtonQ.shift_operation = CalcOperations.M_minus
        self.ui.pushButtonQ.ctrl_operation = CalcOperations.combination
        self.ui.pushButtonQ.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonQ)

        self.ui.pushButtonW.row = 1
        self.ui.pushButtonW.column = 1.5
        self.ui.pushButtonW.setText("x^y")
        self.ui.pushButtonW.original_keyboard_text = "W"
        self.ui.pushButtonW.shift_text = "M+"
        self.ui.pushButtonW.ctrl_text = "nPr"
        self.ui.pushButtonW.base_operation = CalcOperations.pow
        self.ui.pushButtonW.shift_operation = CalcOperations.M_plus
        self.ui.pushButtonW.ctrl_operation = CalcOperations.permutation
        self.ui.pushButtonW.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonW)

        self.ui.pushButtonE.row = 1
        self.ui.pushButtonE.column = 2.5
        # special key exponent have other bg color
        self.ui.pushButtonE.bg_color = self.arithmetic_operation_color
        #self.ui.pushButtonE.shift_text = "n!"
        #self.ui.pushButtonE.ctrl_text = "n!"
        self.ui.pushButtonE.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButtonE.base_operation = CalcOperations.exponent
        self.ui.pushButtonE.shift_operation = CalcOperations.exponent
        self.ui.pushButtonE.ctrl_operation = CalcOperations.exponent
        self.leftside_button_list.append(self.ui.pushButtonE)

        self.ui.pushButtonR.row = 1
        self.ui.pushButtonR.column = 3.5
        self.ui.pushButtonR.setText("√")
        self.ui.pushButtonR.original_keyboard_text = "R"
        self.ui.pushButtonR.shift_text = "x²"
        self.ui.pushButtonR.ctrl_text = ""
        self.ui.pushButtonR.base_operation = CalcOperations.sqrt
        self.ui.pushButtonR.shift_operation = CalcOperations.square
        self.ui.pushButtonR.ctrl_operation = CalcOperations.square
        self.ui.pushButtonR.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonR)

        self.ui.pushButtonT.row = 1
        self.ui.pushButtonT.column = 4.5
        self.ui.pushButtonT.setText("MS")
        self.ui.pushButtonT.original_keyboard_text = "T"
        self.ui.pushButtonT.shift_text = "x³"
        self.ui.pushButtonT.ctrl_text = ""
        self.ui.pushButtonT.base_operation = CalcOperations.MS
        self.ui.pushButtonT.shift_operation = CalcOperations.cube
        self.ui.pushButtonT.ctrl_operation = CalcOperations.cube
        self.ui.pushButtonT.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonT)

        self.ui.pushButtonZ.row = 1
        self.ui.pushButtonZ.column = 5.5
        self.ui.pushButtonZ.setText("M*")
        self.ui.pushButtonZ.original_keyboard_text = "Z"
        self.ui.pushButtonZ.shift_text = "M/"
        self.ui.pushButtonZ.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButtonZ.ctrl_text = "Undo"
        self.ui.pushButtonZ.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonZ.base_operation = CalcOperations.m_multiply
        self.ui.pushButtonZ.shift_operation = CalcOperations.m_division
        self.ui.pushButtonZ.ctrl_operation = CalcOperations.undo
        self.ui.pushButtonZ.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonZ)

    def second_row_keyboard(self):
        self.ui.pushButtonA.row = 2
        self.ui.pushButtonA.column = 1
        self.ui.pushButtonA.setText("AC")
        self.ui.pushButtonA.original_keyboard_text = "A"
        self.ui.pushButtonA.bg_color = self.c_ac_bg_color
        self.ui.pushButtonA.shift_text = ""
        self.ui.pushButtonA.ctrl_text = "Select All"
        self.ui.pushButtonA.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButtonA.base_operation = CalcOperations.AC
        self.ui.pushButtonA.shift_operation = CalcOperations.C
        self.ui.pushButtonA.ctrl_operation = CalcOperations.C
        self.leftside_button_list.append(self.ui.pushButtonA)

        self.ui.pushButtonS.row = 2
        self.ui.pushButtonS.column = 2
        self.ui.pushButtonS.setText("sin")
        self.ui.pushButtonS.original_keyboard_text = "S"
        self.ui.pushButtonS.shift_text = "sin⁻¹"
        self.ui.pushButtonS.ctrl_text = "sinh"
        self.ui.pushButtonS.base_operation = CalcOperations.sin
        self.ui.pushButtonS.shift_operation = CalcOperations.arcsin
        self.ui.pushButtonS.ctrl_operation = CalcOperations.sinh
        self.ui.pushButtonS.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonS)

        self.ui.pushButtonD.row = 2
        self.ui.pushButtonD.column = 3
        self.ui.pushButtonD.setText("cos")
        self.ui.pushButtonD.original_keyboard_text = "D"
        self.ui.pushButtonD.shift_text = "cos⁻¹"
        self.ui.pushButtonD.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButtonD.ctrl_text = "cosh"
        self.ui.pushButtonD.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonD.base_operation = CalcOperations.cos
        self.ui.pushButtonD.shift_operation = CalcOperations.arccos
        self.ui.pushButtonD.ctrl_operation = CalcOperations.cosh
        self.ui.pushButtonD.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonD)

        self.ui.pushButtonF.row = 2
        self.ui.pushButtonF.column = 4
        self.ui.pushButtonF.setText("tan")
        self.ui.pushButtonF.original_keyboard_text = "F"
        self.ui.pushButtonF.shift_text = "tan⁻¹"
        self.ui.pushButtonF.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButtonF.ctrl_text = "tanh"
        self.ui.pushButtonF.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonF.base_operation = CalcOperations.tan
        self.ui.pushButtonF.shift_operation = CalcOperations.arctan
        self.ui.pushButtonF.ctrl_operation = CalcOperations.tanh
        self.ui.pushButtonF.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonF)

        self.ui.pushButtonG.row = 2
        self.ui.pushButtonG.column = 5
        self.ui.pushButtonG.setText("1/x")
        self.ui.pushButtonG.original_keyboard_text = "G"
        self.ui.pushButtonG.shift_text = "R->P"
        self.ui.pushButtonG.ctrl_text = "P->R"
        self.ui.pushButtonG.base_operation = CalcOperations.reciprocal
        self.ui.pushButtonG.shift_operation = CalcOperations.rectangular_to_polar
        self.ui.pushButtonG.ctrl_operation = CalcOperations.polar_to_rectangular
        self.ui.pushButtonG.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonG)

    def third_row_keyboard(self):
        self.ui.pushButtonLess.row = 3
        self.ui.pushButtonLess.column = 0.5
        self.ui.pushButtonLess.setText("<>")
        self.ui.pushButtonLess.original_keyboard_text = "<"
        self.ui.pushButtonLess.shift_text = "X<>M"
        self.ui.pushButtonLess.ctrl_text = ""
        self.ui.pushButtonLess.base_operation = CalcOperations.swap
        self.ui.pushButtonLess.shift_operation = CalcOperations.memory_swap
        self.ui.pushButtonLess.ctrl_operation = CalcOperations.memory_swap
        self.ui.pushButtonLess.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonLess)

        self.ui.pushButtonY.row = 3
        self.ui.pushButtonY.column = 1.5
        self.ui.pushButtonY.setText("ln")
        self.ui.pushButtonY.original_keyboard_text = "Y"
        self.ui.pushButtonY.shift_text = "e^x"
        self.ui.pushButtonY.ctrl_text = "Redo"
        self.ui.pushButtonY.ctrl_font = QFont("Helvetica", 8)
        self.ui.pushButtonY.base_operation = CalcOperations.ln
        self.ui.pushButtonY.shift_operation = CalcOperations.ex
        self.ui.pushButtonY.ctrl_operation = CalcOperations.redo
        self.ui.pushButtonY.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonY)

        self.ui.pushButtonX.row = 3
        self.ui.pushButtonX.column = 2.5
        self.ui.pushButtonX.setText("log")
        self.ui.pushButtonX.original_keyboard_text = "X"
        self.ui.pushButtonX.shift_text = "10^x"
        self.ui.pushButtonX.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButtonX.ctrl_text = "Cut"
        self.ui.pushButtonX.ctrl_font = QFont("Helvetica", 9)
        self.ui.pushButtonX.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonX.base_operation = CalcOperations.log
        self.ui.pushButtonX.shift_operation = CalcOperations.ten_power_10
        self.ui.pushButtonX.ctrl_operation = CalcOperations.cut_to_clipboard
        self.ui.pushButtonX.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonX)

        self.ui.pushButtonC.row = 3
        self.ui.pushButtonC.column = 3.5
        self.ui.pushButtonC.setText("C")
        self.ui.pushButtonC.bg_color = self.c_ac_bg_color
        self.ui.pushButtonC.shift_text = "MS"
        self.ui.pushButtonC.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButtonC.ctrl_text = "Copy"
        self.ui.pushButtonC.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonC.ctrl_font = QFont("Helvetica", 9)
        self.ui.pushButtonC.input_text_edit = self.ui.inputTextEdit
        self.ui.pushButtonC.base_operation = CalcOperations.C
        self.ui.pushButtonC.shift_operation = CalcOperations.MS
        self.ui.pushButtonC.ctrl_operation = CalcOperations.copy_to_clipboard
        self.leftside_button_list.append(self.ui.pushButtonC)

        self.ui.pushButtonV.row = 3
        self.ui.pushButtonV.column = 4.5
        self.ui.pushButtonV.setText("MR")
        self.ui.pushButtonV.original_keyboard_text = "V"
        self.ui.pushButtonV.shift_text = "MR"
        self.ui.pushButtonV.ctrl_text = "Paste"
        self.ui.pushButtonV.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonV.ctrl_font = QFont("Helvetica", 9)
        self.ui.pushButtonV.base_operation = CalcOperations.MR
        self.ui.pushButtonV.shift_operation = CalcOperations.MR
        self.ui.pushButtonV.ctrl_operation = CalcOperations.paste_from_clipboard
        self.ui.pushButtonV.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonV)

        self.ui.pushButtonB.row = 3
        self.ui.pushButtonB.column = 5.5
        self.ui.pushButtonB.setText("Base")
        self.ui.pushButtonB.original_keyboard_text = "B"
        self.ui.pushButtonB.shift_text = "DMS"
        self.ui.pushButtonB.ctrl_text = "DD"
        self.ui.pushButtonB.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonB.base_operation = CalcOperations.convert_to_bases
        self.ui.pushButtonB.shift_operation = CalcOperations.convert_to_dms
        self.ui.pushButtonB.ctrl_operation = CalcOperations.convert_to_dd
        self.ui.pushButtonB.input_text_edit = self.ui.inputTextEdit
        self.leftside_button_list.append(self.ui.pushButtonB)

    def convert_from_binary(self):
        self.ui.inputTextEdit.exec_from_binary()

    def convert_from_octal(self):
        self.ui.inputTextEdit.exec_from_octal()

    def convert_from_decimal(self):
        self.ui.inputTextEdit.exec_from_decimal()

    def convert_from_hexadecimal(self):
        self.ui.inputTextEdit.exec_from_hexadecimal()

    def dms_to_dd(self):
        self.ui.inputTextEdit.exec_convert_to_dd()

    def table_cell_double_clicked(self, row, column):
        item = AppGlobals.table.item(row, column)
        if not item:
            print(f"No item at ({row}, {column})")
            return

        user_data = item.data(Qt.UserRole)
        if user_data is not None:
            self.cell_enter_pressed(row, column)
        else:
            print(f"Cell ({row}, {column}) does NOT have UserRole data.")        

    def arrange_keyboard(self):
        for button in self.leftside_button_list:
            self.button_list.append(button)
            if button.row != -1 and button.column != -1:
                button.move(button.column * AppGlobals.keyboard_grid_width, button.y())
                button.setFixedWidth(button.norm_width * AppGlobals.pushbutton_width)

        for button in self.numpad_button_list:
            self.button_list.append(button)
            if button.row != -1 and button.column != -1:
                offset = AppGlobals.numpad_start_column * AppGlobals.keyboard_grid_width
                button.move(offset + button.column * AppGlobals.numpad_button_width, button.y())
                button.setFixedWidth(button.norm_width * AppGlobals.numpad_button_width)

    def sinh(self):
        self.ui.inputTextEdit.exec_sinh()

    def cosh(self):
        self.ui.inputTextEdit.exec_cosh()

    def tanh(self):
        self.ui.inputTextEdit.exec_tanh()

    def arsinh(self):
        self.ui.inputTextEdit.exec_arsinh()

    def arcosh(self):
        self.ui.inputTextEdit.exec_arcosh()

    def artanh(self):
        self.ui.inputTextEdit.exec_artanh()

    def rectangular_to_polar(self):
        self.ui.inputTextEdit.exec_rectangular_to_polar()

    def polar_to_rectangular(self):
        self.ui.inputTextEdit.exec_polar_to_rectangular()

    def combination(self):
        self.ui.inputTextEdit.exec_combination()

    def permutation(self):
        self.ui.inputTextEdit.exec_permutation()

    def options(self):
        dialog = OptionsDialog(self)
        dialog.ui.timestampCheckBox.setChecked(AppGlobals.timestamp_at_start)

        if dialog.exec():
            AppGlobals.timestamp_at_start = dialog.ui.timestampCheckBox.isChecked()

# main
def main():
    # --- IMPORTANT FOR WINDOWS TASKBAR ICON ---
    # Set a unique Application User Model ID (AppUserModelID)
    # This helps Windows identify your application and display its icon correctly in the taskbar.
    # Choose a unique string for your application, e.g., "YourCompany.YourProduct.SubProduct.Version"
    myappid = 'Kudaschov.ViCalc.Application.4.0' # Example unique ID
    try:
        if sys.platform == 'win32': # Only apply on Windows
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            print("AppUserModelID set successfully.")
    except AttributeError:
        print("Could not set AppUserModelID (likely not Windows or older OS).")

    QCoreApplication.setOrganizationName("Kudaschov")
    QCoreApplication.setApplicationName("ViCalc")

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()