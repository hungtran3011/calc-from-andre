import sys
from functools import partial
import json

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QColor
# from calc import Ui_MainWindow
from calc_ui import CalcUI, ResetPopup
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


class CalcMainWindow(QMainWindow, CalcUI):
    # global ANS, A, B, C, D, E, F, M, X, Y, Z
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

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
        self.menubar.action_ANS.triggered.connect(partial(self.insert_chars, "ANS"))
        self.menubar.action_rcl_A.triggered.connect(partial(self.insert_chars, "A"))
        self.menubar.action_rcl_B.triggered.connect(partial(self.insert_chars, "B"))
        self.menubar.action_rcl_C.triggered.connect(partial(self.insert_chars, "C"))
        self.menubar.action_rcl_D.triggered.connect(partial(self.insert_chars, "D"))
        self.menubar.action_rcl_E.triggered.connect(partial(self.insert_chars, "E"))
        self.menubar.action_rcl_F.triggered.connect(partial(self.insert_chars, "F"))
        self.menubar.action_rcl_M.triggered.connect(partial(self.insert_chars, "M"))
        self.menubar.action_rcl_X.triggered.connect(partial(self.insert_chars, "X"))
        self.menubar.action_rcl_Y.triggered.connect(partial(self.insert_chars, "Y"))
        self.menubar.action_rcl_Z.triggered.connect(partial(self.insert_chars, "Z"))
        self.menubar.action_sto_A.triggered.connect(partial(self.sto_var, "A"))
        self.menubar.action_sto_B.triggered.connect(partial(self.sto_var, "B"))
        self.menubar.action_sto_C.triggered.connect(partial(self.sto_var, "C"))
        self.menubar.action_sto_D.triggered.connect(partial(self.sto_var, "D"))
        self.menubar.action_sto_E.triggered.connect(partial(self.sto_var, "E"))
        self.menubar.action_sto_F.triggered.connect(partial(self.sto_var, "F"))
        self.menubar.action_sto_M.triggered.connect(partial(self.sto_var, "M"))
        self.menubar.action_sto_X.triggered.connect(partial(self.sto_var, "X"))
        self.menubar.action_sto_Y.triggered.connect(partial(self.sto_var, "Y"))
        self.menubar.action_sto_Z.triggered.connect(partial(self.sto_var, "Z"))
        self.menubar.action_reset.triggered.connect(self.reset_vars)

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
        except SyntaxError:
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




app = QApplication()
main = CalcMainWindow()
main.show()
sys.exit(app.exec())
