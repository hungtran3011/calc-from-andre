"""
The official source code for the ui part, a replacement for the file
compiled with pyuic

Icons used for the UIs are:

<a href="https://www.flaticon.com/free-icons/calculator" title="calculator icons">Calculator icons created by Pixel perfect - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/lab" title="lab icons">Lab icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/money" title="money icons">Money icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/area" title="area icons">Area icons created by Mayor Icons - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/volume" title="volume icons">Volume icons created by Creaticca Creative Agency - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/weight" title="weight icons">Weight icons created by Good Ware - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/energy" title="energy icons">Energy icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/fever" title="fever icons">Fever icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/car" title="car icons">Car icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/angle" title="angle icons">Angle icons created by Voysla - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/database" title="database icons">Database icons created by Bartama Graphic - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/fiction" title="fiction icons">Fiction icons created by Buandesign - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/graph" title="graph icons">Graph icons created by Retinaicons - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/blood-pressure-gauge" title="blood pressure gauge icons">Blood pressure gauge icons created by PLANBSTUDIO - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/battery-level" title="battery level icons">Battery level icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/clock" title="clock icons">Clock icons created by dmitri13 - Flaticon</a>
"""

import json

from PySide6.QtWidgets import QFrame, QGridLayout, QPushButton, QSizePolicy, \
QVBoxLayout, QWidget, QMainWindow, QMenu, QMenuBar, QPlainTextEdit, QGraphicsDropShadowEffect, QMessageBox, QStackedWidget, QGroupBox,\
QHBoxLayout, QRadioButton, QSpacerItem, QComboBox
from PySide6.QtGui import QAction, QCursor, QFont, QPixmap
from PySide6.QtCore import QSize, Qt, QRect

# from __feature__ import snake_case, true_property

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

if ICONS_COLOR == "white":
    ICONS_PATH = "./icons/white/"
else:
    ICONS_PATH = "./icons/black/"

class CustomPushButton(QPushButton):
    def __init__(self, parent, text=""):
        super().__init__(text, parent)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
    def __init__(self, parent, txt: str):
        super().__init__(parent)
        self.setText(txt)
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
        small_font = QFont()
        small_font.setPointSize(SMALL_FONT_SIZE)
        self.setFont(small_font)
        self.setGeometry(QRect(0, 0, 290, 22))
        self.setCursor(QCursor(Qt.ArrowCursor))

        self.menu_settings = QMenu("Settings", self)
        self.menu_settings.setFont(small_font)
        self.menu_mode = QMenu("Mode", self.menu_settings)
        self.action_change_theme = QAction("Change theme...", MainWindow)
        self.action_basic = QAction("Basic mode", MainWindow)
        self.action_basic.setIcon(QPixmap(f"{ICONS_PATH}/basic.png"))
        self.action_scientific = QAction("Scientific mode (UI test)", MainWindow)
        self.action_scientific.setIcon(QPixmap(f"{ICONS_PATH}/scientific.png"))
        self.action_conversion = QAction("Measurement units converter (testing)")
        self.action_conversion.setIcon(QPixmap(f"{ICONS_PATH}/measurement"))
        self.action_currency = QAction("Currency converter (Coming soon)")
        self.action_currency.setIcon(QPixmap(f"{ICONS_PATH}/currency.png"))
        self.action_other_settings = QAction("Other settings", MainWindow)
        self.addAction(self.menu_settings.menuAction())
        self.menu_settings.addAction(self.menu_mode.menuAction())
        self.menu_settings.addAction(self.action_change_theme)
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.action_other_settings)
        self.menu_mode.addAction(self.action_basic)
        self.menu_mode.addAction(self.action_scientific)
        self.menu_mode.addAction(self.action_conversion)
        self.menu_mode.addAction(self.action_currency)
        self.menu_mode.setFont(small_font)

        self.menu_variables = QMenu("Variables", self)
        self.menu_variables.setFont(small_font)
        self.menu_save_to = QMenu("Save to", self.menu_variables)
        self.menu_save_to.setFont(small_font)
        self.menu_use = QMenu("Use", self.menu_variables)
        self.menu_use.setFont(small_font)
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
        general_font = QFont()
        general_font.setPointSize(int(GENERAL_FONT_SIZE))
        self.setFont(general_font)

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



class CustomTextArea(QPlainTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        general_font = QFont()
        general_font.setPointSize(
            int(GENERAL_FONT_SIZE)
        )
        self.setFont(general_font)
        self.placeholder = ""
        self.setPlaceholderText(self.placeholder)
        self.setReadOnly(True)
        self.setStyleSheet(f"""
            border-radius: 10px;
            background-color: {CALC_AREA_BG};
        """)
        shadow = QGraphicsDropShadowEffect(parent, blurRadius=10, xOffset=0, yOffset=0)
        self.setGraphicsEffect(shadow)
    
    def set_placeholder_txt(self, txt):
        self.placeholder = txt
        self.setPlaceholderText(self.placeholder)


class CustomComboBox(QComboBox):
        def __init__(self, parent: QWidget):
            super().__init__(parent)
            self.setAttribute(Qt.WA_TranslucentBackground, True)
            self.format_box()

        def format_box(self):
            self.setStyleSheet(f"""
                QComboBox {{
                    border-radius: 10px;
                    padding: 3px 3px 3px 3px;
                    background: white;
                }}
                QComboBox::drop-down{{
                	border: 0;
                	border-radius: 10px;
                	background: transparent;
                }}
                QComboBox QAbstractItemView {{
                    background: white;
                	border-radius: 10px;
                    border: 1px solid gray;
                	selection-background-color: lightgray;
                }}

                QScollBar:vertical {{
                    border: 0;
                    width: 6px;
                    border-radius: 2px;
                    background: transparent;
                }}
                QScrollBar::handle:vertical {{
                    border: 0;
                }}
                QScrollBar::add-line:vertical {{
                    height: 0px;
                }}
                QScrollBar::sub-line:vertical {{
                    height: 0px;
                }}
            """)


class BasicCalcUI(object):
    def setupUi(self, parent: QWidget):
        self.verticalLayout = QVBoxLayout(parent)

        self.calc_area = CustomTextArea(parent)
        self.calc_area.set_placeholder_txt("Click the buttons to use your calculator")
        self.calc_area.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout.addWidget(self.calc_area)
        
        general_font = QFont()
        general_font.size = GENERAL_FONT_SIZE
        self.frame = QFrame(parent)
        self.frame.setFont(general_font)
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

        general_font = QFont()
        general_font.size = GENERAL_FONT_SIZE

        self.verticalLayout = QVBoxLayout(parent)

        self.angle_unit = QGroupBox(parent)
        self.angle_unit.setTitle("Angle unit:")
        gr_box_horizontal = QHBoxLayout(self.angle_unit)
        self.degree_radio = QRadioButton("degree (°)", self.angle_unit)
        self.radian_radio = QRadioButton("radian (rad)", self.angle_unit)
        gr_box_horizontal.addWidget(self.degree_radio)
        gr_box_horizontal.addWidget(self.radian_radio)
        self.verticalLayout.addWidget(self.angle_unit)

        self.calc_area = CustomTextArea(parent)
        self.calc_area.set_placeholder_txt("Click the buttons to use your calculator")
        self.calc_area.setMaximumSize(QSize(16777215, 100))
        self.calc_area.setMinimumHeight(100)
        self.verticalLayout.addWidget(self.calc_area)
        
        self.frame = QFrame(parent)
        self.frame.setFont(general_font)
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
        self.btn_pow = OperButton(self.frame, "pow")
        self.gridLayout.addWidget(self.btn_pow, 3, 4, 1, 1)
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


class MeasurementConverterUI(object):
    def setupUi(self, parent: QWidget, MainWindow:QMainWindow):
        
        MainWindow.setStyleSheet(f"background-color: {WINDOW_BG}")

        small_font = QFont()
        small_font.setPointSize(SMALL_FONT_SIZE)

        general_font = QFont()
        general_font.setPointSize(GENERAL_FONT_SIZE)

        btn_size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.widget_layout = QGridLayout(parent)

        self.unit_types_combobox = CustomComboBox(parent)
        self.unit_types_combobox.setPlaceholderText("Choose a type of measurement unit")
        self.unit_types_combobox.setFont(small_font)
        self.widget_layout.addWidget(self.unit_types_combobox, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.widget_layout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.btn_convert = ProcButton(parent, "Convert")
        self.btn_convert.setFont(small_font)
        self.btn_convert.setSizePolicy(btn_size_policy)
        self.btn_convert.setMaximumSize(QSize(16777215, 100))
        self.widget_layout.addWidget(self.btn_convert, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.widget_layout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.first_unit_combobox = CustomComboBox(parent)
        self.first_unit_combobox.setFont(small_font)
        self.first_unit_combobox.setPlaceholderText("Choose a unit of measurement")
        self.widget_layout.addWidget(self.first_unit_combobox, 1, 0, 1, 1)
        self.list_types_of_units()

        self.btn_switch = ProcButton(parent, "⇄")
        self.btn_switch.setFont(small_font)
        self.btn_switch.setSizePolicy(btn_size_policy)
        self.btn_switch.setMaximumSize(QSize(16777215, 100))
        self.widget_layout.addWidget(self.btn_switch, 1, 2, 1, 1)

        self.second_unit_combobox = CustomComboBox(parent)
        self.second_unit_combobox.setFont(small_font)
        self.second_unit_combobox.setPlaceholderText("Choose a unit of measurement")
        self.widget_layout.addWidget(self.second_unit_combobox, 1, 4, 1, 1)

        self.first_unit_box = CustomTextArea(parent)
        box_size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # box_size_policy.setHeightForWidth(self.first_unit_box.sizePolicy().hasHeightForWidth())
        self.first_unit_box.setSizePolicy(box_size_policy)
        self.first_unit_box.setFont(general_font)
        self.first_unit_box.setReadOnly(True)
        self.first_unit_box.set_placeholder_txt("Input the value here...")
        self.widget_layout.addWidget(self.first_unit_box, 2, 0, 1, 1)

        self.second_unit_box = CustomTextArea(parent)
        self.second_unit_box.setSizePolicy(box_size_policy)
        self.second_unit_box.setFont(general_font)
        self.second_unit_box.setReadOnly(True)
        self.second_unit_box.setDisabled(True)
        self.widget_layout.addWidget(self.second_unit_box, 2, 4, 1, 1)

        self.input_frame = QFrame(parent)
        self.input_frame.setObjectName(u"input_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_frame.sizePolicy().hasHeightForWidth())
        self.input_frame.setSizePolicy(sizePolicy)

        self.input_layout = QGridLayout(self.input_frame)

        self.num_7 = NumButton(self.input_frame, "7")
        self.num_7.setFont(general_font)
        self.input_layout.addWidget(self.num_7, 2, 0, 1, 1)

        self.num_8 = NumButton(self.input_frame, "8")
        self.num_8.setFont(general_font)
        self.input_layout.addWidget(self.num_8, 2, 1, 1, 1)

        self.num_9 = NumButton(self.input_frame, "9")
        self.num_9.setFont(general_font)
        self.input_layout.addWidget(self.num_9, 2, 2, 1, 1)
        
        self.num_4 = NumButton(self.input_frame, "4")
        self.num_4.setFont(general_font)
        self.input_layout.addWidget(self.num_4, 3, 0, 1, 1)

        self.num_5 = NumButton(self.input_frame, "5")
        self.num_5.setFont(general_font)
        self.input_layout.addWidget(self.num_5, 3, 1, 1, 1)

        self.num_6 = NumButton(self.input_frame, "6")
        self.num_6.setFont(general_font)
        self.input_layout.addWidget(self.num_6, 3, 2, 1, 1)

        self.num_1 = NumButton(self.input_frame, "1")
        self.num_1.setFont(general_font)
        self.input_layout.addWidget(self.num_1, 4, 0, 1, 1)

        self.num_2 = NumButton(self.input_frame, "2")
        self.num_2.setFont(general_font)
        self.input_layout.addWidget(self.num_2, 4, 1, 1, 1)

        self.num_3 = NumButton(self.input_frame, "3")
        self.num_3.setFont(general_font)
        self.input_layout.addWidget(self.num_3, 4, 2, 1, 1)

        self.num_0 = NumButton(self.input_frame, "0")
        self.num_0.setFont(general_font)
        self.input_layout.addWidget(self.num_0, 5, 0, 1, 2)

        self.num_dot = NumButton(self.input_frame, ".")
        self.num_dot.setFont(general_font)
        self.input_layout.addWidget(self.num_dot, 5, 2, 1, 1)

        self.btn_del = ProcButton(self.input_frame, "DEL")
        ac_del_size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        ac_del_size_policy.setHorizontalStretch(0)
        ac_del_size_policy.setVerticalStretch(0)
        ac_del_size_policy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(ac_del_size_policy)
        self.btn_del.setFont(general_font)
        self.input_layout.addWidget(self.btn_del, 2, 3, 2, 1)

        self.btn_ac = ProcButton(self.input_frame, "AC")
        ac_del_size_policy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(ac_del_size_policy)
        self.btn_ac.setFont(general_font)
        self.input_layout.addWidget(self.btn_ac, 4, 3, 2, 1)

        self.widget_layout.addWidget(self.input_frame, 3, 0, 1, 1)

        self.units_list = {
            "Length": (
                'Centimeters', 
                'Foot/Feet', 
                'Inches', 
                'Kilometers', 
                'Meters ', 
                'Micrometers',
                'Miles', 
                'Milimeters', 
                'Nanometers',
                'Yards'
            ),
            "Weight": (
                "Carats",
                "Grams",
                "Kilograms",
                "Metric tonnes",
                "Ounces",
                "Pounds",
            ),
            "Area": (
                "Acres",
                "Hectares",
                "Square inches",
                "Square feet",
                "Square kilometers",
                "Square meters",
                "Square millimeters",
                "Square miles",
                "Square yards"
            ),
            "Volume": (
                "Cubic inches",
                "Cubic feets",
                "Cubic meters",
                "Cubic yards",
                "Cups (US)",
                "FLuid ounces (US)",
                "Gallons (UK)",
                "Gallons (US)",
                "Liters",
                "Milliliters",
                "Pints (UK)",
                "Pints (US)",
                "Quarts (UK)",
                "Quarts (US)",
                "Teaspoons (UK)",
                "Teaspoons (US)",
                "Tablespoons (UK)",
                "Tablespoons (US)",
            ),
            "Temperature": (
                "Celsius",
                "Fahrenheit",
                "Kelvin",
            ),
            "Energy": (
                "Ampere-hours",
                "British thermal units",
                "Calories",
                "Electron volts",
                "Foot-pounds",
                "Joules",
                "Kilocalories",
                "Kilojoules",
                "Kilowatt-hours",
                "Megawatt-hours",
                "Milliampere-hours",
                "Therms",
                "Watt-hours",
            ),
            "Time": (
                "Days",
                "Hours",
                "Microseconds",
                "Milliseconds",
                "Minutes",
                "Nanoseconds",
                "Seconds",
                "Weeks",
                "Years",
            ),
            "Speed": (
                "Feet per second",
                "Inches per second",
                "Kilometers per hour",
                "Kilometers per second",
                "Knots",
                "Mach",
                "Meters per second",
                "Miles per hour",
                "Miles per second",
                "Speed of light",
                "Speed of sound",
                "Yards per second",
                "Yards per hour",
            ),
            "Pressure": (
                "Atmospheres",
                "Bars",
                "Dynes per square centimeter",
                "Feet of mercury",
                "Feet of water",
                "Inches of mercury",
                "Inches of water",
                "Kilograms per square centimeter",
                "Kilograms per square meter",
                "Kilopascals",
                "Kips per square inch",
                "Megapascals",
                "Millibars",
                "Millimeters of mercury",
                "Millimeters of water",
                "Newtons per square meter",
                "Pascals",
                "Pounds per square foot",
                "Pounds per square inch",
                "Pounds per square inch (absolute)",
                "Pounds per square inch (gauge)",
                "Pounds per square inch (technical)",
                "Pounds per square inch (water)",
                "Torrs",
            ),
            "Data": (
                "Bits",
                "Bytes",
                "Gigabits",
                "Gigabytes",
                "Kilobits",
                "Kilobytes",
                "Megabits",
                "Megabytes",
                "Petabits",
                "Petabytes",
                "Terabits",
                "Terabytes",
            ),
            "Frequency": (
                "Gigahertz",
                "Hertz",
                "Kilohertz",
                "Megahertz",
                "Terahertz",
            ),
            "Force": (
                "Dynes",
                "Kilograms-force",
                "Kips",
                "Kiloponds",
                "Newtons",
                "Pounds-force",
                "Poundals",
                "Tonnes-force",
            ),
            "Power": (
                "Boilers horsepower",
                "Electrical horsepower",
                "Foot-pounds per minute",
                "Foot-pounds per second",
                "Gigawatts",
                "Horsepower (boiler)",
                "Horsepower (electric)",
                "Horsepower (metric)",
                "Horsepower (UK)",
                "Horsepower (water)",
                "Horsepower (US)",
                "Kilowatts",
                "Megawatts",
                "Metric horsepower",
                "Metric tons of TNT",
                "Microwatts",
                "Milliwatts",
                "Nanowatts",
                "Petawatts",
                "Picojoules per second",
                "Terawatts",
                "Watts",
            ),
            "Angle": (
                "Degrees",
                "Gradians",
                "Minutes",
                "Radians",
                "Seconds",
            ),
        }


class CalcUI(object):
    def setupUi(self, MainWindow: QMainWindow):
        self.menubar = MenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setWindowIcon(QPixmap("icons/logo.png"))
        self.centralwidget = QWidget(MainWindow)
        vertical = QVBoxLayout(self.centralwidget)

        self.stacked_widget = QStackedWidget(self.centralwidget)
        vertical.addWidget(self.stacked_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStyleSheet(f"background-color: {WINDOW_BG}")
    