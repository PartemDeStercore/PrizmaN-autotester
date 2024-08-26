import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup
from Main_window_design import Ui_MainWindow
from Settings_design import Ui_MainWindow_Settings


class WorkClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WorkClass, self).__init__()
        self.st = Settings()
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
        self.pushButton_11.clicked.connect(self.any_func)  # ОБОГРЕВ авто
        self.pushButton_5.clicked.connect(self.any_func)  # ВОЛЬТМЕТР авто
        self.pushButton_6.clicked.connect(self.any_func)  # ФОКУС авто
        self.pushButton_10.clicked.connect(self.any_func)  # ТЕМПЕРАТУРА инфа
        self.pushButton_12.clicked.connect(self.any_func)  # НАПРЯЖЕНИЕ инфа
        self.pushButton_7.clicked.connect(self.any_func)  # PPS инфа
        self.pushButton_8.clicked.connect(self.any_func)  # GPS инфа
        self.pushButton_9.clicked.connect(self.any_func)  # ВСЕ ПАРАМЕТРЫ инфа
        self.pushButton_14.clicked.connect(self.any_func)  # OPENCV !!! пиздец
        self.pushButton_13.clicked.connect(self.open_settings)


    def comport(self):
        ports = list(serial.tools.list_ports.comports())
        port_name = ""
        if len(ports) == 1:
            port_name = ports[0].device
        else:
            print("Ошибка! COM-порт недоступен")
        port = serial.Serial(port_name, 19200)
        return port

    def selfreboot(self):  # Перезапуск, плата
        self.port.write(b"$10,10,1000,0*")

    def reboot_gps(self):  # Перезапуск, gps
        self.port.write(b"$10,40,0000,1*")
        self.port.read()

    def reboot_dev1(self):  # Перезапуск, устройство 1
        self.port.write(b"$10,41,0000,1*")

    def reboot_dev2(self):  # Перезапуск, устройство 2
        self.port.write(b"$10,42,0000,1*")
#     def check_heat(self):
#     def check_voltage(self):
#     def check_focus(self):
    def info_heat(self):
        self.port.write(b"$20,30,0001,1*")#Плата
        ans1=self.port.readline().decode("utf-8")
        self.port.write(b"$20,30,0001,1*")#NTC
        ans2=self.port.readline().decode("utf-8")
        print(f"Плата:{ans1} Нагреватель:{ans2}")
    def info_voltage(self):
        self.port.write(b"$20,30,0001,1*")
        ans=self.port.readline().decode("utf-8")
        print(f"Текущее напряжение:{ans}")
    def info_pps(self):
        self.port.write(b"$30,20,0001,1*")
        ans=self.port.readline().decode("utf-8")
        print(f"Ответ GPS:{ans}")
    def info_gps(self):
        self.port.write(b"$30,10,0001,1*")
        ans=self.port.readline().decode("utf-8")
        print(f"Информация с GPS:{ans}")
    def info_all(self):
        self.port.write(b"$20,30,0001,1*")#Плата
        ans1=self.port.readline().decode("utf-8")
        self.port.write(b"$20,30,0001,1*")#NTC
        ans2=self.port.readline().decode("utf-8")
        self.port.write(b"$20,30,0001,1*")
        ans3=self.port.readline().decode("utf-8")
        print(f"Текущее напряжение:{ans}")
        self.port.write(b"$30,20,0001,1*")
        ans4=self.port.readline().decode("utf-8")
        print(f"Температура платы:{ans1}, температура нагревателя:{ans2},напряжение: {ans3},ответ GPS: {ans4}")
    def any_func(self):
        pass  # Жека, это функция по приколу, везде где комменты ее нужно поменять на рабочую, объявляешь в классе
        # как def func(self, args...)
        # OpenCV подумаем и меню настроек сделаем позже

    def open_settings(self):
        self.st.show()


class Settings(QMainWindow, Ui_MainWindow_Settings):
    def __init__(self):
        super(Settings, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = WorkClass()
    wnd.show()
    sys.exit(app.exec())
