import math, cmath
import ctypes
from .NumberBase import NumberBase
from .WordSize import WordSize
from .NumericFormat import NumericFormat
from PySide6.QtCore import QLocale
from .CalcMode import CalcMode
from .ComplexNumberForm import ComplexNumberForm
from .ShiftRotateOperation import ShiftRotateOperation
from .TrigMode import TrigMode

class AppGlobals:
# Base color mapping stored globally
    BASE_COLORS = {
        NumberBase.DEC: "#E8F0FE",  # Soft Blue
        NumberBase.HEX: "#E0F7FA",  # Soft Cyan
        NumberBase.OCT: "#E6F4EA",  # Soft Green
        NumberBase.BIN: "#FEF7E0",  # Soft Yellow
    }    

    locale = None
    root_expression = None
    expressionLabel = None
    angle_unit = None
    calc_mode = CalcMode.scientific
    current_word_size = WordSize.BIT8
    number_base = NumberBase.DEC
    bitwise_shift = ShiftRotateOperation.arithmetic
    carry_flag = 0 # carry bit for RoLC/RoRC operations
    base_n_signed = True # DEC Values in Base-N mode will be handled w/o sign
    complex_number_form = ComplexNumberForm.rectangular
    numeric_format = NumericFormat.normal
    numeric_precision = 5
    timestamp_at_start = True
    copy_to_clipboard_replace = True
    paste_from_clipboard_replace = True
    input_replace_decimal_separator = False
    # Double shift turn it to True. Keybord stay in shift pressed status.
    # It makes possible to use shift function without holding shift key.
    shift_hold = False
    ctrl_hold = False
    ctrl_shift_hold = False
    # Show number in status bar in binary, octal, and hexadecimal format when the number is an integer.
    show_binary_value = False
    show_octal_value = False
    show_decimal_value = False
    show_hex_value = False
    show_word_size = False
    history = None # history TextBrowser in main window
    history_string_font_size = 11
    history_number_font_size = 11
    input_box = None # inputTextEdit in main window
    input_imag_box = None # inputImagTextEdit, imaginary part of complex number
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
    color_negative_number = "#FF0000" # 

    # comment color
    # candidate for option
    color_comment = "#008F00"

    # last non empty column in last table row for comment in this last row,
    # otherwise comment will be placed on the new row
    # candidate for optrions
    column_number_next_line_comment = 4

    trig_mode = TrigMode.DEG


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

    # arbitrary log base for log calculations
    log_base: float = 10.0

    memory_status_bar_text = "Memory: "

    @staticmethod
    def to_format_string(number: float | complex, local_number_base: NumberBase = None):
        AppGlobals.locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)
        if (AppGlobals.calc_mode == CalcMode.base_n or local_number_base)and number.is_integer():
            lnb = AppGlobals.number_base
            if local_number_base:
                lnb = local_number_base
            match lnb:
                case NumberBase.BIN:
                    return AppGlobals.to_nibble_bin(AppGlobals.mask_value(int(number)))
                case NumberBase.OCT:
                    return oct(AppGlobals.mask_value(int(number)))
                case NumberBase.HEX:
                    return AppGlobals.int_to_hex_with_prefix(AppGlobals.mask_value(int(number)))
                case _:
                    return str(int(number))
        elif AppGlobals.is_complex(number):
            return AppGlobals.complex_number_to_format_string(number)
        else:
            float_number = float(number)
            match AppGlobals.numeric_format:
                case NumericFormat.general:
                    return AppGlobals.locale.toString(float_number, "g", AppGlobals.numeric_precision)
                case NumericFormat.fixed:
                    return AppGlobals.locale.toString(float_number, "f", AppGlobals.numeric_precision)
                case NumericFormat.scientific:
                    return AppGlobals.locale.toString(float_number, "e", AppGlobals.numeric_precision)
                case NumericFormat.engineering:
                    return AppGlobals.format_engineering(float_number)
                case _:
                    return AppGlobals.to_normal_string(float_number)
            
    @staticmethod
    def to_normal_string(number: float):
        # max precision
        AppGlobals.locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)
        if (AppGlobals.calc_mode == CalcMode.base_n) and number.is_integer():
            int_number = int(number)
            match AppGlobals.number_base:
                case NumberBase.BIN:
                    return f"{(int_number & AppGlobals.current_word_size.mask):0{AppGlobals.current_word_size.bits}b}"
                case NumberBase.OCT:
                    return f"{int_number:o}"
                case NumberBase.HEX:
                    return f"{int_number & AppGlobals.current_word_size.mask:X}"
                case _:
                    return f"{int_number}"
        else:
            return AppGlobals.locale.toString(float(number), "g", 16)
    
    @staticmethod
    def format_engineering(value):
        if value == 0:
            return "0"

        exponent = int(math.floor(math.log10(abs(value)) // 3 * 3))
        scaled = value / 10 ** exponent

        # Format with locale without group separator
        AppGlobals.locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)

        # Format with max_precision decimal places
        raw_str = AppGlobals.locale.toString(scaled, 'f', AppGlobals.numeric_precision)

        # Strip trailing zeros and possibly the decimal point
        if AppGlobals.locale.decimalPoint() in raw_str:
            raw_str = raw_str.rstrip('0').rstrip(AppGlobals.locale.decimalPoint())

        return f"{raw_str}e{exponent:+03d}"    
    
   
    @staticmethod
    def toDouble(text: str):
        return AppGlobals.locale.toDouble(text)

    #Discriminant for quadratic equation ax^2 + bx + c = 0
    @staticmethod
    def discriminant(a: float, b: float, c: float):
        return b ** 2 - 4 * a * c
    
    # Discriminant for linear system of equations a1*x + b1*y = c1 and a2*x + b2*y = c2
    @staticmethod
    def lse_discriminant(a1: float, b1: float, a2: float, b2: float):
        return a1 * b2 - b1 * a2
    
    @staticmethod
    def log_base_calculation(number: float, base: float) -> float:
        if base <= 0.0 or base == 1.0:
            raise ValueError("Log base must be positive and not equal to 1.")
        if number <= 0.0:
            raise ValueError("Number must be positive for logarithm.")
        return math.log(number) / math.log(base)
    
    @staticmethod
    def awg_to_diameter_inch_calculation(awg: float) -> float:
        # AWG to diameter in inches conversion using the formula: d = 0.005 * 92^((36 - AWG) / 39)
        diameter_inch = 0.005 * (92 ** ((36 - awg) / 39))
        return diameter_inch
    
    @staticmethod
    def awg_to_diameter_mm_calculation(awg: float) -> float:
        # AWG to diameter in mm conversion using the formula: d = 0.127 * 92^((36 - AWG) / 39)
        diameter_mm = 0.127 * (92 ** ((36 - awg) / 39))
        return diameter_mm
    
    @staticmethod
    def awg_to_kcmil_calculation(awg: float) -> float:
        # AWG to kcmil conversion using the formula: A = (π/4) * (d^2), where d is the diameter in inches
        diameter_inch = AppGlobals.awg_to_diameter_inch_calculation(awg)
        area_kcmil = (diameter_inch ** 2) * 1000
        return area_kcmil

    @staticmethod
    def awg_to_mm2_calculation(awg: float) -> float:
        # AWG to mm^2 conversion using the formula: A = (π/4) * (d^2), where d is the diameter in mm
        diameter_mm = AppGlobals.awg_to_diameter_mm_calculation(awg)
        area_mm2 = (math.pi / 4) * (diameter_mm ** 2)
        return area_mm2
    
    @staticmethod
    def mm2_to_awg_calculation(mm2: float) -> float:
        # mm^2 to AWG conversion using the formula: AWG = 36 - 39 * log10(d / 0.127), where d is the diameter in mm
        diameter_mm = AppGlobals.mm2_to_diameter_mm_calculation(mm2)
        awg = 36 - 39 * AppGlobals.log_base_calculation(diameter_mm / 0.127, 92)
        return awg
    
    @staticmethod
    def mm2_to_diameter_inch_calculation(mm2: float) -> float:
        # mm^2 to diameter in inches conversion using the formula: d = 0.127 * 92^((36 - AWG) / 39)
        diameter_mm = AppGlobals.mm2_to_diameter_mm_calculation(mm2)
        diameter_inch = diameter_mm / 25.4
        return diameter_inch
    
    @staticmethod
    def mm2_to_diameter_mm_calculation(mm2: float) -> float:
        # mm^2 to diameter in mm conversion using the formula: d = 0.127 * 92^((36 - AWG) / 39)
        diameter_mm = math.sqrt((4 * mm2) / math.pi)
        return diameter_mm
    
    @staticmethod
    def mm2_to_kcmil_calculation(mm2: float) -> float:
        # mm^2 to kcmil conversion using the formula: A = (π/4) * (d^2), where d is the diameter in inches
        diameter_mm = math.sqrt((4 * mm2) / math.pi)
        diameter_inch = diameter_mm / 25.4
        area_kcmil = (diameter_inch ** 2) * 1000
        return area_kcmil

    @staticmethod
    def parse_base_str(s_temp: str, base: NumberBase) -> tuple[int, bool]:
        radix_map = {
            NumberBase.BIN: 2,
            NumberBase.OCT: 8,
            NumberBase.DEC: 10,
            NumberBase.HEX: 16,
        }
        try:
            number_temp = int(s_temp.strip(), radix_map[base])
            return number_temp, True  # (Wert, convert_ok)
        except ValueError:
            return 0, False  # Konvertierung fehlgeschlagen

    @staticmethod
    def to_number(s_temp: str) -> tuple[float, bool]:
        if AppGlobals.calc_mode == CalcMode.base_n:
            match AppGlobals.number_base:
                case NumberBase.DEC:
                    # try to convert to int
                    number_temp, convert_ok = AppGlobals.parse_base_str(s_temp, AppGlobals.number_base)
                    # otherwise try to convert to float
                    if not convert_ok:
                        number_temp, convert_ok = AppGlobals.locale.toDouble(s_temp)
                case _:
                    number_temp, convert_ok = AppGlobals.parse_base_str(s_temp, AppGlobals.number_base)
        else:
            number_temp, convert_ok = AppGlobals.locale.toDouble(s_temp)

        return number_temp, convert_ok

    @staticmethod
    def uint_to_signed_int(val: int) -> tuple[int, bool]:
        """Converts an unsigned integer to a signed integer using two's complement.

        Args:
            val: The integer value to convert (e.g., 0b11111011 or 251).

        Returns:
            A tuple of (converted_value, is_signed), where is_signed is True
            if the sign bit (MSB) was set and the value is negative.
        """
        bits = AppGlobals.current_word_size.bits

        # Check if the sign bit (Most Significant Bit) is set
        is_signed = bool(val & (1 << (bits - 1)))
        if is_signed:
            val -= 1 << bits

        return val, is_signed

    @staticmethod
    def int_to_hex_with_prefix(value: int):
        return f"{hex(value).upper().replace("0X", "0x")}"

    @staticmethod
    def real_part():
        return AppGlobals.input_box.number

    @staticmethod
    def imag_part():
        return AppGlobals.input_imag_box.number

    @staticmethod
    def real_part_focus():
        AppGlobals.input_box.setFocus()
        AppGlobals.input_box.selectAll()

    def number_to_input_box(val: int |float | complex):
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            AppGlobals.complex_number_to_input_box(val)
        else:
            AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(val))

    # get complex number depending of rectangular or polar form
    @staticmethod
    def get_complex_number() -> complex:
        if AppGlobals.complex_number_form is ComplexNumberForm.rectangular:
            real_part = AppGlobals.real_part()
            imag_part = AppGlobals.imag_part()
        else:
            angle = AppGlobals.angle_unit.to_rad(AppGlobals.imag_part())
            z = cmath.rect(AppGlobals.real_part(), angle)
            real_part = z.real
            imag_part = z.imag
        return complex(real_part, imag_part)

    @staticmethod
    def get_number() -> float | complex:
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            return AppGlobals.get_complex_number()
        else:
            return AppGlobals.input_box.number

    @staticmethod
    def set_memory(val: float | complex):
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            AppGlobals.input_box.memory = val.real
            AppGlobals.input_imag_box.memory = val.imag
        else:
            AppGlobals.input_box.memory = val

    # used to make unsigned value
    @staticmethod
    def mask_value(val: int) -> int:
        # Create a bitmask for the specified size (e.g., 0xFF for 8-bit, 0xFFFF for 16-bit)
        standard_mask = (1 << AppGlobals.get_standard_mask_size(val)) - 1
        if AppGlobals.current_word_size.mask > standard_mask:
            mask = AppGlobals.current_word_size.mask
        else:
            mask = standard_mask
        if AppGlobals.calc_mode is CalcMode.base_n:
           return (val & mask)
        else:
            return val

    @staticmethod
    def get_standard_mask_size(number: int) -> int:
        """Find the smallest standard bit mask size (8, 16, 32, 64 bits)

        that can hold the given signed integer.
        """
        # Bit sizes to evaluate
        standard_sizes = [8, 16, 32, 64]

        for bits in standard_sizes:
            # Calculate valid bounds for signed integer in two's complement
            min_val = -(1 << (bits - 1))
            max_val = (1 << (bits - 1)) - 1

            if min_val <= number <= max_val:
                return bits

        return 64

        # raise ValueError(
        #     f"Number {number} exceeds maximum supported 64-bit mask size."
        # )

    @staticmethod
    def to_nibble_bin(val: int, bits: int = None) -> str:
        """Converts an integer to a binary string with padded leading zeros and nibble spacing.

        Examples:
            0x51  (8 bit)  -> '0b0101 0001'
            0x510 (12/16 bit) -> '0b0000 0101 0001 0000'
        """

        if val < 0:
            return f"-{AppGlobals.to_nibble_bin(abs(val), bits)}"

        # Convert to pure binary string
        raw_bin = bin(val)[2:]

        # Auto-calculate bit length if not specified:
        # Round up to the next multiple of 4 bits (at least 8 bits)
        if bits is None:
            needed_bits = max(8, len(raw_bin))
            bits = ((needed_bits + 3) // 4) * 4

        # Pad exact number of leading zeros
        padded_bin = raw_bin.zfill(bits)

        # Split into 4-bit nibbles from left to right
        nibbles = [padded_bin[i : i + 4] for i in range(0, len(padded_bin), 4)]

        return f"0b {' '.join(nibbles)}"

    @staticmethod
    def is_number_out_of_range(val: int) -> bool:
        AppGlobals.assert_int(val)
        
        int_number = int(val)

        if AppGlobals.base_n_signed:
            # Minimaler und maximaler Wert für N-Bit Signed
            min_val = -(1 << (AppGlobals.current_word_size.bits - 1))  # Bei 8 Bit: -128
            max_val = (1 << (AppGlobals.current_word_size.bits - 1)) - 1   # Bei 8 Bit:  127
        else:
            min_val = 0
            max_val = (1 << AppGlobals.current_word_size.bits) - 1  # Bei 8 Bit: 255

        if int_number < min_val or int_number > max_val:
            return True
        else:
            return False

    @staticmethod
    def assert_int(val: int):
        if not val.is_integer():
            raise ValueError("Expected integer")

    # return signed value, 1) if mode is signed, and 2) valus has sign
    @staticmethod
    def check_for_signed_number(val: int):
        if AppGlobals.base_n_signed:
            signed_val, signed = AppGlobals.uint_to_signed_int(val)
            if signed:
                return signed_val
            else:
                return val
        else:
            return val

    # Converts complex number to input boxes dependend on rect or polar form
    @staticmethod
    def complex_number_to_input_box(val: complex):
        if AppGlobals.complex_number_form is ComplexNumberForm.rectangular:
            AppGlobals.input_box.setTextSelect(AppGlobals.input_box.toString(val.real))
            AppGlobals.input_imag_box.setTextSelect(AppGlobals.input_imag_box.toString(val.imag))
        else:
            r, theta = cmath.polar(val)
            AppGlobals.input_box.setTextSelect(AppGlobals.input_box.toString(r))
            AppGlobals.input_imag_box.setTextSelect(AppGlobals.input_imag_box.toString(AppGlobals.angle_unit.from_rad(theta)))

    @staticmethod
    def get_memory():
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            return complex(AppGlobals.input_box.memory, AppGlobals.input_imag_box.memory)
        else:
            return AppGlobals.input_box.memory

    @staticmethod
    def complex_number_to_format_string(val: complex):
        if AppGlobals.complex_number_form is ComplexNumberForm.rectangular:
            if val.imag < 0:
                return f"{AppGlobals.to_format_string(val.real)}{AppGlobals.to_format_string(val.imag)}i"
            else:
                return f"{AppGlobals.to_format_string(val.real)}+{AppGlobals.to_format_string(val.imag)}i"
        else:
            r, theta = cmath.polar(val)
            return f"{AppGlobals.to_format_string(r)}∠{AppGlobals.to_format_string(AppGlobals.angle_unit.from_rad(theta))}"

    @staticmethod
    def is_complex(val: object) -> bool:
        """Check if a value is a complex number with a non-zero imaginary part.
        
        Returns True if 'val' is a complex instance or a float/int representation 
        of a complex number, and its imaginary component is non-zero.
        """
        return isinstance(val, complex)

    # Check if Shift key is pressed (Windows only)
    # Used to check if Shift key is pressed when clicking or typing on a hyperlink in the history browser.
    @staticmethod
    def is_shift_pressed() -> bool:
        user32 = ctypes.windll.user32
        left_shift  = bool(user32.GetAsyncKeyState(0xA0) & 0x8000)  # VK_LSHIFT
        right_shift = bool(user32.GetAsyncKeyState(0xA1) & 0x8000)  # VK_RSHIFT
        return left_shift or right_shift