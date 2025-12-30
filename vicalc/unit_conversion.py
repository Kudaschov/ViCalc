from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QListWidget, QLineEdit, QPushButton
)
from PySide6.QtCore import QLocale

class Unit:
    def __init__(self, quantity, name, symbol, to_base, from_base):
        self.quantity = quantity
        self.name = name
        self.symbol = symbol
        self.to_base = to_base
        self.from_base = from_base

class UnitRegistry:
    def __init__(self):
        self.units = []
        self.unit_symbols = set()
        self.unit_names = set()
        self._build_defaults()

    def add(self, unit: Unit):
        # Check for duplicates by symbol or name
        if unit.symbol in self.unit_symbols:
            raise ValueError(f"Duplicate unit symbol detected: {unit.symbol}")
        if unit.name in self.unit_names:
            raise ValueError(f"Duplicate unit name detected: {unit.name}")

        # If unique, register the unit
        self.units.append(unit)
        self.unit_symbols.add(unit.symbol)
        self.unit_names.add(unit.name)

    def by_quantity(self, quantity):
        return [u for u in self.units if u.quantity == quantity]

    def find(self, symbol):
        for u in self.units:
            if u.symbol == symbol:
                return u
        return None

    def _build_defaults(self):
        A = "Area"
        self.add(Unit(A, "acre", "ac", lambda x: x * 4046.873, lambda x: x / 4046.873))
        self.add(Unit(A, "hectare", "ha", lambda x: x * 10000, lambda x: x / 10000))
        self.add(Unit(A, "square centimeter", "cm²", lambda x: x * 1e-4, lambda x: x / 1e-4))
        self.add(Unit(A, "square foot", "ft²", lambda x: x * 9.290304e-2, lambda x: x / 9.290304e-2))
        self.add(Unit(A, "square inch", "in²", lambda x: x * 6.4516e-4, lambda x: x / 6.4516e-4))
        self.add(Unit(A, "square kilometer", "km²", lambda x: x * 1e6, lambda x: x / 1e6))
        self.add(Unit(A, "square meter", "m²", lambda x: x, lambda x: x))
        self.add(Unit(A, "square mile", "mi²", lambda x: x * 2.589988e6, lambda x: x / 2.589988e6))
        self.add(Unit(A, "square millimeter", "mm²", lambda x: x * 1e-6, lambda x: x / 1e-6))
        self.add(Unit(A, "square yard", "yd²", lambda x: x * 0.8361274, lambda x: x / 0.8361274))

        E = "Energy"
        self.add(Unit(E, "British thermal unit (th)", "Btu", lambda x: x * 1.05435e3, lambda x: x / 1.05435e3))
        self.add(Unit(E, "calorie (th)", "cal", lambda x: x * 4.184, lambda x: x / 4.184))
        self.add(Unit(E, "electronvolt", "eV", lambda x: x * 1.602176e-19, lambda x: x / 1.602176e-19))
        self.add(Unit(E, "erg", "erg", lambda x: x * 1e-7, lambda x: x / 1e-7))
        self.add(Unit(E, "joule", "J", lambda x: x, lambda x: x))
        self.add(Unit(E, "kilocalorie (th)", "kcal", lambda x: x * 4184, lambda x: x / 4184))
        self.add(Unit(E, "kilowatt hour", "kWh", lambda x: x * 3.6e6, lambda x: x / 3.6e6))
        self.add(Unit(E, "megajoule", "MJ", lambda x: x * 1e6, lambda x: x / 1e6))
        self.add(Unit(E, "therm (EC)", "thm_EC", lambda x: x * 1.05506e8, lambda x: x / 1.05506e8))
        self.add(Unit(E, "therm (US)", "thm_US", lambda x: x * 1.054804e8, lambda x: x / 1.054804e8))
        self.add(Unit(E, "ton of TNT", "tTNT", lambda x: x * 4.184e9, lambda x: x / 4.184e9))
        self.add(Unit(E, "watt hour", "Wh", lambda x: x * 3600, lambda x: x / 3600))

        F = "Force"
        self.add(Unit(F, "kilogram-force", "kgf", lambda x: x * 9.80665, lambda x: x / 9.80665))
        self.add(Unit(F, "kilonewton", "kN", lambda x: x * 1000.0, lambda x: x / 1000.0))
        self.add(Unit(F, "newton", "N", lambda x: x, lambda x: x))
        self.add(Unit(F, "ton-force (2000 lbf)", "tonf", lambda x: x * 8896.443, lambda x: x / 8896.443))

        F = "Fuel consumption"
        self.add(Unit(
            F,
            "kilometer per liter",
            "km/L",
            to_base=lambda x: x,
            from_base=lambda x: x
        ))
        self.add(Unit(
            F,
            "liter per 100 km",
            "L/100km",
            to_base=lambda x: 100.0 / x,
            from_base=lambda x: 100.0 / x
        ))
        self.add(Unit(
            F,
            "mile per gallon (US)",
            "mpg",
            to_base=lambda x: x * 4.251437e-1,  # mpg -> km/L
            from_base=lambda x: x / 4.251437e-1
        ))

        L = "Length"
        # existing units
        self.add(Unit(L, "ångström", "Å", lambda x: x*1e-10, lambda x: x/1e-10))
        self.add(Unit(L, "centimeter", "cm", lambda x: x*1e-2, lambda x: x/1e-2))
        self.add(Unit(L, "decimeter", "dm", lambda x: x * 0.1, lambda x: x / 0.1))
        self.add(Unit(L, "fathom", "ftm", lambda x: x*1.828804, lambda x: x/1.828804))
        self.add(Unit(L, "foot", "ft", lambda x: x*0.3048, lambda x: x/0.3048))
        self.add(Unit(L, "inch", "in", lambda x: x*0.0254, lambda x: x/0.0254))
        self.add(Unit(L, "kilometer", "km", lambda x: x*1000, lambda x: x/1000))
        self.add(Unit(L, "light year", "ly", lambda x: x*9.46073e15, lambda x: x/9.46073e15))
        self.add(Unit(L, "meter", "m", lambda x: x, lambda x: x))
        self.add(Unit(L, "micrometer", "μm", lambda x: x*1e-6, lambda x: x/1e-6))
        self.add(Unit(L, "micron", "μ", lambda x: x*1e-6, lambda x: x/1e-6))
        self.add(Unit(L, "mil", "mil", lambda x: x*2.54e-5, lambda x: x/2.54e-5))
        self.add(Unit(L, "mile", "mi", lambda x: x*1609.344, lambda x: x/1609.344))
        self.add(Unit(L, "mile, nautical ", "mi,n", lambda x: x*1852, lambda x: x/1852))
        self.add(Unit(L, "millimeter", "mm", lambda x: x*1e-3, lambda x: x/1e-3))
        self.add(Unit(L, "nanometer", "nm", lambda x: x*1e-9, lambda x: x/1e-9))
        self.add(Unit(L, "parsec", "pc", lambda x: x*3.085678e16, lambda x: x/3.085678e16))
        self.add(Unit(L, "rod", "rd", lambda x: x*5.029210, lambda x: x/5.029210))
        self.add(Unit(L, "yard", "yd", lambda x: x*0.9144, lambda x: x/0.9144))

        M = "Mass"
        self.add(Unit(M, "carat", "ct", lambda x: x * 2e-4, lambda x: x / 2e-4))
        self.add(Unit(M, "grain", "gr", lambda x: x * 6.479891e-5, lambda x: x / 6.479891e-5))
        self.add(Unit(M, "gram", "g", lambda x: x * 0.001, lambda x: x / 0.001))
        self.add(Unit(M, "kilogram", "kg", lambda x: x, lambda x: x))
        self.add(Unit(M, "milligram", "mg", lambda x: x * 1e-6, lambda x: x / 1e-6))
        self.add(Unit(M, "ounce (avoirdupois)", "oz", lambda x: x * 2.834952e-2, lambda x: x / 2.834952e-2))
        self.add(Unit(M, "pound (avoirdupois)", "lb", lambda x: x * 0.4535924, lambda x: x / 0.4535924))
        self.add(Unit(M, "ton, metric", "t", lambda x: x * 1000.0, lambda x: x / 1000.0))
        self.add(Unit(M, "ton, short (2000 lb)", "ton", lambda x: x * 907.1847, lambda x: x / 907.1847))

        T = "Moment of Force or Torque"
        self.add(Unit(T, "kilogram-force meter", "kgf·m", lambda x: x * 9.80665, lambda x: x / 9.80665))
        self.add(Unit(T, "newton meter", "N·m", lambda x: x, lambda x: x))
        self.add(Unit(T, "pound-force foot", "lbf·ft", lambda x: x * 1.355818, lambda x: x / 1.355818))

        P = "Power"
        self.add(Unit(P, "horsepower (electric)", "hp_e", lambda x: x * 746.0, lambda x: x / 746.0))
        self.add(Unit(P, "horsepower (metric)", "hp_m", lambda x: x * 7.354988e2, lambda x: x / 7.354988e2))
        self.add(Unit(P, "horsepower (UK)", "hp_UK", lambda x: x * 745.70, lambda x: x / 745.70))
        self.add(Unit(P, "kilowatt", "kW", lambda x: x * 1000.0, lambda x: x / 1000.0))
        self.add(Unit(P, "watt", "W", lambda x: x, lambda x: x))

        P = "Pressure"
        self.add(Unit(P, "atmosphere", "atm", lambda x: x * 101325.0, lambda x: x / 101325.0))
        self.add(Unit(P, "bar", "bar", lambda x: x * 100000.0, lambda x: x / 100000.0))
        self.add(Unit(P, "kilopascal", "kPa", lambda x: x * 1000.0, lambda x: x / 1000.0))
        self.add(Unit(P, "kilogram-force per square centimeter", "kgf/cm²", lambda x: x * 98066.5, lambda x: x / 98066.5))
        self.add(Unit(P, "millibar", "mbar", lambda x: x * 100.0, lambda x: x / 100.0))
        self.add(Unit(P, "millimeter of mercury", "mmHg", lambda x: x * 1.333224e2, lambda x: x / 1.333224e2))
        self.add(Unit(P, "pascal", "Pa", lambda x: x, lambda x: x))
        self.add(Unit(P, "pound-force per square inch", "lbf/in²", lambda x: x * 6894.757, lambda x: x / 6894.757))

        T = "Temperature"
        self.add(Unit(T, "Celsius", "°C", lambda x: x + 273.15, lambda x: x - 273.15))
        self.add(Unit(T, "Fahrenheit", "°F", lambda x: (x + 459.67)/1.8, lambda x: x*1.8 - 459.67))
        self.add(Unit(T, "Kelvin", "K", lambda x: x, lambda x: x))
        self.add(Unit(T, "Rankine", "°R", lambda x: x / 1.8, lambda x: x * 1.8))

        V = "Velocity (includes Speed)"
        self.add(Unit(V, "kilometer per hour", "km/h", lambda x: x / 3.6, lambda x: x * 3.6))
        self.add(Unit(V, "meter per second", "m/s", lambda x: x, lambda x: x))
        self.add(Unit(V, "mile per hour", "mi/h", lambda x: x * 0.44704, lambda x: x / 0.44704))
        self.add(Unit(V, "mile per second", "mi/s", lambda x: x * 1609.344, lambda x: x / 1609.344))

        V1 = "Volume"
        self.add(Unit(V1, "barrel (US)", "bbl", lambda x: x * 1.589873e-1, lambda x: x / 1.589873e-1))
        self.add(Unit(V1, "cubic inch", "in³", lambda x: x * 1.6387064e-05, lambda x: x / 1.6387064e-05))
        self.add(Unit(V1, "cubic meter", "m³", lambda x: x, lambda x: x))
        self.add(Unit(V1, "gallon (UK)", "gal_UK", lambda x: x * 0.00454609, lambda x: x / 0.00454609))
        self.add(Unit(V1, "gallon (US)", "gal", lambda x: x * 3.785412e-3, lambda x: x / 3.785412e-3))
        self.add(Unit(V1, "liter", "L", lambda x: x * 0.001, lambda x: x / 0.001))
        self.add(Unit(V1, "milliliter = cm³", "mL", lambda x: x * 1e-6, lambda x: x / 1e-6))
        self.add(Unit(V1, "ounce (UK fl oz)", "oz_UK", lambda x: x * 2.841306e-5, lambda x: x / 2.841306e-5))
        self.add(Unit(V1, "ounce (US fl oz)", "oz_US", lambda x: x * 2.957353e-5, lambda x: x / 2.957353e-5))
        self.add(Unit(V1, "pint (US liquid)", "liq pt", lambda x: x * 4.731765e-4, lambda x: x / 4.731765e-4))
        self.add(Unit(V1, "quart (US liquid)", "liq qt", lambda x: x * 9.463529e-4, lambda x: x / 9.463529e-4))
        self.add(Unit(V1, "tablespoon", "tbsp", lambda x: x * 1.478676e-5, lambda x: x / 1.478676e-5))
        self.add(Unit(V1, "teaspoon", "tsp", lambda x: x * 4.928922e-6, lambda x: x / 4.928922e-6))

class ConversionDialog(QDialog):
    def __init__(self, initial_value=None, initial_unit=None, result_unit=None):
        super().__init__()
        self.registry = UnitRegistry()
        self.initial_value = initial_value
        self.initial_unit = initial_unit
        self.result_unit = result_unit
        self.value = None
        self.unit = None
        self.result = None
        self.result_unit_out = None
        self._build_ui()

    def _build_ui(self):
        self.setWindowTitle("Unit Converter NIST SP 811 / 2008")
        self.resize(600, 480)
        layout = QVBoxLayout()

        # Horizontal layout for listboxes with labels on top
        lists_layout = QHBoxLayout()

        # Quantity
        qbox = QVBoxLayout()
        label_quantity = QLabel("&Quantity")
        qbox.addWidget(label_quantity)
        self.quantity_list = QListWidget()
        label_quantity.setBuddy(self.quantity_list)
        for q in sorted(set(u.quantity for u in self.registry.units)):
            self.quantity_list.addItem(q)
        qbox.addWidget(self.quantity_list)
        lists_layout.addLayout(qbox)

        # From
        fbox = QVBoxLayout()
        label_from = QLabel("&From")
        fbox.addWidget(label_from)
        self.from_list = QListWidget()
        label_from.setBuddy(self.from_list)
        fbox.addWidget(self.from_list)
        lists_layout.addLayout(fbox)

        # To
        tbox = QVBoxLayout()
        label_to = QLabel("&To")
        tbox.addWidget(label_to)
        self.to_list = QListWidget()
        label_to.setBuddy(self.to_list)
        tbox.addWidget(self.to_list)
        lists_layout.addLayout(tbox)

        layout.addLayout(lists_layout)

        # Input and Result
        hbox = QHBoxLayout()
        value_label = QLabel("&Value:")
        self.input_edit = QLineEdit()
        self.input_edit.setMaximumWidth(150)
        value_label.setBuddy(self.input_edit)
        value_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        hbox.addWidget(value_label)
        self.result_label = QLabel("…")
        self.result_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        hbox.addWidget(self.input_edit)
        swap_btn = QPushButton("&Swap")
        swap_btn.clicked.connect(self._swap_units)
        hbox.addWidget(self.result_label)
        hbox.addWidget(swap_btn)
        layout.addLayout(hbox)

        # OK/Cancel
        btnbox = QHBoxLayout()
        self.ok_btn = QPushButton("OK")
        self.ok_btn.setDefault(True)
        cancel_btn = QPushButton("Cancel")
        self.ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btnbox.addWidget(self.ok_btn)
        btnbox.addWidget(cancel_btn)
        layout.addLayout(btnbox)

        self.setLayout(layout)

        # signals
        self.quantity_list.currentTextChanged.connect(self._populate_units)
        self.from_list.currentTextChanged.connect(self._convert)
        self.to_list.currentTextChanged.connect(self._convert)
        self.input_edit.textChanged.connect(self._convert)

        # initialize selections
        if self.initial_unit:
            u = self.registry.find(self.initial_unit)
            if u:
                # select quantity
                for i in range(self.quantity_list.count()):
                    if self.quantity_list.item(i).text() == u.quantity:
                        self.quantity_list.setCurrentItem(self.quantity_list.item(i))
                        break
                self._populate_units(u.quantity)
                # select from unit
                for i in range(self.from_list.count()):
                    if self.from_list.item(i).text().endswith(f"({u.symbol})"):
                        self.from_list.setCurrentRow(i)
                        break

        if self.result_unit:
            u = self.registry.find(self.result_unit)
            if u and self.to_list.count() > 0:
                for i in range(self.to_list.count()):
                    if self.to_list.item(i).text().endswith(f"({u.symbol})"):
                        self.to_list.setCurrentRow(i)
                        break

        if self.initial_value is not None:
            locale = QLocale(QLocale.C)
            locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)
            self.input_edit.setText(locale.toString(self.initial_value, "g", 15))

        self.input_edit.setFocus()

    def _populate_units(self, quantity):
        self.from_list.clear()
        self.to_list.clear()
        units = self.registry.by_quantity(quantity)
        for u in units:
            self.from_list.addItem(f"{u.name} ({u.symbol})")
            self.to_list.addItem(f"{u.name} ({u.symbol})")
        if units:
            self.from_list.setCurrentRow(0)
            if self.to_list.count() > 1:
                self.to_list.setCurrentRow(1)

    def _convert(self):
        try:
            locale = QLocale(QLocale.C)
            locale.setNumberOptions(QLocale.NumberOption.OmitGroupSeparator)
            value, ok = locale.toDouble(self.input_edit.text())
            if not ok:
                self.result_label.setText("Invalid")
                self.ok_btn.setEnabled(False)
                return
            
            self.ok_btn.setEnabled(True)

            from_txt = self.from_list.currentItem().text()
            to_txt = self.to_list.currentItem().text()
            from_symbol = from_txt.split("(")[-1][:-1]
            to_symbol = to_txt.split("(")[-1][:-1]
            from_u = self.registry.find(from_symbol)
            to_u = self.registry.find(to_symbol)
            if not from_u or not to_u:
                return
            base = from_u.to_base(value)
            result = to_u.from_base(base)
            s_in = f"{from_symbol}"
            s_out = f"{locale.toString(result, "g", 15)} {to_symbol}"
            self.result_label.setText(f"{s_in} = {s_out}")
            self.value, self.unit, self.result, self.result_unit_out = value, from_symbol, result, to_symbol
        except Exception:
            self.ok_btn.setEnabled(False)

    def _swap_units(self):
        fi = self.from_list.currentRow()
        ti = self.to_list.currentRow()
        if fi >= 0 and ti >= 0:
            self.from_list.setCurrentRow(ti)
            self.to_list.setCurrentRow(fi)
            self._convert()

    def get_results(self):
        return self.value, self.unit, self.result, self.result_unit_out