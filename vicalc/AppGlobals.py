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
    input_replace_decimal_separator = False
    table = None # tableWidget in main window
    input_box = None # inputTextEdit in main window
    current_row = -1 # current row in table
    current_column = -1 # current column in table
    keyboard_grid_width = 58
    pushbutton_width = 59
    numpad_button_width = 52
    keyboard_grid_height = 48
    pushbutton_height = 48
    numpad_enter_height = 96
    right_side_keyboard_visible = False
    numpad_start_column = 7 # if right_side_keyboard_visible: >= 13
    numlock_ac = False
    phy_const_index = 0 # select index in phy const dialog
    unit_conversion_from = "in"
    unit_conversion_to = "mm"

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

    # persistent values for ratio calculation dialog
    ratio_c_a = 1.0
    ratio_c_b = 2.0
    ratio_c_d = 4.0

    ratio_d_a = 5.0
    ratio_d_b = 6.0
    ratio_d_c = 7.0

    linear_x0: float = 1.0
    linear_y0: float = 2.0
    linear_x1: float = 3.0
    linear_y1: float = 4.0
    linear_a: float = 5.0
    linear_b: float = 6.0

    quadratic_a: float = 1.0
    quadratic_b: float = -3.0
    quadratic_c: float = 2.0

    # Linear System of Equations with 2 equations and 2 unknowns
    lse_a1: float = 1.0
    lse_b1: float = 2.0
    lse_a2: float = 3.0
    lse_b2: float = 4.0
    lse_c1: float = 5.0
    lse_c2: float = 6.0

    @staticmethod
    def to_format_string(number):
        locale = QLocale(QLocale.C)
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
        locale = QLocale(QLocale.C)
        locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)
        return locale.toString(number, "g", 15)
    
    @staticmethod
    def format_engineering(value):
        if value == 0:
            return "0"

        exponent = int(math.floor(math.log10(abs(value)) // 3 * 3))
        scaled = value / 10 ** exponent

        # Format with locale without group separator
        locale = QLocale(QLocale.C)
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
    
    @staticmethod
    def toDouble(text: str):
        return QLocale(QLocale.Language.C).toDouble(text)

    #Discriminant for quadratic equation ax^2 + bx + c = 0
    @staticmethod
    def discriminant(a: float, b: float, c: float):
        return b ** 2 - 4 * a * c
    
    # Discriminant for linear system of equations a1*x + b1*y = c1 and a2*x + b2*y = c2
    @staticmethod
    def lse_discriminant(a1: float, b1: float, a2: float, b2: float):
        return a1 * b2 - b1 * a2