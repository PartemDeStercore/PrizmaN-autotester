import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup
from Main_window_design import Ui_MainWindow


class WorkClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WorkClass, self).__init__()
        self.setupUi(self)
        self.port = []
        self.ports = []
        self.port = self.comport()
        self.setupUi(self)

        self.button_group_diaphragm = QButtonGroup()
        self.button_group_focus = QButtonGroup()
        self.button_group_approximation = QButtonGroup()
        self.radio_buttons()
        self.button_group_diaphragm.buttonClicked.connect(self.radio_button_clicked_diaphragm)
        self.button_group_focus.buttonClicked.connect(self.radio_button_clicked_focus)
        self.button_group_approximation.buttonClicked.connect(self.radio_button_clicked_approximation)

        self.push_buttons()

    def check_boxes(self):
        self.checkBox_2.stateChanged.connect(self.any_func)  # ОБОГРЕВ
        self.checkBox.stateChanged.connect(self.any_func)  # ВЕНТИЛЯТОР
        self.checkBox_3.stateChanged.connect(self.any_func)  # IR
        self.checkBox_4.stateChanged.connect(self.any_func)  # Xn

    def radio_button_clicked_diaphragm(self, button):
        if button == self.radioButton_22:
            pass  # Функция 0
        elif button == self.radioButton_23:
            pass  # Функция -
        elif button == self.radioButton_24:
            pass  # Функция +

    def radio_button_clicked_focus(self, button):
        if button == self.radioButton:
            pass  # Функция 0
        elif button == self.radioButton_2:
            pass  # Функция -
        elif button == self.radioButton_3:
            pass  # Функция +

    def radio_button_clicked_approximation(self, button):
        if button == self.radioButton_19:
            pass  # Функция 0
        elif button == self.radioButton_20:
            pass  # Функция -
        elif button == self.radioButton_21:
            pass  # Функция +

    def radio_buttons(self):
        self.button_group_diaphragm.addButton(self.radioButton_22)
        self.button_group_diaphragm.addButton(self.radioButton_23)
        self.button_group_diaphragm.addButton(self.radioButton_24)

        self.button_group_focus.addButton(self.radioButton)
        self.button_group_focus.addButton(self.radioButton_2)
        self.button_group_focus.addButton(self.radioButton_3)

        self.button_group_approximation.addButton(self.radioButton_19)
        self.button_group_approximation.addButton(self.radioButton_20)
        self.button_group_approximation.addButton(self.radioButton_21)

    def push_buttons(self):
        self.pushButton.clicked.connect(self.selfreboot)
        self.pushButton_2.clicked.connect(self.reboot_gps)
        self.pushButton_3.clicked.connect(self.reboot_dev1)
        self.pushButton_4.clicked.connect(self.reboot_dev2)
        self.pushButton_11.clicked.connect(self.any_func)  # ОБОГРЕВ
        self.pushButton_5.clicked.connect(self.any_func)  # ВОЛЬТМЕТР
        self.pushButton_6.clicked.connect(self.any_func)  # ФОКУС
        self.pushButton_10.clicked.connect(self.any_func)  # ТЕМПЕРАТУРА
        self.pushButton_12.clicked.connect(self.any_func)  # НАПРЯЖЕНИЕ
        self.pushButton_7.clicked.connect(self.any_func)  # PPS
        self.pushButton_8.clicked.connect(self.any_func)  # GPS
        self.pushButton_9.clicked.connect(self.any_func)  # ВСЕ ПАРАМЕТРЫ
        self.pushButton_14.clicked.connect(self.any_func)  # OPENCV !!!
        self.pushButton_13.clicked.connect(self.any_func)  # МЕНЮ НАСТРОЕК !!!


    def comport(self):
        ports = list(serial.tools.list_ports.comports())
        port_name = ""
        if len(ports) == 1:
            port_name = ports[0].device  # В этом варианте в списке должен быть сразу выбран вариант
        else:
            print("Ошибка! COM-порт недоступен")
        port = serial.Serial(port_name, 19200)
        return port

    def selfreboot(self):  # Перезапуск, плата
        self.port.write(b"$10,10,1000,0*")

    def reboot_gps(self):  # Перезапуск, gps
        self.port.write(b"$10,40,0000,1*")

    def reboot_dev1(self):  # Перезапуск, устройство 1
        self.port.write(b"$10,41,0000,1*")

    def reboot_dev2(self):  # Перезапуск, устройство 2
        self.port.write(b"$10,42,0000,1*")

    def any_func(self):
        pass  # Жека, это функция по приколу, везде где комменты ее нужно поменять на рабочую, объявляешь в классе
        # как def func(self, args...)
        # OpenCV подумаем и меню настроек сделаем позже


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = WorkClass()
    wnd.show()
    sys.exit(app.exec())
