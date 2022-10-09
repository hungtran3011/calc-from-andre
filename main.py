import sys
from functools import partial
import json

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PySide6.QtGui import QPixmap, QKeyEvent
from PySide6.QtCore import QSize
# from calc import Ui_MainWindow
from calc_ui import CalcUI, ResetPopup, BasicCalcUI, ScientificCalcUI, MeasurementConverterUI, AboutDialogUI
# from __feature__ import true_property, snake_case


with open("sto.json", "r+") as sto_file:
    tmp = json.load(sto_file)
    print(type(tmp))
    A = tmp["A"]
    B = tmp["B"]
    C = tmp["C"]
    D = tmp["D"]
    E = tmp["E"]
    F = tmp["F"]
    M = tmp["M"]
    X = tmp["X"]
    Y = tmp["Y"]
    Z = tmp["Z"]
    ANS = tmp["ANS"]

with open("./config/theme.json", "r") as theme_file:
    THEME = json.load(theme_file)

WINDOW_BG = THEME["window-bg"]
NUM_BUTTON_BG_NORMAL = THEME["num-button-bg-normal"]
NUM_BUTTON_FG_NORMAL = THEME["num-button-fg-normal"]
NUM_BUTTON_BG_HOVER = THEME["num-button-bg-hover"]
NUM_BUTTON_FG_HOVER = THEME["num-button-fg-hover"]
OP_BUTTON_BG_NORMAL = THEME["op-button-bg-normal"]
OP_BUTTON_FG_NORMAL = THEME["op-button-fg-normal"]
OP_BUTTON_BG_HOVER = THEME["op-button-bg-hover"]
OP_BUTTON_FG_HOVER = THEME["op-button-fg-hover"]
PROC_BUTTON_BG_NORMAL = THEME["proc-button-bg-normal"]
PROC_BUTTON_FG_NORMAL = THEME["proc-button-fg-normal"]
PROC_BUTTON_BG_HOVER = THEME["proc-button-bg-hover"]
PROC_BUTTON_FG_HOVER = THEME["proc-button-fg-hover"]
CALC_AREA_BG = THEME["calc-area-bg"]
SMALL_FONT_SIZE = THEME["small-font-size"]
GENERAL_FONT_SIZE = THEME["general-font-size"]
MENU_BG_NORMAL = THEME["menu-bg-normal"]
MENU_FG_NORMAL = THEME["menu-fg-normal"]
MENU_BG_HOVER = THEME["menu-bg-hover"]
MENU_FG_HOVER = THEME["menu-fg-hover"]
MESSAGE_DEFAULT_BUTTON_BG_NORMAL = THEME["message-default-button-bg-normal"]
MESSAGE_DEFAULT_BUTTON_FG_NORMAL = THEME["message-default-button-fg-normal"]
MESSAGE_DEFAULT_BUTTON_BG_HOVER = THEME["message-default-button-bg-hover"]
MESSAGE_DEFAULT_BUTTON_FG_HOVER = THEME["message-default-button-fg-hover"]
MESSAGE_OTHER_BUTTONS_BG_NORMAL = THEME["message-other-buttons-bg-normal"]
MESSAGE_OTHER_BUTTONS_FG_NORMAL = THEME["message-other-buttons-fg-normal"]
MESSAGE_OTHER_BUTTONS_BG_HOVER = THEME["message-other-buttons-bg-hover"]
MESSAGE_OTHER_BUTTONS_FG_HOVER = THEME["message-other-buttons-fg-hover"]
ICONS_COLOR = THEME["icons-color"]

if ICONS_COLOR == "FFFFFF":
    ICON_PATH = "./icons/white/"
else:
    ICON_PATH = "./icons/black/"

with open("./config/settings.json", "r+") as settings_file:
    settings = json.load(settings_file)

DEFAULT_MODE = settings["default-mode"]


class BasicCalcWidget(BasicCalcUI, QWidget):
    def __init__(self, MainWindow:QMainWindow):
        super().__init__()
        self.setupUi(self)
        self.MainWindow = MainWindow
        self.num_0.clicked.connect(partial(self.insert_chars, "0"))
        self.num_1.clicked.connect(partial(self.insert_chars, "1"))
        self.num_2.clicked.connect(partial(self.insert_chars, "2"))
        self.num_3.clicked.connect(partial(self.insert_chars, "3"))
        self.num_4.clicked.connect(partial(self.insert_chars, "4"))
        self.num_5.clicked.connect(partial(self.insert_chars, "5"))
        self.num_6.clicked.connect(partial(self.insert_chars, "6"))
        self.num_7.clicked.connect(partial(self.insert_chars, "7"))
        self.num_8.clicked.connect(partial(self.insert_chars, "8"))
        self.num_9.clicked.connect(partial(self.insert_chars, "9"))
        self.num_dot.clicked.connect(partial(self.insert_chars, "."))
        self.btn_divide.clicked.connect(partial(self.insert_chars, "/"))
        self.btn_plus.clicked.connect(partial(self.insert_chars, "+"))
        self.btn_minus.clicked.connect(partial(self.insert_chars, "-"))
        self.btn_times.clicked.connect(partial(self.insert_chars, "*"))
        self.btn_left.clicked.connect(partial(self.insert_chars, "("))
        self.btn_right.clicked.connect(partial(self.insert_chars,")")) 
        self.btn_eq.clicked.connect(self.calc)
        self.btn_ac.clicked.connect(self.ac) 
        self.btn_del.clicked.connect(self.del_calc)
        self.showing_ans = False

    def set_basic(self):
        self.MainWindow.setWindowTitle("Basic calculator")
        self.MainWindow.setMinimumSize(QSize(290, 450))
        self.MainWindow.menubar.action_ANS.triggered.connect(partial(self.insert_chars, "ANS"))
        self.MainWindow.menubar.action_rcl_A.triggered.connect(partial(self.insert_chars, "A"))
        self.MainWindow.menubar.action_rcl_B.triggered.connect(partial(self.insert_chars, "B"))
        self.MainWindow.menubar.action_rcl_C.triggered.connect(partial(self.insert_chars, "C"))
        self.MainWindow.menubar.action_rcl_D.triggered.connect(partial(self.insert_chars, "D"))
        self.MainWindow.menubar.action_rcl_E.triggered.connect(partial(self.insert_chars, "E"))
        self.MainWindow.menubar.action_rcl_F.triggered.connect(partial(self.insert_chars, "F"))
        self.MainWindow.menubar.action_rcl_M.triggered.connect(partial(self.insert_chars, "M"))
        self.MainWindow.menubar.action_rcl_X.triggered.connect(partial(self.insert_chars, "X"))
        self.MainWindow.menubar.action_rcl_Y.triggered.connect(partial(self.insert_chars, "Y"))
        self.MainWindow.menubar.action_rcl_Z.triggered.connect(partial(self.insert_chars, "Z"))
        self.MainWindow.menubar.action_sto_A.triggered.connect(partial(self.sto_var, "A"))
        self.MainWindow.menubar.action_sto_B.triggered.connect(partial(self.sto_var, "B"))
        self.MainWindow.menubar.action_sto_C.triggered.connect(partial(self.sto_var, "C"))
        self.MainWindow.menubar.action_sto_D.triggered.connect(partial(self.sto_var, "D"))
        self.MainWindow.menubar.action_sto_E.triggered.connect(partial(self.sto_var, "E"))
        self.MainWindow.menubar.action_sto_F.triggered.connect(partial(self.sto_var, "F"))
        self.MainWindow.menubar.action_sto_M.triggered.connect(partial(self.sto_var, "M"))
        self.MainWindow.menubar.action_sto_X.triggered.connect(partial(self.sto_var, "X"))
        self.MainWindow.menubar.action_sto_Y.triggered.connect(partial(self.sto_var, "Y"))
        self.MainWindow.menubar.action_sto_Z.triggered.connect(partial(self.sto_var, "Z"))
        self.MainWindow.menubar.action_reset.triggered.connect(self.reset_vars)
        self.MainWindow.menubar.menu_variables.setEnabled(True)

    def to_sto(self):
        print(
            {
                "A": A,
                "B": B,
                "C": C,
                "D": D,
                "E": E,
                "F": F,
                "M": M,
                "X": X,
                "Y": Y,
                "Z": Z,
                "ANS": ANS
            }
        )
        with open("sto.json", "w") as sto_file:
            json.dump({
                "A": A,
                "B": B,
                "C": C,
                "D": D,
                "E": E,
                "F": F,
                "M": M,
                "X": X,
                "Y": Y,
                "Z": Z,
                "ANS": ANS
            }, sto_file)

    def sto_var(self, var):
        # global A, B, C, D, E, F, M, X, Y, Z
        try:
            global A, B, C, D, E, F, M, X, Y, Z
            value = eval(str(self.calc_area.toPlainText()))
            print(value)
            self.calc()
            match var:
                case "A": 
                    A = value
                case "B":
                    B = value
                case "C":
                    C = value
                case "D":
                    D = value
                case "E":
                    E = value
                case "F":
                    F = value
                case "M":
                    M = value
                case "X":
                    X = value
                case "Y":
                    Y = value
                case "Z":
                    Z = value
        finally:
            self.to_sto()

    def eventFilter(self, event: QKeyEvent = None):
        accepted_chars = ['0','1','2','3','4','5','6','7','8','9','+','-','*',"/"]
        if (inp_char := event.text()) in accepted_chars:
            self.insert_chars(inp_char)

    def insert_chars(self, char: str):
        if self.showing_ans:
            self.calc_area.clear()
            self.showing_ans = False
            if "Error" not in self.calc_area.toPlainText() and char in ["+", "-", "*", "/"]:
                self.calc_area.insertPlainText(f"ANS {char} ")
        elif char in ["+", "-", "*", "/"]:
            self.calc_area.insertPlainText(f" {char} ")
        else:
            self.calc_area.insertPlainText(char)
        # self.calc_area.setTextCursor(0)
        print(repr(self.calc_area.toPlainText()))

    def calc(self):
        global ANS
        try:
            ANS = eval(str(self.calc_area.toPlainText()))
            self.calc_area.clear()
            self.calc_area.setPlainText(str(ANS))
            self.to_sto()
        except SyntaxError or ZeroDivisionError:
            self.calc_area.clear()
            self.calc_area.setPlainText("Error")
        finally:
            self.showing_ans = True

    def ac(self):
        self.calc_area.clear()
        self.showing_ans = False
    
    def del_calc(self):
        if self.showing_ans:
            self.calc_area.clear()
        else:
            text_cursor = self.calc_area.textCursor()
            text_cursor.deletePreviousChar()
    
    def reset_vars(self):
        global A, B, C, D, E, F, M, X, Y, Z, ANS
        message_box = ResetPopup(self)
        message_box.show()
        # if message_box.buttons.accepted():
        #     A = B = C = D = E = F = M = X = Y = Z = ANS = 0
        #     self.to_sto()

    def about(self):
        message_box = QDialog(self)
        ui = AboutDialogUI()
        ui.setupUi(message_box)
        message_box.show()


class ScientificCalcWidget(ScientificCalcUI, QWidget):
    def __init__(self, MainWindow) -> None:
        super().__init__()
        self.setupUi(self, MainWindow)
        self.MainWindow = MainWindow
        self.num_0.clicked.connect(partial(self.insert_chars, "0"))
        self.num_1.clicked.connect(partial(self.insert_chars, "1"))
        self.num_2.clicked.connect(partial(self.insert_chars, "2"))
        self.num_3.clicked.connect(partial(self.insert_chars, "3"))
        self.num_4.clicked.connect(partial(self.insert_chars, "4"))
        self.num_5.clicked.connect(partial(self.insert_chars, "5"))
        self.num_6.clicked.connect(partial(self.insert_chars, "6"))
        self.num_7.clicked.connect(partial(self.insert_chars, "7"))
        self.num_8.clicked.connect(partial(self.insert_chars, "8"))
        self.num_9.clicked.connect(partial(self.insert_chars, "9"))
        self.num_dot.clicked.connect(partial(self.insert_chars, "."))
        self.btn_pi.clicked.connect(partial(self.insert_chars, "π"))
        self.btn_comma.clicked.connect(partial(self.insert_chars, ","))
        self.btn_e.clicked.connect(partial(self.insert_chars, "\u212f"))
        self.btn_divide.clicked.connect(partial(self.insert_chars, "/"))
        self.btn_plus.clicked.connect(partial(self.insert_chars, "+"))
        self.btn_minus.clicked.connect(partial(self.insert_chars, "-"))
        self.btn_times.clicked.connect(partial(self.insert_chars, "*"))
        self.btn_left.clicked.connect(partial(self.insert_chars, "("))
        self.btn_right.clicked.connect(partial(self.insert_chars,")")) 
        self.btn_sqrt.clicked.connect(partial(self.insert_chars, "√("))
        self.btn_pow.clicked.connect(partial(self.insert_chars, "^"))
        self.btn_factorial.clicked.connect(partial(self.insert_chars, "!"))
        self.btn_eq.clicked.connect(self.calc)
        self.btn_ac.clicked.connect(self.ac) 
        self.btn_del.clicked.connect(self.del_calc)
        self.btn_sin.clicked.connect(partial(self.insert_chars, "sin("))
        self.btn_cos.clicked.connect(partial(self.insert_chars, "cos("))
        self.btn_tan.clicked.connect(partial(self.insert_chars, "tan("))
        self.btn_asin.clicked.connect(partial(self.insert_chars, "arcsin("))
        self.btn_acos.clicked.connect(partial(self.insert_chars, "arccos("))
        self.btn_atan.clicked.connect(partial(self.insert_chars, "arctan("))
        self.btn_sinh.clicked.connect(partial(self.insert_chars, "sinh("))
        self.btn_cosh.clicked.connect(partial(self.insert_chars, "cosh("))
        self.btn_tanh.clicked.connect(partial(self.insert_chars, "tanh("))
        self.btn_asinh.clicked.connect(partial(self.insert_chars, "arcsinh("))
        self.btn_acosh.clicked.connect(partial(self.insert_chars, "arccosh("))
        self.btn_atanh.clicked.connect(partial(self.insert_chars, "arctanh("))
        self.btn_log.clicked.connect(partial(self.insert_chars, "log("))
        self.btn_ln.clicked.connect(partial(self.insert_chars, "ln("))
        self.btn_gcd.clicked.connect(partial(self.insert_chars, "gcd("))
        self.btn_lcm.clicked.connect(partial(self.insert_chars, "lcm("))
        

    def set_scientific(self):
        self.MainWindow.setMinimumSize(QSize(586, 567))
        self.MainWindow.setWindowTitle("Scientific mode")
        self.MainWindow.menubar.action_ANS.triggered.connect(partial(self.insert_chars, "ANS"))
        self.MainWindow.menubar.action_rcl_A.triggered.connect(partial(self.insert_chars, "A"))
        self.MainWindow.menubar.action_rcl_B.triggered.connect(partial(self.insert_chars, "B"))
        self.MainWindow.menubar.action_rcl_C.triggered.connect(partial(self.insert_chars, "C"))
        self.MainWindow.menubar.action_rcl_D.triggered.connect(partial(self.insert_chars, "D"))
        self.MainWindow.menubar.action_rcl_E.triggered.connect(partial(self.insert_chars, "E"))
        self.MainWindow.menubar.action_rcl_F.triggered.connect(partial(self.insert_chars, "F"))
        self.MainWindow.menubar.action_rcl_M.triggered.connect(partial(self.insert_chars, "M"))
        self.MainWindow.menubar.action_rcl_X.triggered.connect(partial(self.insert_chars, "X"))
        self.MainWindow.menubar.action_rcl_Y.triggered.connect(partial(self.insert_chars, "Y"))
        self.MainWindow.menubar.action_rcl_Z.triggered.connect(partial(self.insert_chars, "Z"))
        self.MainWindow.menubar.action_sto_A.triggered.connect(partial(self.sto_var, "A"))
        self.MainWindow.menubar.action_sto_B.triggered.connect(partial(self.sto_var, "B"))
        self.MainWindow.menubar.action_sto_C.triggered.connect(partial(self.sto_var, "C"))
        self.MainWindow.menubar.action_sto_D.triggered.connect(partial(self.sto_var, "D"))
        self.MainWindow.menubar.action_sto_E.triggered.connect(partial(self.sto_var, "E"))
        self.MainWindow.menubar.action_sto_F.triggered.connect(partial(self.sto_var, "F"))
        self.MainWindow.menubar.action_sto_M.triggered.connect(partial(self.sto_var, "M"))
        self.MainWindow.menubar.action_sto_X.triggered.connect(partial(self.sto_var, "X"))
        self.MainWindow.menubar.action_sto_Y.triggered.connect(partial(self.sto_var, "Y"))
        self.MainWindow.menubar.action_sto_Z.triggered.connect(partial(self.sto_var, "Z"))
        self.MainWindow.menubar.action_reset.triggered.connect(self.reset_vars)
        self.MainWindow.menubar.menu_variables.setEnabled(True)

    def calc(self):
        self.to_sto()

    def to_sto(self):
        print(
            {
                "A": A,
                "B": B,
                "C": C,
                "D": D,
                "E": E,
                "F": F,
                "M": M,
                "X": X,
                "Y": Y,
                "Z": Z,
                "ANS": ANS
            }
        )
        with open("sto.json", "w") as sto_file:
            json.dump({
                "A": A,
                "B": B,
                "C": C,
                "D": D,
                "E": E,
                "F": F,
                "M": M,
                "X": X,
                "Y": Y,
                "Z": Z,
                "ANS": ANS
            }, sto_file)

    def sto_var(self, var):
        # global A, B, C, D, E, F, M, X, Y, Z
        try:
            global A, B, C, D, E, F, M, X, Y, Z
            value = eval(str(self.calc_area.toPlainText()))
            print(value)
            self.calc()
            match var:
                case "A": 
                    A = value
                case "B":
                    B = value
                case "C":
                    C = value
                case "D":
                    D = value
                case "E":
                    E = value
                case "F":
                    F = value
                case "M":
                    M = value
                case "X":
                    X = value
                case "Y":
                    Y = value
                case "Z":
                    Z = value
        finally:
            self.to_sto()

    def insert_chars(self, char: str):
        if "Error" in self.calc_area.toPlainText():
            self.calc_area.clear()
        elif char in ["+", "-", "*", "/"]:
            self.calc_area.insertPlainText(f" {char} ")
        else:
            self.calc_area.insertPlainText(char)
        # self.calc_area.setTextCursor(0)
        print(repr(self.calc_area.toPlainText()))

    def reset_vars(self):
        global A, B, C, D, E, F, M, X, Y, Z, ANS
        message_box = ResetPopup(self)
        message_box.show()

    def del_calc(self):
        if "Error" in self.calc_area.toPlainText():
            self.calc_area.clear()
        else:
            text_cursor = self.calc_area.textCursor()
            text_cursor.deletePreviousChar()

    def ac(self):
        self.calc_area.clear()

class Converter:
    def __init__(self, input_value, unit_type, input_unit, output_unit) -> None:
        self.AREA = "Area"
        self.ENERGY = "Energy"
        self.LENGTH = "Length"
        self.TEMPERATURE = "Temperature"
        self.VOLUME = "Volume"
        self.WEIGHT = "Weight"
        self.SPEED = "Speed"
        self.TIME = "Time"
        self.POWER = "Power"
        self.PRESSURE = "Pressure"
        self.ANGLE = "Angle"
        self.DATA = "Data"
        self.FORCE = "Force"
        self.input_value = input_value
        self.unit_type = unit_type
        self.input_unit = input_unit
        self.output_unit = output_unit
        self.output_value = 0
        match unit_type:
            case self.AREA: self.output_value = self.convert_area()
            case self.ENERGY: self.output_value = self.convert_energy()
            case self.LENGTH: self.output_value = self.convert_length()
            case self.TEMPERATURE: self.output_value = self.convert_temperature()
            case self.VOLUME: self.output_value = self.convert_volume()
            case self.WEIGHT: self.output_value = self.convert_weight()
            case self.SPEED: self.output_value = self.convert_speed()
            case self.TIME: self.output_value = self.convert_time()
            case self.POWER: self.output_value = self.convert_power()
            case self.PRESSURE: self.output_value = self.convert_pressure()
            case self.ANGLE: self.output_value = self.convert_angle()
            case self.DATA: self.output_value = self.convert_data()
            case self.FORCE: self.output_value = self.convert_force()
        

    def get_result(self):
        return self.output_value

    
    def convert_length(self):
        def to_meters(input_value, input_unit):
            try:
                results = {
                    'Centimeters': input_value *.01, 
                    'Foot/Feet': input_value * .3048, 
                    'Inches': input_value * .0254,
                    'Kilometers': input_value * 1000,
                    'Meters ': input_value,
                    'Micrometers': input_value / 1000000,
                    'Miles': input_value * 1609.34, 
                    'Milimeters': input_value * .001, 
                    'Nanometers': input_value / 1000000000,
                    'Yards': input_value * .9144
                }
                return results[input_unit]
            except TypeError:
                return 0
        
        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_meters = to_meters(input_value, input_unit)
                results = {
                    'Centimeters': value_in_meters * 100, 
                    'Foot/Feet': value_in_meters * 1/.3048, 
                    'Inches': value_in_meters * 1/.0254, 
                    'Kilometers': value_in_meters * .001, 
                    'Meters ': value_in_meters * 1, 
                    'Micrometers': value_in_meters * 10**6,
                    'Miles': value_in_meters * 1/1609.344, 
                    'Milimeters': value_in_meters * 1000, 
                    'Nanometers': value_in_meters * 10**9,
                    'Yards': value_in_meters * 1/.9144
                }
                return results[output_unit]
            except TypeError:
                return 0

        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_area(self):
        def to_sq_meters(input_value, input_unit):
            try:
                results = {
                    "Acres": input_value * 4047,
                    "Hectares": input_value * 10000,
                    "Square inches": input_value / 1550.0031,
                    "Square feet": input_value / 10.764,
                    "Square kilometers": input_value * 1000,
                    "Square meters": input_value,
                    "Square millimeters": input_value / 1000000,
                    "Square miles": input_value * 2.59 * 10**6,
                    "Square yards": input_value / 1.196
                }
                return results[input_unit]
            except TypeError:
                return 0

        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_meters = to_sq_meters(input_value, input_unit)
                results = {
                    "Acres": value_in_meters / 4047,
                    "Hectares": value_in_meters / 10000,
                    "Square inches": value_in_meters * 1550.0031,
                    "Square feet": value_in_meters * 10.764,
                    "Square kilometers": value_in_meters / 1000,
                    "Square meters": value_in_meters,
                    "Square millimeters": value_in_meters * 1000000,
                    "Square miles": value_in_meters / (2.59 * 10**6),
                    "Square yards": value_in_meters * 1.196
                }
                return results[output_unit]
            except:
                return 0
        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_volume(self):
        def to_cubic_meters(input_value, input_unit):
            results = {
                "Cubic centimeters": input_value / 1000000,
                "Cubic feet": input_value / 35.3147,
                "Cubic inches": input_value / 61023.7,
                "Cubic kilometers": input_value * 1000000000,
                "Cubic meters": input_value,
                "Cubic millimeters": input_value / 1000000000,
                "Cubic yards": input_value / 1.30795,
                "Liters": input_value / 1000,
                "Milliliters": input_value / 1000000,
                "Gallon (US)": input_value / 264.172,
                "Quarts (US)": input_value / 1056.69,
                "Pints (US)": input_value / 2113.38,
                "Cups (US)": input_value / 4226.75,
                "Fluid ounces (US)": input_value / 33814,
                "Tablespoons (US)": input_value / 67628,
                "Teaspoons (US)": input_value / 202884,
                "Gallon (UK)": input_value / 219.969,
                "Quarts (UK)": input_value / 879.877,
                "Pints (UK)": input_value / 1759.75,
                "Cups (UK)": input_value / 3519.51,
                "Fluid ounces (UK)": input_value / 28413.8,
                "Tablespoons (UK)": input_value / 56827.5,
                "Teaspoons (UK)": input_value / 170482,
            }
            return results[input_unit]

        def to_all(input_value, input_unit, output_unit):
            value_in_cubic_meters = to_cubic_meters(input_value, input_unit)
            results = {
                "Cubic centimeters": value_in_cubic_meters * 1000000,
                "Cubic feet": value_in_cubic_meters * 35.3147,
                "Cubic inches": value_in_cubic_meters * 61023.7,
                "Cubic kilometers": value_in_cubic_meters / 1000000000,
                "Cubic meters": value_in_cubic_meters,
                "Cubic millimeters": value_in_cubic_meters * 1000000000,
                "Cubic yards": value_in_cubic_meters * 1.30795,
                "Liters": value_in_cubic_meters * 1000,
                "Milliliters": value_in_cubic_meters * 1000000,
                "Gallon (US)": value_in_cubic_meters * 264.172,
                "Quarts (US)": value_in_cubic_meters * 1056.69,
                "Pints (US)": value_in_cubic_meters * 2113.38,
                "Cups (US)": value_in_cubic_meters * 4226.75,
                "Fluid ounces (US)": value_in_cubic_meters * 33814,
                "Tablespoons (US)": value_in_cubic_meters * 67628,
                "Teaspoons (US)": value_in_cubic_meters * 202884,
                "Gallon (UK)": value_in_cubic_meters * 219.969,
                "Quarts (UK)": value_in_cubic_meters * 879.877,
                "Pints (UK)": value_in_cubic_meters * 1759.75,
                "Cups (UK)": value_in_cubic_meters * 3519.51,
                "Fluid ounces (UK)": value_in_cubic_meters * 28413.8,
                "Tablespoons (UK)": value_in_cubic_meters * 56827.5,
                "Teaspoons (UK)": value_in_cubic_meters * 170482,
            }
            return results[output_unit]

        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_weight(self):
        def to_kg(input_value, input_unit):
            try:
                results = {
                    "Carats": input_value / 5000,
                    "Grams": input_value / 1000,
                    "Kilograms": input_value,
                    "Metric tonnes": input_value * 1000,
                    "Ounces": input_value / 35.274,
                    "Pounds": input_value / 2.205,
                }
                return results[input_unit]
            except TypeError:
                return 0

        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_kg = to_kg(input_value, input_unit)
                results = {
                    "Carats": value_in_kg * 5000,
                    "Grams": value_in_kg * 1000,
                    "Kilograms": value_in_kg,
                    "Metric tonnes": value_in_kg / 1000,
                    "Ounces": value_in_kg * 35.274,
                    "Pounds": value_in_kg * 2.205,
                }
                return results[output_unit]
            except TypeError:
                return 0

        return to_all(self.input_value, self.input_unit, self.output_unit)


    def convert_temperature(self):
        def to_celsius(input_value, input_unit):
            try:
                all_results = {
                    "Fahrenheit": (input_value - 32) * 5 / 9,
                    "Kelvin": input_value - 273.15,
                    "Celsius": input_value,
                }
                return all_results[input_unit]
            except TypeError:
                return 0

        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_celsius = to_celsius(input_value, input_unit)
                all_results = {
                    "Fahrenheit": value_in_celsius * 9 / 5 + 32,
                    "Kelvin": value_in_celsius + 273.15,
                    "Celsius": value_in_celsius,
                }
                return all_results[output_unit]
            except TypeError:
                return 0
                        
        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_energy(self):
        def to_joules(input_value, input_unit):
            try:
                all_results = {
                    "Ampere-hours": input_value * 3600,
                    "British thermal units": input_value * 1055,
                    "Calories": input_value * 4.184,
                    "Foot-pounds": input_value * 1.35582,
                    "Joules": input_value,
                    "Kilojoules": input_value * 1000,
                    "Kilocalories": input_value * 4184,
                    "Kilowatt-hours": input_value * 3600000,
                    "Megawatt-hours": input_value * 3600000000,
                    "Milliamperes-hours": input_value / 3.6,
                    "Electron volts": input_value * 1.60218e-19,
                    "Therms (EC)": input_value * 105505600,
                    "Watt-hours": input_value * 3600,
                }
                return all_results[input_unit]
            except TypeError:
                return 0

        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_joules = to_joules(input_value, input_unit)
                all_results = {
                    "Ampere-hours": value_in_joules / 3600,
                    "British thermal units": value_in_joules / 1055,
                    "Calories": value_in_joules / 4.184,
                    "Electron volts": value_in_joules / 1.60218e-19,
                    "Foot-pounds": value_in_joules / 1.35582,
                    "Joules": value_in_joules,
                    "Kilojoules": value_in_joules / 1000,
                    "Kilocalories": value_in_joules / 4184,
                    "Kilowatt-hours": value_in_joules / 3600000,
                    "Megawatt-hours": value_in_joules / 3600000000,
                    "Milliamperes-hours": value_in_joules * 3.6,
                    "Therms (EC)": value_in_joules / 105505600,
                    "Watt-hours": value_in_joules / 3600,
                }
                return all_results[output_unit]
            except TypeError:
                return 0
        
        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_speed(self):
        def to_meters_per_second(input_value, input_unit):
            try:
                all_results = {
                    "Feet per second": input_value * 3.281,
                    "Inches per second": input_value * 39.37,
                    "Kilometers per hour": input_value * 3.6,
                    "Kilometers per second": input_value / 1000,
                    "Knots": input_value * 1.944,
                    "Mach": input_value * 1225,
                    "Meters per second": input_value,
                    "Miles per hour": input_value * 2.237,
                    "Miles per second": input_value / 1609,
                    "Speed of light": input_value * 299792458,
                    "Speed of sound": input_value * 340.29,
                    "Yards per second": input_value * 1.094,
                }
                return all_results[input_unit]
            except TypeError:
                return 0

        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_meters_per_second = to_meters_per_second(input_value, input_unit)
                all_results = {
                    "Inches per second": value_in_meters_per_second / 39.37,
                    "Kilometers per hour": value_in_meters_per_second / 3.6,
                    "Kiilometers per second": value_in_meters_per_second * 1000,
                    "Meters per second": value_in_meters_per_second,
                    "Kilometers per hour": value_in_meters_per_second / 3.6,
                    "Miles per hour": value_in_meters_per_second / 2.237,
                    "Feet per second": value_in_meters_per_second / 3.281,
                    "Knots": value_in_meters_per_second / 1.944,
                    "Mach": value_in_meters_per_second / 1225,
                    "Speed of light": value_in_meters_per_second / 299792458,
                    "Speed of sound": value_in_meters_per_second / 340.29,
                    "Yards per second": value_in_meters_per_second / 1.094,
                }
                return all_results[output_unit]
            except TypeError:
                return 0

        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_time(self):
        def to_seconds(input_value, input_unit):
            try:
                all_results = {
                    "Microseconds": input_value / 1000000,
                    "Milliseconds": input_value / 1000,
                    "Seconds": input_value,
                    "Minutes": input_value * 60,
                    "Hours": input_value * 3600,
                    "Days": input_value * 86400,
                    "Weeks": input_value * 604800,
                    "Months": input_value * 2628000,
                    "Years": input_value * 31536000,
                }
                return all_results[input_unit]
            except TypeError:
                return 0

        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_seconds = to_seconds(input_value, input_unit)
                all_results = {
                    "Microseconds": value_in_seconds * 1000000,
                    "Milliseconds": value_in_seconds * 1000,
                    "Seconds": value_in_seconds,
                    "Minutes": value_in_seconds / 60,
                    "Hours": value_in_seconds / 3600,
                    "Days": value_in_seconds / 86400,
                    "Weeks": value_in_seconds / 604800,
                    "Months": value_in_seconds / 2628000,
                    "Years": value_in_seconds / 31536000,
                }
                return all_results[output_unit]
            except TypeError:
                return 0

        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_pressure(self):
        def to_pascals(input_value, input_unit):
            try:
                all_results = {
                    "Atmospheres": input_value * 101325,
                    "Bars": input_value * 100000,
                    "Dynes per square centimeter": input_value * 10000000,
                    "Feet of water": input_value * 2989.07,
                    "Feet of mercury": input_value * 40679.7,
                    "Inches of water": input_value * 249.082,
                    "Inches of mercury": input_value * 3386.39,
                    "Kilograms per square centimeter": input_value * 98066.5,
                    "Kilograms per square meter": input_value * 9.80665,
                    "Kilopascals": input_value * 1000,
                    "Kips per square inch": input_value * 6894757,
                    "Megabars": input_value / 10,
                    "Megapascals": input_value / 1000,
                    "Millibars": input_value * 100,
                    "Millimeters of mercury": input_value * 133.322,
                    "Millimeters of water": input_value * 9.80665,
                    "Newtons per square centimeter": input_value * 98066.5,
                    "Newtons per square meter": input_value * 9.80665,
                    "Pascals": input_value,
                    "Pounds per square foot": input_value * 47.8803,
                    "Pounds per square inch": input_value * 6894.76,
                    "Pounds per square inch (absolute)": input_value * 6894.76,
                    "Pounds per square inch (gauge)": input_value * 6894.76,
                    "Pounds per square inch (technical)": input_value * 6894.76,
                    "Pounds per square inch (water)": input_value * 6894.76,
                    "Torr": input_value * 133.322,
                }
                return all_results[input_unit]
            except TypeError:
                return 0

        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_pascals = to_pascals(input_value, input_unit)
                all_results = {
                    "Atmospheres": value_in_pascals / 101325,
                    "Bars": value_in_pascals / 100000,
                    "Centimeters of mercury": value_in_pascals / 1333.22,
                    "Feet of water": value_in_pascals / 2989.07,
                    "Feet of mercury": value_in_pascals / 40679.7,
                    "Inches of water": value_in_pascals / 249.082,
                    "Inches of mercury": value_in_pascals / 3386.39,
                    "Kilobars": value_in_pascals / 100,
                    "Kilograms per square centimeter": value_in_pascals / 98066.5,
                    "Kilograms per square meter": value_in_pascals / 9.80665,
                    "Kilopascals": value_in_pascals / 1000,
                    "Kips per square inch": value_in_pascals / 6894757,
                    "Megabars": value_in_pascals * 10,
                    "Megapascals": value_in_pascals * 1000,
                    "Millibars": value_in_pascals / 100,
                    "Millimeters of mercury": value_in_pascals / 133.322,
                    "Millimeters of water": value_in_pascals / 9.80665,
                    "Newtons per square centimeter": value_in_pascals / 98066.5,
                    "Newtons per square meter": value_in_pascals / 9.80665,
                    "Pascals": value_in_pascals,
                    "Pounds per square foot": value_in_pascals / 47.8803,
                    "Pounds per square inch": value_in_pascals / 6894.76,
                    "Pounds per square inch (absolute)": value_in_pascals / 6894.76,
                    "Pounds per square inch (gauge)": value_in_pascals / 6894.76,
                    "Pounds per square inch (technical)": value_in_pascals / 6894.76,
                    "Pounds per square inch (water)": value_in_pascals / 6894.76,
                    "Torr": value_in_pascals / 133.322,
                }
                return all_results[output_unit]
            except TypeError:
                return 0

        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_power(self):
        def to_watts(input_value, input_unit):
            try:
                all_results = {
                   "Boilers horsepower": input_value * 9809.5,
                    "Electrical horsepower": input_value * 746,
                    "Foot-pounds per minute": input_value * 0.022596,
                    "Foot-pounds per second": input_value * 1.35582,
                    "Gigawatts" : input_value * 1000000000,
                    "Horsepower (boiler)": input_value * 9809.5,
                    "Horsepower (electric)": input_value * 746,
                    "Horsepower (metric)": input_value * 735.49875,
                    "Horsepower (UK)": input_value * 745.69987158227022,
                    "Horsepower (water)": input_value * 746,
                    "Horsepower (US)": input_value * 745.69987158227022,
                    "Kilowatts": input_value * 1000,
                    "Megawatts": input_value * 1000000,
                    "Metric horsepower": input_value * 735.49875,
                    "Metric tons of TNT": input_value * 4184000000,
                    "Microwatts": input_value * 0.000001,
                    "Milliwatts": input_value * 0.001,
                    "Nanowatts": input_value * 0.000000001,
                    "Petawatts": input_value * 1000000000000000,
                    "Picojoules per second": input_value * 0.000000001,
                    "Terawatts": input_value * 1000000000000,
                    "Watts": input_value,
                }
                return all_results[input_unit]
            except TypeError:
                return 0
        
        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_watts = to_watts(input_value, input_unit)
                all_results = {
                        "Boilers horsepower": value_in_watts / 9809.5,
                        "Electrical horsepower": value_in_watts / 746,
                        "Foot-pounds per minute": value_in_watts / 0.022596,
                        "Foot-pounds per second": value_in_watts / 1.35582,
                        "Gigawatts" : value_in_watts / 1000000000,
                        "Horsepower (boiler)": value_in_watts / 9809.5,
                        "Horsepower (electric)": value_in_watts / 746,
                        "Horsepower (metric)": value_in_watts / 735.49875,
                        "Horsepower (UK)": value_in_watts / 745.69987158227022,
                        "Horsepower (water)": value_in_watts / 746,
                        "Horsepower (US)": value_in_watts / 745.69987158227022,
                        "Kilowatts": value_in_watts / 1000,
                        "Megawatts": value_in_watts / 1000000,
                        "Metric horsepower": value_in_watts / 735.49875,
                        "Metric tons of TNT": value_in_watts / 4184000000,
                        "Microwatts": value_in_watts / 0.000001,
                        "Milliwatts": value_in_watts / 0.001,
                        "Nanowatts": value_in_watts / 0.000000001,
                        "Petawatts": value_in_watts / 1000000000000000,
                        "Picojoules per second": value_in_watts / 0.000000001,
                        "Terawatts": value_in_watts / 1000000000000,
                        "Watts": value_in_watts,            
                    }
                return all_results[output_unit]
            except TypeError:
                return 0    

        return to_all(self.input_value, self.input_unit, self.output_unit)    

    def convert_angle(self):
        def to_radians(input_value, input_unit):
            try:
                all_results = {
                    "Degrees": input_value * 0.0174533,
                    "Gradians": input_value * 0.01570796,\
                    "Minutes": input_value * 0.000290888,
                    "Radians": input_value,
                    "Seconds": input_value * 0.00000484814,
                }
                return all_results[input_unit]
            except TypeError:
                return 0
        
        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_radians = to_radians(input_value, input_unit)
                all_results = {
                    "Degrees": value_in_radians / 0.0174533,
                    "Gradians": value_in_radians / 0.01570796,
                    "Minutes": value_in_radians / 0.000290888,
                    "Radians": value_in_radians,
                    "Seconds": value_in_radians / 0.00000484814,
                }
                return all_results[output_unit]
            except TypeError:
                return 0    

        return to_all(self.input_value, self.input_unit, self.output_unit)

    def convert_force(self):
        def to_newtons(input_value, input_unit):
            try:
                all_results = {
                    "Dynes": input_value * 0.00001,
                    "Kips": input_value * 4448.2216152605,
                    "Kiloponds": input_value * 9.80665,
                    "Kilograms-force": input_value * 9.80665,
                    "Newtons": input_value,
                    "Poundals": input_value * 0.138255,
                    "Pounds-force": input_value * 4.4482216152605,
                    "Tonnes-force": input_value * 9806.65,
                }
                return all_results[input_unit]
            except TypeError:
                return 0
        
        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_newtons = to_newtons(input_value, input_unit)
                all_results = {
                    "Dynes": value_in_newtons / 0.00001,
                    "Kips": value_in_newtons / 4448.2216152605,
                    "Kiloponds": value_in_newtons / 9.80665,
                    "Kilograms-force": value_in_newtons / 9.80665,
                    "Newtons": value_in_newtons,
                    "Poundals": value_in_newtons / 0.138255,
                    "Pounds-force": value_in_newtons / 4.4482216152605,
                    "Tonnes-force": value_in_newtons / 9806.65,
                }
                return all_results[output_unit]
            except TypeError:
                return 0

        return to_all(self.input_value, self.input_unit, self.output_unit)
        
    def convert_data(self):
        def to_bits(input_value, input_unit):
            try:
                all_results = {
                    "Bits": input_value,
                    "Bytes": input_value * 8,
                    "Gigabits": input_value * 2**30,
                    "Gigabytes": input_value * 2**30 * 8,
                    "Kilobits": input_value * 2**10,
                    "Kilobytes": input_value * 2**10 * 8,
                    "Megabits": input_value * 2**20,
                    "Megabytes": input_value * 2**20 * 8,
                    "Petabits": input_value * 2**50,
                    "Petabytes": input_value * 2**50 * 8,
                    "Terabits": input_value * 2**40,
                    "Terabytes": input_value * 2**40 * 8,
                }
                return all_results[input_unit]
            except TypeError:
                return 0
        
        def to_all(input_value, input_unit, output_unit):
            try:
                value_in_bits = to_bits(input_value, input_unit)
                all_results = {
                    "Bits": value_in_bits,
                    "Bytes": value_in_bits / 8,
                    "Gigabits": value_in_bits / 2**30,
                    "Gigabytes": value_in_bits / 2**30 / 8,
                    "Kilobits": value_in_bits / 2**10,
                    "Kilobytes": value_in_bits / 2**10 / 8,
                    "Megabits": value_in_bits / 2**20,
                    "Megabytes": value_in_bits / 2**20 / 8,
                    "Petabits": value_in_bits / 2**50,
                    "Petabytes": value_in_bits / 2**50 / 8,
                    "Terabits": value_in_bits / 2**40,
                    "Terabytes": value_in_bits / 2**40 / 8,
                }
                return all_results[output_unit]
            except TypeError:
                return 0

        return to_all(self.input_value, self.input_unit, self.output_unit)


class MeasureConverterWidget(MeasurementConverterUI, QWidget):
    def __init__(self, MainWindow: QMainWindow) -> None:
        super().__init__()
        self.setupUi(self, MainWindow)
        self.MainWindow = MainWindow
        self.num_0.clicked.connect(partial(self.insert_chars, "0"))
        self.num_1.clicked.connect(partial(self.insert_chars, "1"))
        self.num_2.clicked.connect(partial(self.insert_chars, "2"))
        self.num_3.clicked.connect(partial(self.insert_chars, "3"))
        self.num_4.clicked.connect(partial(self.insert_chars, "4"))
        self.num_5.clicked.connect(partial(self.insert_chars, "5"))
        self.num_6.clicked.connect(partial(self.insert_chars, "6"))
        self.num_7.clicked.connect(partial(self.insert_chars, "7"))
        self.num_8.clicked.connect(partial(self.insert_chars, "8"))
        self.num_9.clicked.connect(partial(self.insert_chars, "9"))
        self.num_dot.clicked.connect(partial(self.insert_chars, "."))
        self.btn_switch.clicked.connect(self.swap_units)
        self.btn_convert.clicked.connect(self.convert)
        self.btn_convert.setVisible(False)
        self.btn_ac.clicked.connect(self.ac)
        self.btn_del.clicked.connect(self.del_calc)
        self.list_types_of_units()
        self.first_unit_combobox.setEnabled(False)
        self.second_unit_combobox.setEnabled(False)
        self.first_unit_box.setEnabled(False)
        self.input_frame.setEnabled(False)
        self.types_tuple = tuple(self.types_list)
        self.unit_types_combobox.activated.connect(self.unit_types_chosen)
        self.first_unit_combobox.activated.connect(self.convert)
        self.second_unit_combobox.activated.connect(self.convert)
        self.second_unit_combobox.activated.connect(self.enable_input)
        try:
            self.units_tuple = self.units_list[self.types_tuple[self.unit_types_combobox.currentIndex()]]
        except AttributeError:
            pass

    def unit_types_chosen(self):
        self.list_units(self.types_tuple[self.unit_types_combobox.currentIndex()])
        self.convert()

    def enable_input(self):
        self.first_unit_box.setEnabled(True)
        self.input_frame.setEnabled(True)

    def list_types_of_units(self):
        self.types_list = {
            "Area": QPixmap(f"{ICON_PATH}/area.png"),
            "Angle": QPixmap(f"{ICON_PATH}/angle.png"),
            "Data": QPixmap(f"{ICON_PATH}/data.png"),
            "Energy": QPixmap(f"{ICON_PATH}/energy.png"),
            "Force": QPixmap(f"{ICON_PATH}/force.png"),
            "Frequency": QPixmap(f"{ICON_PATH}/frequency.png"),
            "Length": QPixmap(f"{ICON_PATH}/length.png"),
            "Pressure": QPixmap(f"{ICON_PATH}/pressure.png"),
            "Power": QPixmap(f"{ICON_PATH}/power.png"),
            "Speed": QPixmap(f"{ICON_PATH}/speed.png"),
            "Temperature": QPixmap(f"{ICON_PATH}/temperature.png"),
            "Time": QPixmap(f"{ICON_PATH}/time.png"),
            "Volume": QPixmap(f"{ICON_PATH}/volume.png"),
            "Weight": QPixmap(f"{ICON_PATH}/weight.png"),          
        }
        self.unit_types_combobox.clear()
        self.types_tuple = tuple(self.types_list)
        for unit_type in (self.types_tuple):
            self.unit_types_combobox.addItem(self.types_list[unit_type], unit_type)

    def list_units(self, unit_type):
        self.first_unit_combobox.clear()
        self.second_unit_combobox.clear()
        for item in self.units_list[unit_type]:
            self.first_unit_combobox.addItem(item)
            self.second_unit_combobox.addItem(item)
        self.first_unit_combobox.setCurrentIndex(0)
        self.second_unit_combobox.setCurrentIndex(0)
        self.first_unit_combobox.setEnabled(True)
        self.second_unit_combobox.setEnabled(True)
        self.enable_input()
    
    def set_unit_converter(self):
        self.MainWindow.setWindowTitle("Measurement units converter")
        self.MainWindow.setMinimumSize(730, 444)
        self.MainWindow.menubar.menu_variables.setEnabled(False)

    def convert(self):
        # match self.unit_types_combobox.currentIndex():
        #     case 0:
        try:
            input_value = float(self.first_unit_box.toPlainText()) 
        except ValueError:
            input_value = None
        unit_type = self.types_tuple[self.unit_types_combobox.currentIndex()]
        units_tuple = self.units_list[self.types_tuple[self.unit_types_combobox.currentIndex()]]
        input_unit = units_tuple[self.first_unit_combobox.currentIndex()]
        output_unit = units_tuple[self.second_unit_combobox.currentIndex()]
        convert_obj = Converter(input_value, unit_type, input_unit, output_unit)
        try:
            result = f"{convert_obj.get_result():4f}".rstrip("0").rstrip(".")
        except TypeError:
            result = ""
        self.second_unit_box.clear()
        self.second_unit_box.setPlainText(result)
    
    def swap_units(self):
        first_index = self.first_unit_combobox.currentIndex()
        second_index = self.second_unit_combobox.currentIndex()
        first_index, second_index = second_index, first_index
        self.first_unit_combobox.setCurrentIndex(first_index)
        self.second_unit_combobox.setCurrentIndex(second_index)
        self.convert()

    def insert_chars(self, char: str):
        self.first_unit_box.insertPlainText(char)
        self.convert()

    def ac(self):
        self.first_unit_box.clear()
        self.second_unit_box.clear()
        self.convert()

    def del_calc(self):
        text_cursor = self.first_unit_box.textCursor()
        text_cursor.deletePreviousChar()
        self.convert()

class CurrencyConverterWidget(QWidget):
    def __init__(self, MainWindow) -> None:
        super().__init__()

class CalcMainWindow(QMainWindow, CalcUI):
    # global ANS, A, B, C, D, E, F, M, X, Y, Z
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.basic_calc = BasicCalcWidget(self)
        self.stacked_widget.addWidget(self.basic_calc)
        self.scientific_calc = ScientificCalcWidget(self)
        self.stacked_widget.addWidget(self.scientific_calc)
        self.unit_converter = MeasureConverterWidget(self)
        self.stacked_widget.addWidget(self.unit_converter)
        match DEFAULT_MODE:
            case 0: self.set_basic_mode()
            case 1: self.set_scientific_mode()
            case 2: self.set_unit_converter_mode()
        self.menubar.action_basic.triggered.connect(self.set_basic_mode)
        self.menubar.action_scientific.triggered.connect(self.set_scientific_mode)
        self.menubar.action_conversion.triggered.connect(self.set_unit_converter_mode)

    def set_basic_mode(self):
        self.basic_calc.set_basic()
        self.stacked_widget.setCurrentIndex(0)

    def set_scientific_mode(self):
        self.scientific_calc.set_scientific()
        self.stacked_widget.setCurrentIndex(1)

    def set_unit_converter_mode(self):
        self.unit_converter.set_unit_converter()
        self.stacked_widget.setCurrentIndex(2)



app = QApplication()
main = CalcMainWindow()
main.show()
sys.exit(app.exec())

# if __name__ == "main":
#     app = QApplication()
#     main = CalcMainWindow()
#     main.show()
#     sys.exit(app.exec())
