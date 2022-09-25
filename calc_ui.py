"""
The official source code for the ui part, a replacement for the file
compiled with pyuic
"""

from ast import Num
import json
from turtle import title

from PySide6.QtWidgets import QFrame, QGridLayout, QPushButton, QSizePolicy, \
QVBoxLayout, QWidget, QMainWindow, QMenu, QMenuBar, QPlainTextEdit, QGraphicsDropShadowEffect, QMessageBox, QStackedWidget, QGroupBox, QHBoxLayout, QRadioButton, QLabel, QSpacerItem
from PySide6.QtGui import QAction, QCursor, QFont, QPixmap
from PySide6.QtCore import QSize, Qt, QRect


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
FUNC_BUTTON_BG_NORMAL = THEME["func-button-bg-normal"]
FUNC_BUTTON_FG_NORMAL = THEME["func-button-fg-normal"]
FUNC_BUTTON_BG_HOVER = THEME["func-button-bg-hover"]
FUNC_BUTTON_FG_HOVER = THEME["func-button-fg-hover"]
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


class CustomPushButton(QPushButton):
    def __init__(self, parent, text=""):
        super().__init__(text, parent)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.setSizePolicy(size_policy)
        font = QFont()
        font.setPointSize(int(GENERAL_FONT_SIZE))
        self.setFont(font)
        shadow = QGraphicsDropShadowEffect(parent, blurRadius=10, xOffset=0, yOffset=0)
        self.setGraphicsEffect(shadow)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def format_style(self):
        pass
        

class NumButton(CustomPushButton):
    def __init__(self, parent, num: str):
        super().__init__(parent)
        self.setText(str(num))
        self.setAutoFillBackground(False)
        self.format_style()
    
    def format_style(self):
        self.setStyleSheet(f"""
            QPushButton {{
                border: 0;
                border-radius: 10px;
                padding: 10px;
                background: {NUM_BUTTON_BG_NORMAL};
                color: {NUM_BUTTON_FG_NORMAL}
            }}

            QPushButton:hover{{
                background: {NUM_BUTTON_BG_HOVER};
                color: {NUM_BUTTON_FG_HOVER}
            }}
        """)

class OperButton(CustomPushButton):
    def __init__(self, parent, oper: str):
        super().__init__(parent)
        self.setText(oper)
        self.format_style()
    
    def format_style(self):
        self.setStyleSheet(f"""
            QPushButton {{
                border: 0;
                border-radius: 10px;
                padding: 10px;
                background: {OP_BUTTON_BG_NORMAL};
                color: {OP_BUTTON_FG_NORMAL}
            }}

            QPushButton:hover{{
                background: {OP_BUTTON_BG_HOVER};
                color: {OP_BUTTON_FG_HOVER}
            }}
        """)


class ProcButton(CustomPushButton):
    def __init__(self, parent, oper: str):
        super().__init__(parent)
        self.setText(oper)
        self.format_style()
    
    def format_style(self):
        self.setStyleSheet(f"""
            QPushButton {{
                border: 0;
                border-radius: 10px;
                padding: 10px;
                background: {PROC_BUTTON_BG_NORMAL};
                color: {PROC_BUTTON_FG_NORMAL}
            }}

            QPushButton:hover{{
                background: {PROC_BUTTON_BG_HOVER};
                color: {PROC_BUTTON_FG_HOVER}
            }}
        """)


class FuncButton(CustomPushButton):
    def __init__(self, parent, func_text):
        super().__init__(parent, func_text)
        self.setText(func_text)
        self.format_style()
    
    def format_style(self):
        self.setStyleSheet(
            f"""
            QPushButton {{
                border: 0;
                border-radius: 10px;
                padding: 10px;
                background: {FUNC_BUTTON_BG_NORMAL};
                color: {FUNC_BUTTON_FG_NORMAL}
            }}

            QPushButton:hover{{
                background: {FUNC_BUTTON_BG_HOVER};
                color: {FUNC_BUTTON_FG_HOVER}
            }}
            """
        )

class MenuBar(QMenuBar):
    def __init__(self, MainWindow: QMainWindow):
        super().__init__(MainWindow)
        font = QFont()
        font.setPointSize(MENU_FONT_SIZE)
        self.setFont(font)
        self.setGeometry(QRect(0, 0, 290, 22))
        self.setCursor(QCursor(Qt.ArrowCursor))

        self.menu_settings = QMenu("Settings", self)
        self.menu_settings.setFont(font)
        self.menu_mode = QMenu("Mode", self.menu_settings)
        self.action_change_theme = QAction("Change theme...", MainWindow)
        self.action_basic = QAction("Basic mode", MainWindow)
        self.action_scientific = QAction("Scientific mode (UI test)", MainWindow)
        self.action_conversion = QAction("Unit converter mode (Coming soon)")
        self.action_currency = QAction("Currency converter mode (Coming soon)")
        self.action_other_settings = QAction("Other settings", MainWindow)
        self.addAction(self.menu_settings.menuAction())
        self.menu_settings.addAction(self.menu_mode.menuAction())
        self.menu_settings.addAction(self.action_change_theme)
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.action_other_settings)
        self.menu_mode.addAction(self.action_basic)
        self.menu_mode.addAction(self.action_scientific)
        self.menu_mode.setFont(font)

        self.menu_variables = QMenu("Variables", self)
        self.menu_variables.setFont(font)
        self.menu_save_to = QMenu("Save to", self.menu_variables)
        self.menu_save_to.setFont(font)
        self.menu_use = QMenu("Use", self.menu_variables)
        self.menu_use.setFont(font)
        self.action_ANS = QAction("ANS", MainWindow)
        self.action_sto_A = QAction("A", MainWindow)
        self.action_sto_B = QAction("B", MainWindow)
        self.action_sto_C = QAction("C", MainWindow)
        self.action_sto_D = QAction("D", MainWindow)
        self.action_sto_E = QAction("E", MainWindow)
        self.action_sto_F = QAction("F", MainWindow)
        self.action_sto_M = QAction("M", MainWindow)
        self.action_sto_X = QAction("X", MainWindow)
        self.action_sto_Y = QAction("Y", MainWindow)
        self.action_sto_Z = QAction("Z", MainWindow)
        self.action_rcl_A = QAction("A", MainWindow)
        self.action_rcl_B = QAction("B", MainWindow)
        self.action_rcl_C = QAction("C", MainWindow)
        self.action_rcl_D = QAction("D", MainWindow)
        self.action_rcl_E = QAction("E", MainWindow)
        self.action_rcl_F = QAction("F", MainWindow)
        self.action_rcl_M = QAction("M", MainWindow)
        self.action_rcl_X = QAction("X", MainWindow)
        self.action_rcl_Y = QAction("Y", MainWindow)
        self.action_rcl_Z = QAction("Z", MainWindow)
        self.action_reset = QAction("Reset all...", MainWindow)
        self.menu_variables.addAction(self.action_ANS)
        self.menu_variables.addAction(self.menu_save_to.menuAction())
        self.menu_variables.addAction(self.menu_use.menuAction())
        self.menu_variables.addAction(self.action_reset)
        self.menu_save_to.addAction(self.action_sto_A)
        self.menu_save_to.addAction(self.action_sto_B)
        self.menu_save_to.addAction(self.action_sto_C)
        self.menu_save_to.addAction(self.action_sto_D)
        self.menu_save_to.addAction(self.action_sto_E)
        self.menu_save_to.addAction(self.action_sto_F)
        self.menu_save_to.addAction(self.action_sto_M)
        self.menu_save_to.addAction(self.action_sto_X)
        self.menu_save_to.addAction(self.action_sto_Y)
        self.menu_save_to.addAction(self.action_sto_Z)
        self.menu_use.addAction(self.action_rcl_A)
        self.menu_use.addAction(self.action_rcl_B)
        self.menu_use.addAction(self.action_rcl_C)
        self.menu_use.addAction(self.action_rcl_D)
        self.menu_use.addAction(self.action_rcl_E)
        self.menu_use.addAction(self.action_rcl_F)
        self.menu_use.addAction(self.action_rcl_M)
        self.menu_use.addAction(self.action_rcl_X)
        self.menu_use.addAction(self.action_rcl_Y)
        self.menu_use.addAction(self.action_rcl_Z)
        self.addAction(self.menu_variables.menuAction())

        self.menu_about = QMenu("About", self)
        self.action_about = QAction("About this software...", MainWindow)
        self.menu_about.addAction(self.action_about)
        self.addMenu(self.menu_about)
        self.format_style()
    
    def format_style(self):
        self.setStyleSheet(f"""
        QMenu{{
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
            background: {MENU_BG_NORMAL};
            color: {MENU_FG_NORMAL};
        }}

        QMenu::item:selected{{
            background: {MENU_BG_HOVER};
            color: {MENU_FG_HOVER};
        }}
        """)


class CustomMessageBox(QMessageBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.format_message()
        self._message_text = ""
        self._message_informative_text = ""
        font = QFont()
        font.setPointSize(int(GENERAL_FONT_SIZE))
        self.setFont(font)

    @property
    def message_text(self):
        return self._message_text
    
    @message_text.setter
    def message_text(self, text):
        self._message_text = text
        self.setText(self._message_text)
    
    @property
    def message_informative_text(self):
        return self._message_informative_text
    
    @message_informative_text.setter
    def message_informative_text(self, informative_text: str):
        self._message_informative_text = informative_text
        self.setInformativeText(informative_text)

    def format_message(self):
        self.setStyleSheet(
            f"""
            QMessageBox{{
                background-color: {WINDOW_BG};
            }}
            QMessageBox QPushButton{{
                background-color: {MESSAGE_OTHER_BUTTONS_BG_NORMAL};
                color: {MESSAGE_OTHER_BUTTONS_FG_NORMAL};
                padding: 10px;
                border-radius: 10px;
                font-size: {GENERAL_FONT_SIZE};
            }}
            QMessageBox QPushButton:hover{{
                background-color: {MESSAGE_OTHER_BUTTONS_BG_HOVER};
                color: {MESSAGE_OTHER_BUTTONS_FG_HOVER};
            }}
            """
        )           


class ResetPopup(CustomMessageBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.message_text = "You are going to reset the values from all variables. \n Continue?"
        self.informative_text = "Continue?"
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.Yes)
        self.button(QMessageBox.Yes).setStyleSheet(
            f"""
            QPushButton{{
                background-color: {MESSAGE_DEFAULT_BUTTON_BG_NORMAL};
                color: {MESSAGE_DEFAULT_BUTTON_FG_NORMAL};
            }}
            QPushButton:hover{{
                background-color: {MESSAGE_DEFAULT_BUTTON_BG_HOVER};
                color: {MESSAGE_DEFAULT_BUTTON_FG_HOVER};
            }}
            """
        )



class CustomCalcArea(QPlainTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(
            int(GENERAL_FONT_SIZE)
        )
        self.setFont(font)
        self.setPlaceholderText("Click the buttons to use your calculator")
        self.setReadOnly(True)
        self.setStyleSheet(f"""
            border-radius: 10px;
            background-color: {CALC_AREA_BG};
            font-size: {GENERAL_FONT_SIZE};
        """)
        shadow = QGraphicsDropShadowEffect(parent, blurRadius=10, xOffset=0, yOffset=0)
        self.setGraphicsEffect(shadow)


class BasicCalcUI(object):
    def setupUi(self, parent: QWidget):
        self.verticalLayout = QVBoxLayout(parent)

        self.calc_area = CustomCalcArea(parent)
        self.calc_area.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout.addWidget(self.calc_area)
        
        font = QFont()
        font.size = 16
        self.frame = QFrame(parent)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.num_0 = NumButton(self.frame, "0")
        self.gridLayout.addWidget(self.num_0, 4, 0, 1, 1)
        self.num_1 = NumButton(self.frame, "1")
        self.gridLayout.addWidget(self.num_1, 3, 0, 1, 1)
        self.num_2 = NumButton(self.frame, "2")
        self.gridLayout.addWidget(self.num_2, 3, 1, 1, 1)
        self.num_3 = NumButton(self.frame, "3")
        self.gridLayout.addWidget(self.num_3, 3, 2, 1, 1)
        self.num_4 = NumButton(self.frame, "4")
        self.gridLayout.addWidget(self.num_4, 2, 0, 1, 1)
        self.num_5 = NumButton(self.frame, "5")
        self.gridLayout.addWidget(self.num_5, 2, 1, 1, 1)
        self.num_6 = NumButton(self.frame, "6")
        self.gridLayout.addWidget(self.num_6, 2, 2, 1, 1)
        self.num_7 = NumButton(self.frame, "7")
        self.gridLayout.addWidget(self.num_7, 1, 0, 1, 1)
        self.num_8 = NumButton(self.frame, "8")
        self.gridLayout.addWidget(self.num_8, 1, 1, 1, 1)
        self.num_9 = NumButton(self.frame, "9")
        self.gridLayout.addWidget(self.num_9, 1, 2, 1, 1)
        self.num_dot = NumButton(self.frame, ".")
        self.gridLayout.addWidget(self.num_dot, 4, 1, 1, 1)

        self.btn_left = OperButton(self.frame, "(")
        self.gridLayout.addWidget(self.btn_left, 4, 2, 1, 1)
        self.btn_right = OperButton(self.frame, ")")
        self.gridLayout.addWidget(self.btn_right, 4, 3, 1, 1)
        self.btn_plus = OperButton(self.frame, "+")
        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)
        self.btn_minus = OperButton(self.frame, "-")
        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_times = OperButton(self.frame, "*")
        self.gridLayout.addWidget(self.btn_times, 2, 3, 1, 1)
        self.btn_divide = OperButton(self.frame, "/")
        self.gridLayout.addWidget(self.btn_divide, 3, 3, 1, 1)

        self.btn_eq = ProcButton(self.frame, "=")
        self.gridLayout.addWidget(self.btn_eq, 0, 2, 1, 1)
        self.btn_ac = ProcButton(self.frame, "AC")
        self.gridLayout.addWidget(self.btn_ac, 0, 1, 1, 1)
        self.btn_del = ProcButton(self.frame, "DEL")
        self.gridLayout.addWidget(self.btn_del, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.frame)



class ScientificCalcUI(object):
    def setupUi(self, parent: QWidget, MainWindow: QMainWindow):
        # super().setupUi(parent, MainWindow)

        self.verticalLayout = QVBoxLayout(parent)

        self.angle_unit = QGroupBox(parent)
        self.angle_unit.setTitle("Angle unit:")
        gr_box_horizontal = QHBoxLayout(self.angle_unit)
        self.degree_radio = QRadioButton("degree (°)", self.angle_unit)
        self.radian_radio = QRadioButton("radian (rad)", self.angle_unit)
        gr_box_horizontal.addWidget(self.degree_radio)
        gr_box_horizontal.addWidget(self.radian_radio)
        self.verticalLayout.addWidget(self.angle_unit)

        self.calc_area = CustomCalcArea(parent)
        self.calc_area.setMaximumSize(QSize(16777215, 100))
        self.calc_area.setMinimumHeight(100)
        self.verticalLayout.addWidget(self.calc_area)
        
        font = QFont()
        font.size = 16
        self.frame = QFrame(parent)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.num_0 = NumButton(self.frame, "0")
        self.gridLayout.addWidget(self.num_0, 4, 0, 1, 1)
        self.num_1 = NumButton(self.frame, "1")
        self.gridLayout.addWidget(self.num_1, 3, 0, 1, 1)
        self.num_2 = NumButton(self.frame, "2")
        self.gridLayout.addWidget(self.num_2, 3, 1, 1, 1)
        self.num_3 = NumButton(self.frame, "3")
        self.gridLayout.addWidget(self.num_3, 3, 2, 1, 1)
        self.num_4 = NumButton(self.frame, "4")
        self.gridLayout.addWidget(self.num_4, 2, 0, 1, 1)
        self.num_5 = NumButton(self.frame, "5")
        self.gridLayout.addWidget(self.num_5, 2, 1, 1, 1)
        self.num_6 = NumButton(self.frame, "6")
        self.gridLayout.addWidget(self.num_6, 2, 2, 1, 1)
        self.num_7 = NumButton(self.frame, "7")
        self.gridLayout.addWidget(self.num_7, 1, 0, 1, 1)
        self.num_8 = NumButton(self.frame, "8")
        self.gridLayout.addWidget(self.num_8, 1, 1, 1, 1)
        self.num_9 = NumButton(self.frame, "9")
        self.gridLayout.addWidget(self.num_9, 1, 2, 1, 1)
        self.num_dot = NumButton(self.frame, ".")
        self.gridLayout.addWidget(self.num_dot, 4, 1, 1, 1)

        self.btn_left = OperButton(self.frame, "(")
        self.btn_right = OperButton(self.frame, ")")
        self.btn_plus = OperButton(self.frame, "+")
        self.btn_minus = OperButton(self.frame, "-")
        self.btn_times = OperButton(self.frame, "*")
        self.btn_divide = OperButton(self.frame, "/")

        self.btn_eq = ProcButton(self.frame, "=")
        self.gridLayout.addWidget(self.btn_eq, 0, 2, 1, 1)
        self.btn_ac = ProcButton(self.frame, "AC")
        self.gridLayout.addWidget(self.btn_ac, 0, 1, 1, 1)
        self.btn_del = ProcButton(self.frame, "DEL")
        self.gridLayout.addWidget(self.btn_del, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_minus, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.btn_times, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_divide, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.btn_left, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_right, 2, 4, 1, 1)

        self.btn_ans = NumButton(self.frame, "ANS")
        self.gridLayout.addWidget(self.btn_ans, 4, 2, 1, 1)
        self.btn_pi = NumButton(self.frame, u"π")
        self.gridLayout.addWidget(self.btn_pi, 5, 0, 1, 1)      
        self.btn_comma = NumButton(self.frame, ",")
        self.gridLayout.addWidget(self.btn_comma, 5, 1, 1, 1)
        self.btn_e = NumButton(self.frame, u"\u212f")
        self.gridLayout.addWidget(self.btn_e, 5, 2, 1, 1)

        self.btn_sqrt = OperButton(self.frame, u"√")
        self.gridLayout.addWidget(self.btn_sqrt, 3, 3, 1, 1)
        self.btn_nroot = OperButton(self.frame, "nroot")
        self.gridLayout.addWidget(self.btn_nroot, 3, 4, 1, 1)
        self.btn_factorial = OperButton(self.frame, "!")
        self.gridLayout.addWidget(self.btn_factorial, 4, 3, 1, 1)
        self.btn_percent = OperButton(self.frame, "%")
        self.gridLayout.addWidget(self.btn_percent, 4, 4, 1, 1)

        self.btn_sin = FuncButton(self.frame, "sin")
        self.btn_cos = FuncButton(self.frame, "cos")
        self.btn_tan = FuncButton(self.frame, "tan")
        self.btn_sinh = FuncButton(self.frame, "sinh")
        self.btn_cosh = FuncButton(self.frame, "cosh")
        self.btn_tanh = FuncButton(self.frame, "tanh")
        self.btn_asin = FuncButton(self.frame, "arcsin")
        self.btn_acos = FuncButton(self.frame, "arccos")
        self.btn_atan = FuncButton(self.frame, "arctan")
        self.btn_asinh = FuncButton(self.frame, "arcsinh")
        self.btn_acosh = FuncButton(self.frame, "arccosh")
        self.btn_atanh = FuncButton(self.frame, "arctanh")
        self.gridLayout.addWidget(self.btn_sin, 0, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_cos, 1, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_tan, 2, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_sinh, 3, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_cosh, 4, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_tanh, 5, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_asin, 0, 6, 1, 1)
        self.gridLayout.addWidget(self.btn_acos, 1, 6, 1, 1)
        self.gridLayout.addWidget(self.btn_atan, 2, 6, 1, 1)
        self.gridLayout.addWidget(self.btn_asinh, 3, 6, 1, 1)
        self.gridLayout.addWidget(self.btn_acosh, 4, 6, 1, 1)
        self.gridLayout.addWidget(self.btn_atanh, 5, 6, 1, 1)

        self.btn_log = FuncButton(self.frame, "log")
        self.btn_ln = FuncButton(self.frame, "ln")
        self.btn_gcd = FuncButton(self.frame, "GCD")
        self.btn_lcm = FuncButton(self.frame, "LCM")
        self.gridLayout.addWidget(self.btn_log, 5, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_ln, 5, 4, 1, 1)
        self.gridLayout.addWidget(self.btn_gcd, 5, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_lcm, 5, 6, 1, 1)

        self.verticalLayout.addWidget(self.frame)


class CalcUI(object):
    def setupUi(self, MainWindow: QMainWindow):
        self.menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.centralwidget = QWidget(MainWindow)
        vertical = QVBoxLayout(self.centralwidget)

        self.stacked_widget = QStackedWidget(self.centralwidget)
        vertical.addWidget(self.stacked_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStyleSheet(f"background-color: {WINDOW_BG}")
    


# class TestWindow(QMainWindow, BasicCalcUI):
#     def __init__(self):
#         super().__init__()
#         self.centralwidget = QWidget(self)
#         self.setupUi(self.centralwidget)
#         self.setCentralWidget(self.centralwidget)


# import sys
# from PySide6.QtWidgets import QApplication
# app = QApplication()
# main = TestWindow()
# main.show()
# sys.exit(app.exec())