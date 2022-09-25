import sys
from functools import partial
import json
from unittest.mock import DEFAULT

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize
# from calc import Ui_MainWindow
from calc_ui import CalcUI, ResetPopup, BasicCalcUI, ScientificCalcUI
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
MENU_FONT_SIZE = THEME["menu-font-size"]
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
        self.btn_divide.clicked.connect(partial(self.insert_chars, "/"))
        self.btn_plus.clicked.connect(partial(self.insert_chars, "+"))
        self.btn_minus.clicked.connect(partial(self.insert_chars, "-"))
        self.btn_times.clicked.connect(partial(self.insert_chars, "*"))
        self.btn_left.clicked.connect(partial(self.insert_chars, "("))
        self.btn_right.clicked.connect(partial(self.insert_chars,")")) 
        self.btn_eq.clicked.connect(self.calc)
        self.btn_ac.clicked.connect(self.ac) 
        self.btn_del.clicked.connect(self.del_calc)

    def setBasic(self):
        self.MainWindow.setWindowTitle("Basic calculator")
        self.MainWindow.setMinimumSize(QSize(290, 450))
        self.MainWindow.setMaximumSize(QSize(290, 450))
        self.MainWindow.resize(290, 450)
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
        if char in ["+", "-", "*", "/"]:
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

    def ac(self):
        self.calc_area.clear()
    
    def del_calc(self):
        if "Error" in self.calc_area.toPlainText():
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
        self.btn_divide.clicked.connect(partial(self.insert_chars, "/"))
        self.btn_plus.clicked.connect(partial(self.insert_chars, "+"))
        self.btn_minus.clicked.connect(partial(self.insert_chars, "-"))
        self.btn_times.clicked.connect(partial(self.insert_chars, "*"))
        self.btn_left.clicked.connect(partial(self.insert_chars, "("))
        self.btn_right.clicked.connect(partial(self.insert_chars,")")) 
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
        

    def setScientific(self):
        self.MainWindow.setMinimumSize(QSize(586, 567))
        self.MainWindow.setMaximumSize(QSize(586, 567))
        self.MainWindow.resize(QSize(586, 567))
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
        if char in ["+", "-", "*", "/"]:
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

class CalcMainWindow(QMainWindow, CalcUI):
    # global ANS, A, B, C, D, E, F, M, X, Y, Z
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QPixmap("logo.png"))
        self.basic_calc = BasicCalcWidget(self)
        self.stacked_widget.addWidget(self.basic_calc)
        self.scientific_calc = ScientificCalcWidget(self)
        self.stacked_widget.addWidget(self.scientific_calc)
        if int(DEFAULT_MODE) == 0:
            self.setBasicMode()
        elif int(DEFAULT_MODE) == 1:
            self.setScientificMode()
        self.menubar.action_basic.triggered.connect(self.setBasicMode)
        self.menubar.action_scientific.triggered.connect(self.setScientificMode)

    def setBasicMode(self):
        self.basic_calc.setBasic()
        self.stacked_widget.setCurrentIndex(0)

    def setScientificMode(self):
        self.scientific_calc.setScientific()
        self.stacked_widget.setCurrentIndex(1)



app = QApplication()
main = CalcMainWindow()
main.show()
sys.exit(app.exec())
