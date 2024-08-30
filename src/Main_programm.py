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

        self.push_buttons()

    def check_boxes(self):
        self.checkBox_2.stateChanged.connect(self.any_func)  # ОБОГРЕВ
        self.checkBox.stateChanged.connect(self.any_func)  # ВЕНТИЛЯТОР
        self.checkBox_3.stateChanged.connect(self.any_func)  # IR
        self.checkBox_4.stateChanged.connect(self.any_func)  # Xn

    def push_buttons(self):
        self.pushButton.clicked.connect(self.selfreboot)
        self.pushButton_2.clicked.connect(self.reboot_gps)
        self.pushButton_3.clicked.connect(self.reboot_dev1)
        self.pushButton_4.clicked.connect(self.reboot_dev2)
        self.pushButton_5.clicked.connect(self.any_func)  # ОБОГРЕВ авто
        self.pushButton_6.clicked.connect(self.any_func)  # ВОЛЬТМЕТР авто
        self.pushButton_11.clicked.connect(self.any_func)  # ФОКУС авто
        self.pushButton_7.clicked.connect(self.info_heat)  # ТЕМПЕРАТУРА инфа
        self.pushButton_8.clicked.connect(self.info_voltage)  # НАПРЯЖЕНИЕ инфа
        self.pushButton_9.clicked.connect(self.info_pps)  # PPS инфа
        self.pushButton_10.clicked.connect(self.info_gps)  # GPS инфа
        self.pushButton_12.clicked.connect(self.info_all)  # ВСЕ ПАРАМЕТРЫ инфа
        self.pushButton_14.clicked.connect(self.any_func)  # OPENCV !!! пиздец
        self.pushButton_13.clicked.connect(self.open_settings)
        self.pushButton_15.clicked.connect(self.any_func)  # Диафрагма -
        self.pushButton_16.clicked.connect(self.any_func)  # Диафрагма +
        self.pushButton_17.clicked.connect(self.any_func)  # Фокус -
        self.pushButton_19.clicked.connect(self.any_func)  # Фокус +
        self.pushButton_18.clicked.connect(self.any_func)  # Приближение -
        self.pushButton_20.clicked.connect(self.any_func)  # Приближение +

    def comport(self):
        ports = list(serial.tools.list_ports.comports())
        port_name = ""
        if len(ports) == 1:
            port_name = ports[0].device
        else:
            self.textBrowser_16.append("<span>Ошибка! COM-порт недоступен</span>")
            # print("Ошибка! COM-порт недоступен")
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
        self.port.write(b"$20,30,0001,1*")  # Плата
        ans1 = self.port.readline().decode("utf-8")
        self.port.write(b"$20,30,0001,1*")  # NTC
        ans2 = self.port.readline().decode("utf-8")
        self.textBrowser_16.append(f"<span>Плата:{ans1} Нагреватель:{ans2}</span>")
        # print(f"Плата:{ans1} Нагреватель:{ans2}")

    def info_voltage(self):
        self.port.write(b"$20,30,0001,1*")
        ans = self.port.readline().decode("utf-8")
        self.textBrowser_16.append(f"<span>Текущее напряжение:{ans}</span>")
        # print(f"Текущее напряжение:{ans}")

    def info_pps(self):
        self.port.write(b"$30,20,0001,1*")
        ans = self.port.readline().decode("utf-8")
        self.textBrowser_16.append(f"<span>Ответ GPS:{ans}</span>")
        # print(f"Ответ GPS:{ans}")

    def info_gps(self):
        self.port.write(b"$30,10,0001,1*")
        ans = self.port.readline().decode("utf-8")
        self.textBrowser_16.append(f"<span>Информация с GPS:{ans}</span>")
        # print(f"Информация с GPS:{ans}")

    def info_all(self):
        self.port.write(b"$20,30,0001,1*")  # Плата
        ans1 = self.port.readline().decode("utf-8")
        self.port.write(b"$20,30,0001,1*")  # NTC
        ans2 = self.port.readline().decode("utf-8")
        self.port.write(b"$20,30,0001,1*")
        ans3 = self.port.readline().decode("utf-8")
        self.port.write(b"$30,20,0001,1*")
        ans4 = self.port.readline().decode("utf-8")
        self.textBrowser_16.append(f"<span>Температура платы:{ans1}, температура нагревателя:{ans2},напряжение: {ans3},ответ GPS: {ans4}</span>")
        # print(f"Температура платы:{ans1}, температура нагревателя:{ans2},напряжение: {ans3},ответ GPS: {ans4}")

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
