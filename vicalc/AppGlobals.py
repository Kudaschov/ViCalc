import math
from .NumericFormat import NumericFormat
from PySide6.QtCore import QLocale

class AppGlobals:
    angle_unit = None
    numeric_format = NumericFormat.normal
    numeric_precision = 5
    timestamp_at_start = True
    copy_to_clipboard_replace = True
    paste_from_clipboard_replace = True
    input_replace_point = False
    table = None # tableWidget in main window
    input_box = None # inputTextEdit in main window
    current_row = -1 # current row in table
    current_column = -1 # current column in table
    keyboard_grid_width = 58
    pushbutton_width = 59
    numpad_button_width = 52
    right_side_keyboard_visible = False
    numpad_start_column = 7 # if right_side_keyboard_visible: >= 13
    numlock_ac = False
    phy_const_index = 0 # select index in phy const dialog

    # When checked, the angle value will be automatically converted to the new unit when
    # changing between degrees (D), radians (R), or grads (G).
    # If unchecked, only the unit display changes, and the angle value remains the same.    
    convert_angle_on_unit_change = True

    # candidate for options
    different_view_negative_number = True

    # e. g. red color for negative numbers
    # candidate for options
    color_negative_number = "#0000FF" # 

    # comment color
    # candidate for option
    color_comment = "#008F00"

    # last non empty column in last table row for comment in this last row,
    # otherwise comment will be placed on the new row
    # candidate for optrions
    column_number_next_line_comment = 4

    @staticmethod
    def to_format_string(number):
        locale = QLocale()
        locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)
        # todo vk eng format
        match AppGlobals.numeric_format:
            case NumericFormat.general:
                return locale.toString(number, "g", AppGlobals.numeric_precision)
            case NumericFormat.fixed:
                return locale.toString(number, "f", AppGlobals.numeric_precision)
            case NumericFormat.scientific:
                return locale.toString(number, "e", AppGlobals.numeric_precision)
            case NumericFormat.engineering:
                return AppGlobals.format_engineering(number)
            case _:
                return AppGlobals.to_normal_string(number)
            
    @staticmethod
    def to_normal_string(number: float):
        # max precision
        locale = QLocale()
        locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)
        return locale.toString(number, "g", 15)
    
    @staticmethod
    def format_engineering(value):
        if value == 0:
            return "0"

        exponent = int(math.floor(math.log10(abs(value)) // 3 * 3))
        scaled = value / 10 ** exponent

        # Format with locale without group separator
        locale = QLocale()
        locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)

        # Format with max_precision decimal places
        raw_str = locale.toString(scaled, 'f', AppGlobals.numeric_precision)

        # Strip trailing zeros and possibly the decimal point
        if locale.decimalPoint() in raw_str:
            raw_str = raw_str.rstrip('0').rstrip(locale.decimalPoint())

        return f"{raw_str}e{exponent:+03d}"    
    
    @staticmethod
    def non_empty_col_last_row_table():
        row_count = AppGlobals.table.rowCount()
        col_count = AppGlobals.table.columnCount()

        if row_count == 0 or col_count == 0:
            return  -1 # Nothing to do

        last_row = row_count - 1

        # Find last non-empty column in the last row
        last_non_empty_col = -1
        for col in reversed(range(col_count)):
            item = AppGlobals.table.item(last_row, col)
            if item and item.text().strip() != "":
                last_non_empty_col = col
                break

        return last_non_empty_col
