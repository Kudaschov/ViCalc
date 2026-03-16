# ViCalc

ViCalc is an open-source touch-typing scientific calculator with a key-preselection function. It turns your PC keyboard into a scientific calculator, while full mouse support is also available.

The upper part of the ViCalc window displays the calculation history. The lower part shows the left section of the main keyboard area and the numeric keypad.

<img src="docs/images/vicalc_keyboard_area.png" alt = "ViCalc" width="760" />

## Keyboard Operation Modes

ViCalc supports two keyboard operation modes.

### Mode 1
In this mode, the left hand remains in the standard touch-typing position (ASDF), while the right hand operates the numeric keypad (see picture above).

The numeric keypad functions as a scientific calculator.
The left hand is used for additional input functions:

- E key – enter the exponent (scientific notation)
- Shift – access the second function of a key (see picture below)
- Ctrl – access the third function of a key (see picture below)
- Additional scientific functions (for example polar coordinates) that are not available directly on the numeric keypad

<img src="docs/images/key.png" alt = "Key functions" /><br>

### Mode 2

If the user prefers the traditional touch-typing position (ASDF and JKL:), or if a full-size keyboard with a numeric keypad is not available (for example on notebooks), ViCalc provides Operation Mode 2 (see picture below).

Although this section of the keyboard is not displayed on the screen, it is fully supported. It is used for entering the symbols exactly as they appear on the keyboard, including:

- Numbers 7, 8, 9, 0
- Parentheses ()
- \+ − * /
- ., =
- underscore for negative sign
- Backspace
- Enter
- Shift
- Control<br>

<img src="docs/images/vicalc_mode_2.png" alt = "ViCalc Mode 2" /><br>

## Key-Preselection Function
The Key-Preselection feature allows you to preview a key before its function is executed.

This function requires a keyboard with analog input. ViCalc was developed and tested using the Wooting Two HE keyboard. With a standard keyboard, ViCalc works fully, but the Key-Preselection feature is not available.

When a key is lightly pressed, the corresponding function is highlighted (preselected) on the screen.
If this is the desired function, you can press the key fully to execute it.

If the highlighted function is not the intended one, you can simply release the key and correct your input without triggering the wrong function.
<img src="docs/images/preselect.png" alt = "ViCalc Key-Preselection Function" width="760" /><br>

## Calculation Example
<img src="docs/images/ViCalcExample.png" alt = "ViCalc Calculation Example" width="760" />

## Key Features

- Touch-Typing Optimized: Keys are split for left-hand (left keyboard side) and right-hand (right side or numeric keypad) operation, enabling fast ten-finger typing.
- Calculation History: Automatically records output, allowing you to review or reuse past calculations.
- Mouse Support: Use the mouse for a traditional calculator experience.
- Cross-Platform: Runs on any system with Python.
- Open Source: Contributions are welcome to add new features!

## History

Originating in 2003, ViCalc was rewritten in Python to modernize it. It was created to address the need for a tool that integrates coding and calculations, supporting ten-finger typing for academic and professional tasks like mathematical modeling.

## Installation

You can install and run **ViCalc** using one of the following methods:

### Option 1: Use the Installer (Windows)

1. Go to the [Releases](https://github.com/Kudaschov/ViCalc/releases) page.
2. Download **`ViCalcSetup.exe`** from the **Assets** section of the latest release.
3. Run the installer and follow the on-screen instructions.

### Option 2: Clone and Run from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/kudaschov/ViCalc.git
   cd ViCalc

2. Run ViCalc
   ```bash
   python -m vicalc

## License
Copyright (c) Dr. Vitali Kudaschov, 2003 - 2026.

Licensed under the [MIT License](./LICENSE).
