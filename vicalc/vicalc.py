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
from .CommentDialog import CommentDialog
from .CommentCellValue import CommentCellValue
from .key_preselect import KeyPreselect

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
        self.c_ac_bg_color = QColor("#EAEAFF")
        #self.arithmetic_operation_color = QColor("#FEFEFE")
        self.arithmetic_operation_color = QColor("#FAFAFA")
        self.number_key_color = QColor("#FFFFFF")

        AppGlobals.table = self.ui.tableWidget
        AppGlobals.input_box = self.ui.inputTextEdit

        layout = self.ui.verticalLayout
        old_widget = AppGlobals.input_box
        index = layout.indexOf(old_widget)
        layout.removeWidget(old_widget)
        old_widget.deleteLater()

        AppGlobals.input_box = InputTextEdit(self)
        AppGlobals.input_box.setObjectName("inputTextEdit")
        AppGlobals.input_box.setFont(old_widget.font())
        AppGlobals.input_box.setMaximumSize(old_widget.maximumSize())
        AppGlobals.input_box.expressionLabel = self.ui.expressionLabel
        layout.insertWidget(index, AppGlobals.input_box)

        self.ui.action_DEG.triggered.connect(self.mode_deg)
        self.ui.action_RAD.triggered.connect(self.mode_rad)
        self.ui.action_GRA.triggered.connect(self.mode_gra)
        self.ui.action_convert_to_deg.triggered.connect(self.convert_to_deg)
        self.ui.action_convert_to_rad.triggered.connect(self.convert_to_rad)
        self.ui.action_convert_to_gra.triggered.connect(self.convert_to_gra)

        self.ui.action_convert_from_binary.triggered.connect(self.convert_from_binary)
        self.ui.action_convert_from_octal.triggered.connect(self.convert_from_octal)
        self.ui.action_convert_from_decimal.triggered.connect(self.convert_from_decimal)
        self.ui.action_convert_from_hexadecimal.triggered.connect(self.convert_from_hexadecimal)
        self.ui.action_unit_conversion.triggered.connect(self.unit_conversion)

        self.ui.action_dms_to_dd.triggered.connect(self.dms_to_dd)

        self.ui.action_About.triggered.connect(self.show_about_dialog)
        self.ui.action_Help.triggered.connect(self.show_help)
        self.ui.action_numeric_format.triggered.connect(self.numeric_format)

        self.ui.actionInsertDateTime.triggered.connect(self.date_time_stamp)

        self.ui.action_square.triggered.connect(self.square)
        self.ui.action_cube.triggered.connect(self.cube)
        self.ui.action_fourth_power.triggered.connect(self.fourth_power)
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
        self.ui.action_generate_random_number.triggered.connect(AppGlobals.input_box.exec_random)

        self.ui.action_phy_const.triggered.connect(AppGlobals.input_box.exec_phy_const)
        self.ui.action_options.triggered.connect(self.options)

        self.settings = QSettings("Kudaschov", "ViCalc")
        self.read_settings()
        AppGlobals.input_box.setFocus()
        AppGlobals.input_box.selectAll()

        # connect mouse double click on table
        AppGlobals.table.cellDoubleClicked.connect(self.table_cell_double_clicked)

        # context menu
        AppGlobals.table.setContextMenuPolicy(Qt.CustomContextMenu)
        AppGlobals.table.customContextMenuRequested.connect(self.show_context_menu)

        # Define a list to store QPushButton objects
        self.button_list = []
        self.leftside_button_list = [] # for arrange position and size
        self.numpad_button_list = [] # for arrange position and size

        self.ui.pushButtonSpace.row = 4
        self.ui.pushButtonSpace.column = 1
        self.ui.pushButtonSpace.bg_color = self.arithmetic_operation_color

        if AppGlobals.right_side_keyboard_visible:
            self.ui.pushButtonSpace.norm_width = 8.93
        else:
            self.ui.pushButtonSpace.norm_width = 4.94

        self.font_long_names = QFont("Helvetica", 9)
        
        self.ui.pushButtonSpace.setText("=")
        self.ui.pushButtonSpace.shift_text = "Comment"
        self.ui.pushButtonSpace.ctrl_text = "Comment"
        self.ui.pushButtonSpace.base_operation = CalcOperations.calculate
        self.ui.pushButtonSpace.shift_operation = CalcOperations.comment
        self.ui.pushButtonSpace.ctrl_operation = CalcOperations.comment
        self.leftside_button_list.append(self.ui.pushButtonSpace)

        self.numpad_keys()
        self.numbers_row_keyboard()
        self.first_row_keyboard()
        self.second_row_keyboard()
        self.third_row_keyboard()
        self.right_side_keyboard()
        self.arrange_keyboard()
        self.map_to_preselect()

        AppGlobals.input_box.button_list = self.button_list

        #Preselect polling timer
        self.key_preselect = KeyPreselect(self.map_preselect)
        self.preselect_timer = QTimer()
        self.preselect_timer.timeout.connect(self.poll_key_preselect)
        self.preselect_timer.start(50)

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
        AppGlobals.input_box.shiftStatusChanged.connect(self.updateButtonsForShift)
        AppGlobals.input_box.ctrlStatusChanged.connect(self.updateButtonsForCtrl)
        AppGlobals.input_box.focusIn.connect(self.input_box_focus_in)
        AppGlobals.input_box.focusOut.connect(self.change_mode)
        AppGlobals.input_box.memory_changed.connect(self.memory_changed)
        AppGlobals.input_box.statusbar_changed.connect(self.statusbar_changed)
        # --- End custom signal connection ---       

        # Exit-Menüaktion verbinden
        self.ui.actionExit.triggered.connect(self.close)     
        self.ui.actionToggle_Protocol.triggered.connect(self.toggle_protocol)
        self.ui.action_delete_full_protocol.triggered.connect(self.delete_full_protocol)

    def poll_key_preselect(self):
        self.key_preselect.poll_keys()

    def show_context_menu(self, pos):
        global_pos = AppGlobals.table.viewport().mapToGlobal(pos)
        index = AppGlobals.table.indexAt(pos)
        item = AppGlobals.table.itemAt(pos)
        if item:
            menu = QMenu(self)
            action_copy_table_to_clipboard = menu.addAction("Copy")
            action_paste_to_calculator = menu.addAction("Paste to calculator")
            action_clear_cell = menu.addAction("Clear Cell(s)")
            action_delete = menu.addAction("Delete row(s)")
            action = menu.exec(global_pos)
            if action == action_paste_to_calculator:
                self.paste_item_to_calculator(item)
            elif action == action_copy_table_to_clipboard:
                AppGlobals.table.copy_selection_to_clipboard()
            elif action == action_delete:
                self.delete_rows_in_history()
            elif action == action_clear_cell:
                # Create a warning message box
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Warning")
                msg_box.setText("Are you sure you want to clear the cell?")
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg_box.setDefaultButton(QMessageBox.No)

                # Show the message box and get the user's response
                result = msg_box.exec()

                if result == QMessageBox.Yes:
                    AppGlobals.table.setItem(index.row(), index.column(), None)

        elif index.isValid():
            menu = QMenu(self)
            action_add_comment = menu.addAction("Add Comment")
            action = menu.exec(global_pos)
            if action == action_add_comment:
                dialog = CommentDialog()
                dialog.ui.lineEdit.setText("")
                if dialog.exec():
                    comment = dialog.get_comment()
                    CommentCellValue(comment, index.row(), index.column())

    def clear_cell_in_table(self):
        # Create a warning message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText("Are you sure you want to clear the cell?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        # Show the message box and get the user's response
        result = msg_box.exec()

        if result == QMessageBox.Yes:
            for index in AppGlobals.table.selectedIndexes():
                r, c = index.row(), index.column()
                AppGlobals.table.setItem(r, c, None)

    def delete_rows_in_history(self):
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
        msg_box.setText("Are you sure you want to delete full calculation history?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        # Show the message box and get the user's response
        result = msg_box.exec()

        if result == QMessageBox.Yes:
            AppGlobals.table.setRowCount(0)

    def connect_table_signals(self):
        AppGlobals.table.enterPressed.connect(self.cell_enter_pressed)
        AppGlobals.table.escPressed.connect(self.cell_esc_pressed)
        AppGlobals.table.shift_delete_pressed.connect(self.delete_rows_in_history)
        AppGlobals.table.delete_pressed.connect(self.clear_cell_in_table)

    def cell_esc_pressed(self):
        if (self.is_tableWidget_editing() == False):
            # tableWidget is not editing, go in calculator mode
            AppGlobals.input_box.setFocus()
            AppGlobals.input_box.selectAll()

    def cell_enter_pressed(self, row, col):
        if (self.is_tableWidget_editing() == False):
            # tableWidget is not editing, put the current value in inputTextEdit
            item = AppGlobals.table.item(row, col)
            self.paste_item_to_calculator(item)

    def is_tableWidget_editing(self) -> bool:
        # is the tableWidget in edit mode
        current_item = AppGlobals.table.currentItem()
        if current_item:
            return AppGlobals.table.isPersistentEditorOpen(current_item)
        return False         

    def read_settings(self):
        saved_text = self.settings.value("inputText", "")
        try:
            AppGlobals.input_box.setText(saved_text)
            AppGlobals.input_box.trig_mode_init(self.settings.value("trig_mode"))
            AppGlobals.input_box.memory = self.settings.value("memory", type=float)

            AppGlobals.numeric_precision = self.settings.value("numeric_precision", type=int)
            AppGlobals.numeric_format = NumericFormat(self.settings.value("numeric_format"))
            AppGlobals.timestamp_at_start = self.settings.value("timestamp_at_start", True, type=bool)
            AppGlobals.copy_to_clipboard_replace = self.settings.value("copy_to_clipboard_replace", True, type=bool)
            AppGlobals.paste_from_clipboard_replace = self.settings.value("paste_from_clipboard_replace", True, type=bool)
            AppGlobals.input_replace_point = self.settings.value("input_replace_point", False, type=bool)
            AppGlobals.numlock_ac = self.settings.value("numlocK_ac", False, type=bool)
            AppGlobals.convert_angle_on_unit_change = self.settings.value("convert_angle", True, type=bool)
            AppGlobals.phy_const_index = self.settings.value("phy_const_index", 0, type=int)
            AppGlobals.unit_conversion_from = self.settings.value("unit_conversion_from", "in", type=str)
            AppGlobals.unit_conversion_to = self.settings.value("unit_conversion_to", "mm", type=str)

            match AppGlobals.input_box.trig_mode:
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

    def get_key_state(self, key_code):
        return bool(ctypes.windll.user32.GetKeyState(key_code) & 0x0001)

    def get_async_state(self, key_code):
        return bool(ctypes.windll.user32.GetAsyncKeyState(key_code) & 0x8000)         

    def show_about_dialog(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec()

    def numeric_format(self):
        AppGlobals.input_box.exec_numeric_format()

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
        self.settings.setValue("inputText", AppGlobals.input_box.text())
        self.settings.setValue("trig_mode", AppGlobals.input_box.trig_mode.value)
        self.settings.setValue("memory", AppGlobals.input_box.memory)

        self.settings.setValue("numeric_format", AppGlobals.numeric_format.value)
        self.settings.setValue("numeric_precision", AppGlobals.numeric_precision)
        self.settings.setValue("timestamp_at_start", AppGlobals.timestamp_at_start)
        self.settings.setValue("copy_to_clipboard_replace", AppGlobals.copy_to_clipboard_replace)
        self.settings.setValue("paste_from_clipboard_replace", AppGlobals.paste_from_clipboard_replace)
        self.settings.setValue("input_replace_point", AppGlobals.input_replace_point)
        self.settings.setValue("numlocK_ac", AppGlobals.numlock_ac)
        self.settings.setValue("convert_angle", AppGlobals.convert_angle_on_unit_change)
        self.settings.setValue("phy_const_index", AppGlobals.phy_const_index)
        self.settings.setValue("unit_conversion_from", AppGlobals.unit_conversion_from)
        self.settings.setValue("unit_conversion_to", AppGlobals.unit_conversion_to)

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
        if AppGlobals.input_box.memory == 0:
            self.memory_label.setText("")
        else:
            self.memory_label.setText("Memory: " + sMemory)

    def statusbar_changed(self):            
        self.update_numeric_format_label()
        # update memory
        self.memory_changed(AppGlobals.input_box.memory_to_format_string())

    def change_mode(self):
        #print("input_box_focus_out")
        if AppGlobals.table.hasFocus():
            self.mode_label.setStyleSheet(self.status_label_current_stylesheet + "background-color: yellow;")
            self.mode_label.setText("Calculation History")
        else:
            self.mode_label.setText("")

    def input_box_focus_in(self):
        #print("input_box_focus_in")
        if AppGlobals.table.hasFocus():
            self.mode_label.setStyleSheet(self.status_label_current_stylesheet + "background-color: yellow;")
            self.mode_label.setText("Calculation History")
        else:
            self.mode_label.setText("")

    def mode_deg(self):
        AppGlobals.input_box.trig_mode = TrigMode.DEG

    def mode_rad(self):
        AppGlobals.input_box.trig_mode = TrigMode.RAD

    def mode_gra(self):
        AppGlobals.input_box.trig_mode = TrigMode.GRA

    def convert_to_deg(self):
        AppGlobals.input_box.exec_convert_to_deg()

    def convert_to_rad(self):
        AppGlobals.input_box.exec_convert_to_rad()

    def convert_to_gra(self):
        AppGlobals.input_box.exec_convert_to_gra()

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(0, self.after_mainwindow_show)

    def after_mainwindow_show(self):
        self.memory_changed(AppGlobals.input_box.memory_to_format_string())
        self.update_numeric_format_label()
        if AppGlobals.timestamp_at_start:
            self.date_time_stamp()

    def date_time_stamp(self):
        AppGlobals.input_box.exec_date_time_stamp()

    def memory_label_clicked(self):
        AppGlobals.input_box.exec_MR()

    def numeric_format_clicked(self):
        self.numeric_format()

    def toggle_protocol(self):
        AppGlobals.input_box.exec_toggle_table()

    def numpad_keys(self):
        self.ui.pushButton0numpad.row = 4
        self.ui.pushButton0numpad.column = 0
        self.ui.pushButton0numpad.norm_width = 2
        self.ui.pushButton0numpad.bg_color = self.number_key_color
        self.ui.pushButton0numpad.shift_text = ")"
        self.ui.pushButton0numpad.ctrl_text = "<>"
        self.ui.pushButton0numpad.base_operation = CalcOperations.number_0
        self.ui.pushButton0numpad.shift_operation = CalcOperations.closing_bracket
        self.ui.pushButton0numpad.ctrl_operation = CalcOperations.swap
        self.numpad_button_list.append(self.ui.pushButton0numpad)

        self.ui.pushButton1numpad.row = 3
        self.ui.pushButton1numpad.column = 0
        self.ui.pushButton1numpad.bg_color = self.number_key_color
        self.ui.pushButton1numpad.shift_text = "log"
        self.ui.pushButton1numpad.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButton1numpad.ctrl_text = "10^X"
        self.ui.pushButton1numpad.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButton1numpad.base_operation = CalcOperations.number_1
        self.ui.pushButton1numpad.shift_operation = CalcOperations.log
        self.ui.pushButton1numpad.ctrl_operation = CalcOperations.ten_power_x
        self.numpad_button_list.append(self.ui.pushButton1numpad)

        self.ui.pushButton2numpad.row = 3
        self.ui.pushButton2numpad.column = 1
        self.ui.pushButton2numpad.bg_color = self.number_key_color
        self.ui.pushButton2numpad.shift_text = "√"
        self.ui.pushButton2numpad.ctrl_text = "x²"
        self.ui.pushButton2numpad.base_operation = CalcOperations.number_2
        self.ui.pushButton2numpad.shift_operation = CalcOperations.sqrt
        self.ui.pushButton2numpad.ctrl_operation = CalcOperations.square
        self.numpad_button_list.append(self.ui.pushButton2numpad)

        self.ui.pushButton3numpad.row = 3
        self.ui.pushButton3numpad.column = 2
        self.ui.pushButton3numpad.bg_color = self.number_key_color
        self.ui.pushButton3numpad.shift_text = "³√x"
        self.ui.pushButton3numpad.ctrl_text = "x³"
        self.ui.pushButton3numpad.base_operation = CalcOperations.number_3
        self.ui.pushButton3numpad.shift_operation = CalcOperations.cube_root
        self.ui.pushButton3numpad.ctrl_operation = CalcOperations.cube
        self.numpad_button_list.append(self.ui.pushButton3numpad)

        self.ui.pushButton4numpad.row = 2
        self.ui.pushButton4numpad.column = 0
        self.ui.pushButton4numpad.bg_color = self.number_key_color
        self.ui.pushButton4numpad.shift_text = "sin"
        self.ui.pushButton4numpad.ctrl_text = "-1"
        self.ui.pushButton4numpad.base_operation = CalcOperations.number_4
        self.ui.pushButton4numpad.shift_operation = CalcOperations.sin
        self.ui.pushButton4numpad.ctrl_operation = CalcOperations.arcsin
        self.numpad_button_list.append(self.ui.pushButton4numpad)

        self.ui.pushButton5numpad.row = 2
        self.ui.pushButton5numpad.column = 1
        self.ui.pushButton5numpad.bg_color = self.number_key_color
        self.ui.pushButton5numpad.shift_text = "cos"
        self.ui.pushButton5numpad.ctrl_text = "-1"
        self.ui.pushButton5numpad.base_operation = CalcOperations.number_5
        self.ui.pushButton5numpad.shift_operation = CalcOperations.cos
        self.ui.pushButton5numpad.ctrl_operation = CalcOperations.arccos
        self.numpad_button_list.append(self.ui.pushButton5numpad)

        self.ui.pushButton6numpad.row = 2
        self.ui.pushButton6numpad.column = 2
        self.ui.pushButton6numpad.bg_color = self.number_key_color
        self.ui.pushButton6numpad.shift_text = "tan"
        self.ui.pushButton6numpad.ctrl_text = "-1"
        self.ui.pushButton6numpad.base_operation = CalcOperations.number_6
        self.ui.pushButton6numpad.shift_operation = CalcOperations.tan
        self.ui.pushButton6numpad.ctrl_operation = CalcOperations.arctan
        self.numpad_button_list.append(self.ui.pushButton6numpad)

        self.ui.pushButton7numpad.row = 1
        self.ui.pushButton7numpad.column = 0
        self.ui.pushButton7numpad.bg_color = self.number_key_color
        self.ui.pushButton7numpad.shift_text = "ln"
        self.ui.pushButton7numpad.ctrl_text = "e^x"
        self.ui.pushButton7numpad.base_operation = CalcOperations.number_7
        self.ui.pushButton7numpad.shift_operation = CalcOperations.ln
        self.ui.pushButton7numpad.ctrl_operation = CalcOperations.ex
        self.numpad_button_list.append(self.ui.pushButton7numpad)

        self.ui.pushButton8numpad.row = 1
        self.ui.pushButton8numpad.column = 1
        self.ui.pushButton8numpad.bg_color = self.number_key_color
        self.ui.pushButton8numpad.shift_text = "Hist"
        self.ui.pushButton8numpad.ctrl_text = "MS"
        self.ui.pushButton8numpad.base_operation = CalcOperations.number_8
        self.ui.pushButton8numpad.shift_operation = CalcOperations.toggle_table
        self.ui.pushButton8numpad.ctrl_operation = CalcOperations.MS
        self.numpad_button_list.append(self.ui.pushButton8numpad)

        self.ui.pushButton9numpad.row = 1
        self.ui.pushButton9numpad.column = 2
        self.ui.pushButton9numpad.bg_color = self.number_key_color
        self.ui.pushButton9numpad.shift_text = "("
        self.ui.pushButton9numpad.ctrl_text = "MR"
        self.ui.pushButton9numpad.base_operation = CalcOperations.number_9
        self.ui.pushButton9numpad.shift_operation = CalcOperations.opening_bracket
        self.ui.pushButton9numpad.ctrl_operation = CalcOperations.MR
        self.numpad_button_list.append(self.ui.pushButton9numpad)

        self.ui.pushButtonAC.row = 0
        self.ui.pushButtonAC.column = 0
        self.ui.pushButtonAC.setText("AC")
        self.ui.pushButtonAC.bg_color = self.c_ac_bg_color
        self.ui.pushButtonAC.shift_text = "C"
        self.ui.pushButtonAC.ctrl_text = "C"
        self.ui.pushButtonAC.base_operation = CalcOperations.AC
        self.ui.pushButtonAC.shift_operation = CalcOperations.C
        self.ui.pushButtonAC.ctrl_operation = CalcOperations.C
        self.numpad_button_list.append(self.ui.pushButtonAC)

        self.ui.pushButtonBackspace.row = 0
        if AppGlobals.right_side_keyboard_visible:
            self.ui.pushButtonBackspace.column = 12
        else:
            self.ui.pushButtonBackspace.column = 6
        self.ui.pushButtonBackspace.bg_color = self.c_ac_bg_color
        self.ui.pushButtonBackspace.shift_text = "Del Line"
        self.ui.pushButtonBackspace.ctrl_text = "Del Line"
        self.ui.pushButtonBackspace.base_operation = CalcOperations.backspace
        self.ui.pushButtonBackspace.shift_operation = CalcOperations.del_last_line
        self.ui.pushButtonBackspace.ctrl_operation = CalcOperations.del_last_line
        self.leftside_button_list.append(self.ui.pushButtonBackspace)

        self.ui.pushButtonCommaNumpad.row = 4
        self.ui.pushButtonCommaNumpad.column = 2
        self.ui.pushButtonCommaNumpad.bg_color = self.number_key_color
        self.ui.pushButtonCommaNumpad.shift_text = "<-"
        self.ui.pushButtonCommaNumpad.ctrl_text = "DL"
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
        self.numpad_button_list.append(self.ui.pushButtonMinusNumpad)

        self.ui.pushButtonEnter.row = 2
        if AppGlobals.right_side_keyboard_visible:
            self.ui.pushButtonEnter.column = 12
        else:
            self.ui.pushButtonEnter.column = 6
        self.ui.pushButtonEnter.bg_color = self.c_ac_bg_color
        self.ui.pushButtonEnter.shift_text = "Time"
        self.ui.pushButtonEnter.base_operation = CalcOperations.calculate
        self.ui.pushButtonEnter.shift_operation = CalcOperations.date_time_stamp
        self.ui.pushButtonEnter.ctrl_operation = CalcOperations.date_time_stamp
        self.leftside_button_list.append(self.ui.pushButtonEnter)

        self.ui.pushButtonEnterNumpad.row = 2
        self.ui.pushButtonEnterNumpad.column = 3
        self.ui.pushButtonEnterNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonEnterNumpad.shift_text = "%"
        self.ui.pushButtonEnterNumpad.ctrl_text = "Time"
        self.ui.pushButtonEnterNumpad.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonEnterNumpad.base_operation = CalcOperations.calculate
        self.ui.pushButtonEnterNumpad.shift_operation = CalcOperations.percent
        self.ui.pushButtonEnterNumpad.ctrl_operation = CalcOperations.date_time_stamp
        self.numpad_button_list.append(self.ui.pushButtonEnterNumpad)

        self.ui.pushButtonPlusNumpad.row = 1
        self.ui.pushButtonPlusNumpad.column = 3
        self.ui.pushButtonPlusNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonPlusNumpad.shift_text = "M+"
        self.ui.pushButtonPlusNumpad.ctrl_text = "M+"
        self.ui.pushButtonPlusNumpad.base_operation = CalcOperations.Plus
        self.ui.pushButtonPlusNumpad.shift_operation = CalcOperations.M_plus
        self.ui.pushButtonPlusNumpad.ctrl_operation = CalcOperations.M_plus
        self.numpad_button_list.append(self.ui.pushButtonPlusNumpad)

        self.ui.pushButtonMultiplyNumpad.row = 0
        self.ui.pushButtonMultiplyNumpad.column = 2
        self.ui.pushButtonMultiplyNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonMultiplyNumpad.shift_text = "x^y"
        self.ui.pushButtonMultiplyNumpad.ctrl_text = "n!"
        self.ui.pushButtonMultiplyNumpad.base_operation = CalcOperations.Multiply
        self.ui.pushButtonMultiplyNumpad.shift_operation = CalcOperations.pow
        self.ui.pushButtonMultiplyNumpad.ctrl_operation = CalcOperations.factorial
        self.numpad_button_list.append(self.ui.pushButtonMultiplyNumpad)

        self.ui.pushButtonDivisionNumpad.row = 0
        self.ui.pushButtonDivisionNumpad.column = 1
        self.ui.pushButtonDivisionNumpad.bg_color = self.arithmetic_operation_color
        self.ui.pushButtonDivisionNumpad.shift_text = "1/x"
        self.ui.pushButtonDivisionNumpad.ctrl_text = "π"
        self.ui.pushButtonDivisionNumpad.ctrl_font = QFont("Times New Roman", 13)
        self.ui.pushButtonDivisionNumpad.ctrl_highlight_font = QFont("Times New Roman", 13, QFont.Bold)
        self.ui.pushButtonDivisionNumpad.base_operation = CalcOperations.Division
        self.ui.pushButtonDivisionNumpad.shift_operation = CalcOperations.reciprocal
        self.ui.pushButtonDivisionNumpad.ctrl_operation = CalcOperations.pi
        self.numpad_button_list.append(self.ui.pushButtonDivisionNumpad)

    def numbers_row_keyboard(self):
        self.ui.pushButton1.row = 0
        self.ui.pushButton1.column = 0
        self.ui.pushButton1.bg_color = self.number_key_color
        self.ui.pushButton1.shift_text = "n!"
        self.ui.pushButton1.ctrl_text = "RAN#"
        self.ui.pushButton1.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButton1.ctrl_font = self.font_long_names
        self.ui.pushButton1.base_operation = CalcOperations.number_1
        self.ui.pushButton1.shift_operation = CalcOperations.factorial
        self.ui.pushButton1.ctrl_operation = CalcOperations.random
        self.leftside_button_list.append(self.ui.pushButton1)

        self.ui.pushButton2.row = 0
        self.ui.pushButton2.column = 1
        self.ui.pushButton2.bg_color = self.number_key_color
        self.ui.pushButton2.shift_text = "x²"
        self.ui.pushButton2.ctrl_text = "->DEG"
        self.ui.pushButton2.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButton2.ctrl_font = self.font_long_names
        self.ui.pushButton2.base_operation = CalcOperations.number_2
        self.ui.pushButton2.shift_operation = CalcOperations.square
        self.ui.pushButton2.ctrl_operation = CalcOperations.convert_to_deg
        self.leftside_button_list.append(self.ui.pushButton2)

        self.ui.pushButton3.row = 0
        self.ui.pushButton3.column = 2
        self.ui.pushButton3.bg_color = self.number_key_color
        self.ui.pushButton3.shift_text = "x³"
        self.ui.pushButton3.ctrl_text = "->RAD"
        self.ui.pushButton3.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButton3.ctrl_font = self.font_long_names
        self.ui.pushButton3.base_operation = CalcOperations.number_3
        self.ui.pushButton3.shift_operation = CalcOperations.cube
        self.ui.pushButton3.ctrl_operation = CalcOperations.convert_to_rad
        self.leftside_button_list.append(self.ui.pushButton3)

        self.ui.pushButton4.row = 0
        self.ui.pushButton4.column = 3
        self.ui.pushButton4.bg_color = self.number_key_color
        self.ui.pushButton4.shift_text = "x⁴"
        self.ui.pushButton4.ctrl_text = "->GRA"
        self.ui.pushButton4.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButton4.ctrl_font = self.font_long_names
        self.ui.pushButton4.base_operation = CalcOperations.number_4
        self.ui.pushButton4.shift_operation = CalcOperations.fourth_power
        self.ui.pushButton4.ctrl_operation = CalcOperations.convert_to_gra
        self.leftside_button_list.append(self.ui.pushButton4)

        self.ui.pushButton5.row = 0
        self.ui.pushButton5.column = 4
        self.ui.pushButton5.bg_color = self.number_key_color
        self.ui.pushButton5.shift_text = "%"
        self.ui.pushButton5.base_operation = CalcOperations.number_5
        self.ui.pushButton5.shift_operation = CalcOperations.percent
        self.ui.pushButton5.ctrl_operation = CalcOperations.percent
        self.leftside_button_list.append(self.ui.pushButton5)

        self.ui.pushButton6.row = 0
        self.ui.pushButton6.column = 5
        self.ui.pushButton6.bg_color = self.number_key_color
        self.ui.pushButton6.shift_text = "Round"
        self.ui.pushButton6.base_operation = CalcOperations.number_6
        self.ui.pushButton6.shift_operation = CalcOperations.round
        self.ui.pushButton6.ctrl_operation = CalcOperations.round
        self.leftside_button_list.append(self.ui.pushButton6)

    def first_row_keyboard(self):
        self.ui.pushButtonQ.row = 1
        self.ui.pushButtonQ.column = 0.5
        self.ui.pushButtonQ.setText("M+")
        self.ui.pushButtonQ.original_keyboard_text = "Q"
        self.ui.pushButtonQ.shift_text = "M-"
        self.ui.pushButtonQ.ctrl_text = "nCr"
        self.ui.pushButtonQ.base_operation = CalcOperations.M_plus
        self.ui.pushButtonQ.shift_operation = CalcOperations.M_minus
        self.ui.pushButtonQ.ctrl_operation = CalcOperations.combination
        self.leftside_button_list.append(self.ui.pushButtonQ)

        self.ui.pushButtonW.row = 1
        self.ui.pushButtonW.column = 1.5
        self.ui.pushButtonW.setText("x^y")
        self.ui.pushButtonW.original_keyboard_text = "W"
        self.ui.pushButtonW.shift_text = "DD"
        self.ui.pushButtonW.ctrl_text = "nPr"
        self.ui.pushButtonW.base_operation = CalcOperations.pow
        self.ui.pushButtonW.shift_operation = CalcOperations.convert_to_dd
        self.ui.pushButtonW.ctrl_operation = CalcOperations.permutation
        self.leftside_button_list.append(self.ui.pushButtonW)

        self.ui.pushButtonE.row = 1
        self.ui.pushButtonE.column = 2.5
        # special key exponent have other bg color
        self.ui.pushButtonE.bg_color = self.number_key_color
        self.ui.pushButtonE.shift_text = "Hist"
        self.ui.pushButtonE.ctrl_text = "Conv"
        self.ui.pushButtonE.base_operation = CalcOperations.exponent
        self.ui.pushButtonE.shift_operation = CalcOperations.toggle_table
        self.ui.pushButtonE.ctrl_operation = CalcOperations.unit_conversion
        self.leftside_button_list.append(self.ui.pushButtonE)

        self.ui.pushButtonR.row = 1
        self.ui.pushButtonR.column = 3.5
        self.ui.pushButtonR.setText("√")
        self.ui.pushButtonR.original_keyboard_text = "R"
        self.ui.pushButtonR.shift_text = "³√x"
        self.ui.pushButtonR.ctrl_text = "Phy"
        self.ui.pushButtonR.base_operation = CalcOperations.sqrt
        self.ui.pushButtonR.shift_operation = CalcOperations.cube_root
        self.ui.pushButtonR.ctrl_operation = CalcOperations.phy_const
        self.leftside_button_list.append(self.ui.pushButtonR)

        self.ui.pushButtonT.row = 1
        self.ui.pushButtonT.column = 4.5
        self.ui.pushButtonT.setText("tan")
        self.ui.pushButtonT.original_keyboard_text = "T"
        self.ui.pushButtonT.shift_text = "tan⁻¹"
        self.ui.pushButtonT.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButtonT.ctrl_text = "tanh"
        self.ui.pushButtonT.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonT.base_operation = CalcOperations.tan
        self.ui.pushButtonT.shift_operation = CalcOperations.arctan
        self.ui.pushButtonT.ctrl_operation = CalcOperations.tanh
        self.leftside_button_list.append(self.ui.pushButtonT)

        self.ui.pushButtonZ.row = 1
        self.ui.pushButtonZ.column = 5.5
        self.ui.pushButtonZ.setText("M*")
        self.ui.pushButtonZ.original_keyboard_text = "Z"
        self.ui.pushButtonZ.shift_text = "M/"
        self.ui.pushButtonZ.ctrl_text = ""
        self.ui.pushButtonZ.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonZ.base_operation = CalcOperations.m_multiply
        self.ui.pushButtonZ.shift_operation = CalcOperations.m_division
        self.ui.pushButtonZ.ctrl_operation = CalcOperations.undo
        self.leftside_button_list.append(self.ui.pushButtonZ)

    def second_row_keyboard(self):
        self.ui.pushButtonA.row = 2
        self.ui.pushButtonA.column = 1
        self.ui.pushButtonA.setText("AC")
        self.ui.pushButtonA.original_keyboard_text = "A"
        self.ui.pushButtonA.bg_color = self.c_ac_bg_color
        self.ui.pushButtonA.shift_text = "Format"
        self.ui.pushButtonA.ctrl_text = ""
        self.ui.pushButtonA.base_operation = CalcOperations.AC
        self.ui.pushButtonA.shift_operation = CalcOperations.numeric_format
        self.ui.pushButtonA.ctrl_operation = CalcOperations.numeric_format
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
        self.leftside_button_list.append(self.ui.pushButtonD)

        self.ui.pushButtonF.row = 2
        self.ui.pushButtonF.column = 4
        self.ui.pushButtonF.setText("MS")
        self.ui.pushButtonF.original_keyboard_text = "F"
        self.ui.pushButtonF.shift_text = "Dec->"
        self.ui.pushButtonF.shift_font = self.font_long_names
        self.ui.pushButtonF.base_operation = CalcOperations.MS
        self.ui.pushButtonF.shift_operation = CalcOperations.convert_to_bases
        self.ui.pushButtonF.ctrl_operation = CalcOperations.convert_to_bases
        self.leftside_button_list.append(self.ui.pushButtonF)

        self.ui.pushButtonG.row = 2
        self.ui.pushButtonG.column = 5
        self.ui.pushButtonG.setText("log")
        self.ui.pushButtonG.original_keyboard_text = "G"
        self.ui.pushButtonG.shift_text = "10^x"
        self.ui.pushButtonG.ctrl_text = "P->R"
        self.ui.pushButtonG.ctrl_font = self.font_long_names
        self.ui.pushButtonG.base_operation = CalcOperations.log
        self.ui.pushButtonG.shift_operation = CalcOperations.ten_power_x
        self.ui.pushButtonG.ctrl_operation = CalcOperations.polar_to_rectangular
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
        self.leftside_button_list.append(self.ui.pushButtonLess)

        self.ui.pushButtonY.row = 3
        self.ui.pushButtonY.column = 1.5
        self.ui.pushButtonY.text_highlight_font = QFont("Times New Roman", 14, QFont.Bold)
        self.ui.pushButtonY.text_font = QFont("Times New Roman", 14)
        self.ui.pushButtonY.setText("π")
        self.ui.pushButtonY.original_keyboard_text = "Y"
        self.ui.pushButtonY.shift_text = "DMS"
        self.ui.pushButtonY.ctrl_text = ""
        self.ui.pushButtonY.base_operation = CalcOperations.pi
        self.ui.pushButtonY.shift_operation = CalcOperations.convert_to_dms
        self.ui.pushButtonY.ctrl_operation = CalcOperations.convert_to_dms
        self.leftside_button_list.append(self.ui.pushButtonY)

        self.ui.pushButtonX.row = 3
        self.ui.pushButtonX.column = 2.5
        self.ui.pushButtonX.setText("1/x")
        self.ui.pushButtonX.original_keyboard_text = "X"
        self.ui.pushButtonX.shift_text = "Bin->"
        self.ui.pushButtonX.ctrl_text = ""
        self.ui.pushButtonX.ctrl_font = self.font_long_names
        self.ui.pushButtonX.base_operation = CalcOperations.reciprocal
        self.ui.pushButtonX.shift_operation = CalcOperations.convert_from_binary
        self.ui.pushButtonX.ctrl_operation = CalcOperations.convert_from_binary
        self.leftside_button_list.append(self.ui.pushButtonX)

        self.ui.pushButtonC.row = 3
        self.ui.pushButtonC.column = 3.5
        self.ui.pushButtonC.setText("C")
        self.ui.pushButtonC.bg_color = self.c_ac_bg_color
        self.ui.pushButtonC.shift_text = "Oct->"
        self.ui.pushButtonC.shift_font = self.font_long_names
        self.ui.pushButtonC.ctrl_text = ""
        self.ui.pushButtonC.ctrl_font = self.font_long_names
        self.ui.pushButtonC.base_operation = CalcOperations.C
        self.ui.pushButtonC.shift_operation = CalcOperations.convert_from_octal
        self.ui.pushButtonC.ctrl_operation = CalcOperations.convert_from_octal
        self.leftside_button_list.append(self.ui.pushButtonC)

        self.ui.pushButtonV.row = 3
        self.ui.pushButtonV.column = 4.5
        self.ui.pushButtonV.setText("MR")
        self.ui.pushButtonV.original_keyboard_text = "V"
        self.ui.pushButtonV.shift_text = "Hex->"
#        self.ui.pushButtonV.shift_text_alignment = Qt.AlignLeft
        self.ui.pushButtonV.shift_font = self.font_long_names
        self.ui.pushButtonV.ctrl_text = ""
#        self.ui.pushButtonV.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonV.ctrl_font = self.font_long_names
        self.ui.pushButtonV.base_operation = CalcOperations.MR
        self.ui.pushButtonV.shift_operation = CalcOperations.convert_from_hexadecimal
        self.ui.pushButtonV.ctrl_operation = CalcOperations.paste_from_clipboard
        self.leftside_button_list.append(self.ui.pushButtonV)

        self.ui.pushButtonB.row = 3
        self.ui.pushButtonB.column = 5.5
        self.ui.pushButtonB.setText("ln")
        self.ui.pushButtonB.original_keyboard_text = "B"
        self.ui.pushButtonB.shift_text = "e^x"
        self.ui.pushButtonB.ctrl_text = "R->P"
        self.ui.pushButtonB.ctrl_font = self.font_long_names
        self.ui.pushButtonB.ctrl_text_alignment = Qt.AlignRight
        self.ui.pushButtonB.base_operation = CalcOperations.ln
        self.ui.pushButtonB.shift_operation = CalcOperations.ex
        self.ui.pushButtonB.ctrl_operation = CalcOperations.rectangular_to_polar
        self.leftside_button_list.append(self.ui.pushButtonB)

    def convert_from_binary(self):
        AppGlobals.input_box.exec_from_binary()

    def convert_from_octal(self):
        AppGlobals.input_box.exec_from_octal()

    def convert_from_decimal(self):
        AppGlobals.input_box.exec_from_decimal()

    def convert_from_hexadecimal(self):
        AppGlobals.input_box.exec_from_hexadecimal()

    def unit_conversion(self):
        AppGlobals.input_box.exec_unit_conversion()

    def dms_to_dd(self):
        AppGlobals.input_box.exec_convert_to_dd()

    def table_cell_double_clicked(self, row, column):

        item = AppGlobals.table.item(row, column)
        self.paste_item_to_calculator(item)

    def paste_item_to_calculator(self, item):
        if not item:
            return
        
        val = item.data(Qt.UserRole)
        str = item.data(Qt.DisplayRole)
        if val:
            if isinstance(val, NumericCellValue):
                AppGlobals.input_box.setText(AppGlobals.to_normal_string(val.value()))
            else:
                AppGlobals.input_box.setText(str)
        else:
            AppGlobals.input_box.setText(item.text())
        AppGlobals.input_box.setFocus()
        AppGlobals.input_box.selectAll()    

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

        # for debug
        if False:
            self.check_double_operations()

    def map_to_preselect(self):
        self.map_preselect = {
            30: self.ui.pushButton1, 31: self.ui.pushButton2, 32: self.ui.pushButton3, 33: self.ui.pushButton4,
            34: self.ui.pushButton5, 35: self.ui.pushButton6, 42: self.ui.pushButtonBackspace,
            20: self.ui.pushButtonQ, 26: self.ui.pushButtonW, 8: self.ui.pushButtonE, 21: self.ui.pushButtonR, 23: self.ui.pushButtonT, 28: self.ui.pushButtonZ,
            4: self.ui.pushButtonA, 22: self.ui.pushButtonS, 7: self.ui.pushButtonD, 9: self.ui.pushButtonF, 10: self.ui.pushButtonG, 40: self.ui.pushButtonEnter,
            100: self.ui.pushButtonLess, 29: self.ui.pushButtonY, 27: self.ui.pushButtonX, 6: self.ui.pushButtonC, 25: self.ui.pushButtonV, 5: self.ui.pushButtonB,
            44: self.ui.pushButtonSpace,

            84: self.ui.pushButtonDivisionNumpad, 85: self.ui.pushButtonMultiplyNumpad, 86: self.ui.pushButtonMinusNumpad,
            95: self.ui.pushButton7numpad, 96: self.ui.pushButton8numpad, 97: self.ui.pushButton9numpad, 87: self.ui.pushButtonPlusNumpad,
            92: self.ui.pushButton4numpad, 93: self.ui.pushButton5numpad, 94: self.ui.pushButton6numpad,
            89: self.ui.pushButton1numpad, 90: self.ui.pushButton2numpad, 91: self.ui.pushButton3numpad, 88: self.ui.pushButtonEnterNumpad,
            98: self.ui.pushButton0numpad, 99: self.ui.pushButtonCommaNumpad
        }

    def sinh(self):
        AppGlobals.input_box.exec_sinh()

    def cosh(self):
        AppGlobals.input_box.exec_cosh()

    def tanh(self):
        AppGlobals.input_box.exec_tanh()

    def arsinh(self):
        AppGlobals.input_box.exec_arsinh()

    def arcosh(self):
        AppGlobals.input_box.exec_arcosh()

    def artanh(self):
        AppGlobals.input_box.exec_artanh()

    def rectangular_to_polar(self):
        AppGlobals.input_box.exec_rectangular_to_polar()

    def polar_to_rectangular(self):
        AppGlobals.input_box.exec_polar_to_rectangular()

    def combination(self):
        AppGlobals.input_box.exec_combination()

    def permutation(self):
        AppGlobals.input_box.exec_permutation()

    def options(self):
        dialog = OptionsDialog(self)
        dialog.ui.timestampCheckBox.setChecked(AppGlobals.timestamp_at_start)
        dialog.ui.copyCheckBox.setChecked(AppGlobals.copy_to_clipboard_replace)
        dialog.ui.pasteCheckBox.setChecked(AppGlobals.paste_from_clipboard_replace)
        dialog.ui.inputReplacePointcheckBox.setChecked(AppGlobals.input_replace_point)
        dialog.ui.NumlockACcheckBox.setChecked(AppGlobals.numlock_ac)
        dialog.ui.convertAngleCheckBox.setChecked(AppGlobals.convert_angle_on_unit_change)

        if dialog.exec():
            AppGlobals.timestamp_at_start = dialog.ui.timestampCheckBox.isChecked()
            AppGlobals.copy_to_clipboard_replace = dialog.ui.copyCheckBox.isChecked()
            AppGlobals.paste_from_clipboard_replace = dialog.ui.pasteCheckBox.isChecked()
            AppGlobals.input_replace_point = dialog.ui.inputReplacePointcheckBox.isChecked()
            AppGlobals.numlock_ac = dialog.ui.NumlockACcheckBox.isChecked()
            AppGlobals.convert_angle_on_unit_change = dialog.ui.convertAngleCheckBox.isChecked()

    def square(self):
        AppGlobals.input_box.exec_square()

    def cube(self):
        AppGlobals.input_box.exec_cube()

    def fourth_power(self):
        AppGlobals.input_box.exec_fourth_power()

    def right_side_keyboard(self):
        self.numbers_row_right_side()
        self.first_row_right_side()
        self.second_row_right_side()
        self.third_row_right_side()

    def numbers_row_right_side(self):
        self.ui.pushButton7.row = 0
        self.ui.pushButton7.column = 6
        self.ui.pushButton7.bg_color = self.number_key_color
        self.ui.pushButton7.shift_text = "/"
        self.ui.pushButton7.base_operation = CalcOperations.number_7
        self.ui.pushButton7.shift_operation = CalcOperations.Division
        self.ui.pushButton7.ctrl_operation = CalcOperations.Division
        self.add_to_rightside_list(self.ui.pushButton7)

        self.ui.pushButton8.row = 0
        self.ui.pushButton8.column = 7
        self.ui.pushButton8.bg_color = self.number_key_color
        self.ui.pushButton8.shift_text = "("
        self.ui.pushButton8.base_operation = CalcOperations.number_8
        self.ui.pushButton8.shift_operation = CalcOperations.opening_bracket
        self.ui.pushButton8.ctrl_operation = CalcOperations.opening_bracket
        self.add_to_rightside_list(self.ui.pushButton8)

        self.ui.pushButton9.row = 0
        self.ui.pushButton9.column = 8
        self.ui.pushButton9.bg_color = self.number_key_color
        self.ui.pushButton9.shift_text = ")"
        self.ui.pushButton9.base_operation = CalcOperations.number_9
        self.ui.pushButton9.shift_operation = CalcOperations.closing_bracket
        self.ui.pushButton9.ctrl_operation = CalcOperations.closing_bracket
        self.add_to_rightside_list(self.ui.pushButton9)

        self.ui.pushButton0.row = 0
        self.ui.pushButton0.column = 9
        self.ui.pushButton0.bg_color = self.number_key_color
        self.ui.pushButton0.shift_text = "="
        self.ui.pushButton0.base_operation = CalcOperations.number_0
        self.ui.pushButton0.shift_operation = CalcOperations.calculate
        self.ui.pushButton0.ctrl_operation = CalcOperations.calculate
        self.add_to_rightside_list(self.ui.pushButton0)

        self.ui.pushButtonSsharp.row = 0
        self.ui.pushButtonSsharp.column = 10
        self.ui.pushButtonSsharp.setText("")
        self.ui.pushButtonSsharp.original_keyboard_text = "ß"
        self.ui.pushButtonSsharp.shift_text = ""
        self.add_to_rightside_list(self.ui.pushButtonSsharp)
        
        self.ui.pushButtonAcute.row = 0
        self.ui.pushButtonAcute.column = 11
        self.ui.pushButtonAcute.setText("")
        self.ui.pushButtonAcute.original_keyboard_text = "´"
        self.ui.pushButtonAcute.shift_text = ""
        self.add_to_rightside_list(self.ui.pushButtonAcute)

    def first_row_right_side(self):
        self.ui.pushButtonU.row = 1
        self.ui.pushButtonU.column = 6.5
        self.ui.pushButtonU.setText("")
        self.ui.pushButtonU.original_keyboard_text = "U"
        self.add_to_rightside_list(self.ui.pushButtonU)

        self.ui.pushButtonI.row = 1
        self.ui.pushButtonI.column = 7.5
        self.ui.pushButtonI.setText("")
        self.ui.pushButtonI.original_keyboard_text = "I"
        self.add_to_rightside_list(self.ui.pushButtonI)

        self.ui.pushButtonO.row = 1
        self.ui.pushButtonO.column = 8.5
        self.ui.pushButtonO.setText("")
        self.ui.pushButtonO.original_keyboard_text = "O"
        self.add_to_rightside_list(self.ui.pushButtonO)

        self.ui.pushButtonP.row = 1
        self.ui.pushButtonP.column = 9.5
        self.ui.pushButtonP.setText("")
        self.ui.pushButtonP.original_keyboard_text = "P"
        self.add_to_rightside_list(self.ui.pushButtonP)

        self.ui.pushButtonUdiaeresis.row = 1
        self.ui.pushButtonUdiaeresis.column = 10.5
        self.ui.pushButtonUdiaeresis.setText("")
        self.ui.pushButtonUdiaeresis.original_keyboard_text = "Ü"
        self.add_to_rightside_list(self.ui.pushButtonUdiaeresis)

        self.ui.pushButtonPlus.row = 1
        self.ui.pushButtonPlus.column = 11.5
        self.ui.pushButtonPlus.setText("+")
        self.ui.pushButtonPlus.shift_text = "*"
        self.ui.pushButtonPlus.ctrl_text = "*"
        self.ui.pushButtonPlus.base_operation = CalcOperations.Plus
        self.ui.pushButtonPlus.shift_operation = CalcOperations.Multiply
        self.ui.pushButtonPlus.ctrl_operation = CalcOperations.Multiply
        self.add_to_rightside_list(self.ui.pushButtonPlus)

    def second_row_right_side(self):
        self.ui.pushButtonH.row = 2
        self.ui.pushButtonH.column = 6
        self.ui.pushButtonH.setText("")
        self.ui.pushButtonH.original_keyboard_text = "H"
        self.add_to_rightside_list(self.ui.pushButtonH)

        self.ui.pushButtonJ.row = 2
        self.ui.pushButtonJ.column = 7
        self.ui.pushButtonJ.setText("")
        self.ui.pushButtonJ.original_keyboard_text = "J"
        self.add_to_rightside_list(self.ui.pushButtonJ)

        self.ui.pushButtonK.row = 2
        self.ui.pushButtonK.column = 8
        self.ui.pushButtonK.setText("")
        self.ui.pushButtonK.original_keyboard_text = "K"
        self.add_to_rightside_list(self.ui.pushButtonK)

        self.ui.pushButtonL.row = 2
        self.ui.pushButtonL.column = 9
        self.ui.pushButtonL.setText("")
        self.ui.pushButtonL.original_keyboard_text = "L"
        self.add_to_rightside_list(self.ui.pushButtonL)

        self.ui.pushButtonOdiaeresis.row = 2
        self.ui.pushButtonOdiaeresis.column = 10
        self.ui.pushButtonOdiaeresis.setText("")
        self.ui.pushButtonOdiaeresis.original_keyboard_text = "Ö"
        self.add_to_rightside_list(self.ui.pushButtonOdiaeresis)
        
        self.ui.pushButtonAdiaeresis.row = 2
        self.ui.pushButtonAdiaeresis.column = 11
        self.ui.pushButtonAdiaeresis.setText("")
        self.ui.pushButtonAdiaeresis.original_keyboard_text = "Ä"
        self.add_to_rightside_list(self.ui.pushButtonAdiaeresis)

    def third_row_right_side(self):
        self.ui.pushButtonN.row = 3
        self.ui.pushButtonN.column = 6.5
        self.ui.pushButtonN.setText("")
        self.ui.pushButtonN.original_keyboard_text = "N"
        self.add_to_rightside_list(self.ui.pushButtonN)

        self.ui.pushButtonM.row = 3
        self.ui.pushButtonM.column = 7.5
        self.ui.pushButtonM.setText("")
        self.ui.pushButtonM.original_keyboard_text = "M"
        self.add_to_rightside_list(self.ui.pushButtonM)

        self.ui.pushButtonComma.row = 3
        self.ui.pushButtonComma.column = 8.5
        self.ui.pushButtonComma.setText(",")
        self.ui.pushButtonComma.base_operation = CalcOperations.comma
        self.ui.pushButtonComma.shift_operation = CalcOperations.comma
        self.ui.pushButtonComma.ctrl_operation = CalcOperations.comma
        self.add_to_rightside_list(self.ui.pushButtonComma)

        self.ui.pushButtonPeriod.row = 3
        self.ui.pushButtonPeriod.column = 9.5
        self.ui.pushButtonPeriod.setText("")
        self.ui.pushButtonPeriod.original_keyboard_text = "."
        self.add_to_rightside_list(self.ui.pushButtonPeriod)

        self.ui.pushButtonMinus.row = 3
        self.ui.pushButtonMinus.column = 10.5
        self.ui.pushButtonMinus.setText("-")
        self.ui.pushButtonMinus.shift_text = "(-)"
        self.ui.pushButtonMinus.ctrl_text = "(-)"
        self.ui.pushButtonMinus.original_keyboard_text = "."
        self.ui.pushButtonMinus.base_operation = CalcOperations.Minus
        self.ui.pushButtonMinus.shift_operation = CalcOperations.SignChange
        self.ui.pushButtonMinus.ctrl_operation = CalcOperations.SignChange
        self.add_to_rightside_list(self.ui.pushButtonMinus)

    def add_to_rightside_list(self, key_button):
        if AppGlobals.right_side_keyboard_visible:
            self.leftside_button_list.append(key_button)
        else:
            key_button.hide()

    def check_double_operations(self):
        # for debugging
        operations = []

        for button in self.leftside_button_list:
            if button.base_operation in operations:
                print(f"Duplicate found in base operation: {button.text()}, {button.base_operation}")
            else:
                operations.append(button.base_operation)

            if button.shift_operation in operations:
                print(f"Duplicate found in shift operation: {button.text()}, {button.shift_operation}")
            else:
                operations.append(button.shift_operation)

            if button.ctrl_operation in operations:
                print(f"Duplication found in ctrl operations: {button.text()}, {button.ctrl_operation}")
            else:
                operations.append(button.ctrl_operation)

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