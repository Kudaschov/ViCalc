import sys
import urllib.request
from PySide6 import QtGui
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QDialogButtonBox, QLabel
)
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from pathlib import Path
from .AppGlobals import AppGlobals

def load_pixmap(url: str) -> QPixmap | None:
    """Download an image using a User-Agent header, return QPixmap or None."""
    try:
        if not url:
            return None
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
        pix = QPixmap()
        return pix if pix.loadFromData(data) else None
    except Exception as e:
        print("Image load failed:", e)
    return None

# Directory containing CODATA GIFs
if getattr(sys, 'frozen', False):  # running as compiled .exe
    BASE_DIR = Path(sys._MEIPASS)
else:  # running as script
    BASE_DIR = Path.cwd()
#    BASE_DIR = Path(__file__).parent

GIF_DIR = BASE_DIR / "vicalc/images"

PHYSICAL_CONSTANTS = [
    {"symbol": "c",   "name": "speed of light in vacuum", "value": 299792458.0,     "unit": "m/s",     "gif": "c.gif"},
    {"symbol": "μ0",  "name": "vacuum magnetic permeability",       "value": 1.25663706127e-6, "unit": "N A⁻²",    "gif": "mu0.gif"},
    {"symbol": "ε0",  "name": "vacuum electric permittivity",       "value": 8.8541878188e-12, "unit": "F/m",     "gif": "ep0.gif"},
    {"symbol": "Z0",  "name": "characteristic impedance of vacuum", "value": 376.730313412,    "unit": "Ω",       "gif": "z0.gif"},
    {"symbol": "g",   "name": "standard acceleration of gravity", "value": 9.80665, "unit": "m s⁻²", "gif": "gn.gif"},
    {"symbol": "G",   "name": "Newtonian constant of gravitation",  "value": 6.67430e-11,      "unit": "m³ kg⁻¹ s⁻²", "gif": "bg.gif"},
    {"symbol": "h",   "name": "Planck constant",           "value": 6.62607015e-34,   "unit": "J s",     "gif": "h.gif"},
    {"symbol": "ħ",   "name": "reduced Planck constant",   "value": 1.054571817e-34,  "unit": "J s",     "gif": "hbar.gif"},
    {"symbol": "k_e", "name": "Coulomb constant",          "value": 8.9875517862e9, "unit": "N m² C⁻²", "gif": "ke.gif"},
    {"symbol": "e",   "name": "elementary charge",         "value": 1.602176634e-19,  "unit": "C",       "gif": "e.gif"},
    {"symbol": "Φ0",  "name": "magnetic flux quantum",     "value": 2.067833848e-15, "unit": "Wb", "gif": "flxquhs2e.gif"},
    {"symbol": "G₀",  "name": "conductance quantum",       "value": 7.748091729e-5, "unit": "S", "gif": "conqu2e2sh.gif"},
    {"symbol": "μB",  "name": "Bohr magneton",             "value": 9.2740100657e-24, "unit": "J/T",    "gif": "mub.gif"},
    {"symbol": "μN",  "name": "nuclear magneton",          "value": 5.0507837393e-27, "unit": "J/T",    "gif": "mun.gif"},
    {"symbol": "α",   "name": "fine-structure constant",   "value": 7.2973525643e-3,  "unit": "","gif": "alph.gif"},
    {"symbol": "R∞",  "name": "Rydberg constant",          "value": 10973731.568157,   "unit": "[m⁻¹]†",   "gif": "ryd.gif"},
    {"symbol": "a₀",  "name": "Bohr radius",               "value": 5.29177210544e-11,"unit": "m",      "gif": "bohrrada0.gif"},
    {"symbol": "mₑ",  "name": "electron mass",             "value": 9.1093837139e-31, "unit": "kg",     "gif": "me.gif"},
    {"symbol": "λₑ",  "name": "Compton wavelength",        "value": 2.42631023538e-12,"unit": "[m]†",   "gif": "ecomwl.gif"},
    {"symbol": "rₑ",  "name": "classical electron radius", "value": 2.8179403205e-15, "unit": "m",       "gif": "re.gif"},
    {"symbol": "μₑ",  "name": "electron magnetic moment",  "value": -9.2847646917e-24,"unit": "J/T",   "gif": "muem.gif"},
    {"symbol": "m_μ", "name": "muon mass",                 "value": 1.883531627e-28,  "unit": "kg",     "gif": "mmu.gif"},
    {"symbol": "μ_μ", "name": "muon magnetic moment",      "value": -4.49044830e-26, "unit": "J/T", "gif": "mumum.gif"},
    {"symbol": "mₚ⁺", "name": "proton mass",                "value": 1.67262192595e-27,"unit": "kg",      "gif": "mp.gif"},
    {"symbol": "λ_{C,p}", "name": "proton Compton wavelength", "value": 1.32140985360e-15, "unit": "m", "gif": "pcomwl.gif"},
    {"symbol": "μ_p", "name": "proton magnetic moment", "value": 1.41060679545e-26, "unit": "J/T", "gif": "mup.gif"},
    {"symbol": "γₚ",  "name": "proton gyromagnetic ratio", "value": 2.6752218708e8, "unit": "s⁻¹ T⁻¹", "gif": "gammap.gif"},
    {"symbol": "mₙ",  "name": "neutron mass",              "value": 1.67492750056e-27,"unit": "kg",      "gif": "mn.gif"},
    {"symbol": "λ_{C,n}", "name": "neutron Compton wavelength", "value": 1.31959090382e-15, "unit": "[m]†", "gif": "ncomwl.gif"},
    {"symbol": "μ_n", "name": "neutron magnetic moment",   "value": -9.6623653e-27, "unit": "J/T", "gif": "munn.gif"},
    {"symbol": "Nₐ",  "name": "Avogadro constant",         "value": 6.02214076e23,    "unit": "mol⁻¹",   "gif": "na.gif"},
    {"symbol": "k",   "name": "Boltzmann constant",        "value": 1.380649e-23,     "unit": "J/K",     "gif": "k.gif"},
    {"symbol": "u",   "name": "atomic mass constant",      "value": 1.66053906892e-27, "unit": "kg", "gif": "u.gif"},
    {"symbol": "R",   "name": "molar gas constant",        "value": 8.314462618,      "unit": "J mol⁻¹ K⁻¹","gif": "r.gif"},
    {"symbol": "F",   "name": "Faraday constant",          "value": 96485.33212,      "unit": "C/mol",   "gif": "f.gif"},
    {"symbol": "atm", "name": "standard atmosphere",       "value": 101325.0, "unit": "Pa", "gif": "stdatm.gif"},
    {"symbol": "V_m", "name": "molar volume of ideal gas (273.15 K, 101.325 kPa)", "value": 22.41396954e-3, "unit": "m³/mol", "gif": "mvolstd.gif"},
    {"symbol": "σ",   "name": "Stefan–Boltzmann constant", "value": 5.670374419e-8, "unit": "W m⁻² K⁻⁴", "gif": "sigma.gif"},
    {"symbol": "c₁",  "name": "first radiation constant",  "value": 3.741771852e-16, "unit": "[W m²]†", "gif": "c11strc.gif"},
    {"symbol": "c₂",  "name": "second radiation constant", "value": 1.438776877e-2, "unit": "[m K]†", "gif": "c22ndrc.gif"},
]

class PhyConstDialog(QDialog):
    def __init__(self, previous_index=0):
        super().__init__()
        self.setWindowTitle("Fundamental physical constants — CODATA 2022")
        self.resize(550, 600)

        layout = QVBoxLayout(self)
        self.table = QTableWidget(len(PHYSICAL_CONSTANTS), 4)
        self.table.setHorizontalHeaderLabels(["Symbol", "Name", "Value", "Unit"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)#        self.table.verticalHeader().setVisible(False)
        self.table.cellDoubleClicked.connect(lambda row, col: self.accept())

        for row, const in enumerate(PHYSICAL_CONSTANTS):
            # Column 0: GIF or text
            gif_path = GIF_DIR / const["gif"]
            if const["gif"]:
                pix = QPixmap(str(gif_path))
                if pix:
                    lbl = QLabel()
#                    lbl.setPixmap(pix.scaledToHeight(15, Qt.SmoothTransformation))
                    lbl.setPixmap(pix)
                    lbl.setAlignment(Qt.AlignCenter)
                    lbl.setStyleSheet("background-color: #D0F0C8;")
                    self.table.setCellWidget(row, 0, lbl)
                else:
                    item = QTableWidgetItem(const["symbol"])
                    item.setBackground(QColor("#D0F0C8"))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(row, 0, item)
            else:
                item = QTableWidgetItem(const["symbol"])
                item.setBackground(QColor("#D0F0C8"))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, 0, item)

            # Columns 1–3
            self.table.setItem(row, 1, QTableWidgetItem(const["name"]))
            self.table.setItem(row, 2, QTableWidgetItem(AppGlobals.to_normal_string(const["value"])))
            self.table.setItem(row, 3, QTableWidgetItem(const["unit"]))

        self.table.setColumnWidth(0, 60)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 150)
        self.table.setRowHeight(row, 22)
        layout.addWidget(self.table)

        if 0 <= previous_index < len(PHYSICAL_CONSTANTS):
            self.table.selectRow(previous_index)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_selection_by_index(self):
        row = self.table.currentRow()
        if row >= 0:
            return PHYSICAL_CONSTANTS[row], row
        return None, None
