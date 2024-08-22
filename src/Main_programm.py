import sys
from pickle import load
import serial
import serial.tools.list_ports
from time import sleep
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from Main_window_design import Ui_MainWindow


class Work_class(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Work_class, self).__init__()
        self.setupUi(self)
        self.port = []
        self.ports = []
        self.port = self.comport()
        self.comboBox.addItems(self.ports)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.selfreboot())
        self.pushButton_2.clicked.connect(self.selfreboot())
        self.pushButton_3.clicked.connect(self.selfreboot())
        self.pushButton_4.clicked.connect(self.selfreboot())


    def comport(self):  # Функция выполняется самой первой в программе, возвращает значение port которое используется во всех остальных функциях
        self.ports = list(serial.tools.list_ports.comports())
        port_name = ""
        if len(self.ports) == 1:
            port_name = self.ports[0].device  # В этом варианте в списке должен быть сразу выбран вариант
        elif len(self.ports) == 0:
            print("В портах пусто, повторяю попытку")
            while len(self.ports) == 0:
                self.ports = list(serial.tools.list_ports.comports())
                sleep(3)
        else:
            # В этом варианте список должен быть с пустым выбором изначально
            print("Выбери порт")  # Заменить на выпадающий список
            for port in self.ports:
                print(f"{port.device}")  # Непосредственно список
            foo = int(input())
            port_name = self.ports[foo].device
        port = serial.Serial(port_name, 19200)
        return port

    def selfreboot(self):  # Перезапуск, плата
        self.port.write(b"$10,10,1000,0*")

    def reboot_gps(self):  # Перезапуск, gps
        self.port.write(b"$10,40,0000,1*")

    def selfreboot(self):  # Перезапуск, устройство 1
        self.port.write(b"$10,41,0000,1*")

    def selfreboot(self):  # Перезапуск, устройство 2
        self.port.write(b"$10,42,0000,1*")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Work_class()
    wnd.show()
    sys.exit(app.exec())
