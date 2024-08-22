from pickle import load
import serial
import serial.tools.list_ports
from time import sleep


# Саня, дарова
# Все printы должны быть в большом окошке которое stdout если не указано иное
# Все inputы входят из маленького окошка stdin
def comport():  # Функция выполняется самой первой в программе, возвращает значение port которое используется во всех остальных функциях
    ports = list(serial.tools.list_ports.comports())
    port_name = ""
    if len(ports) == 1:
        port_name = ports[0].device  # В этом варианте в списке должен быть сразу выбран вариант
    elif len(ports) == 0:
        print("В портах пусто, повторяю попытку")
        while len(ports) == 0:
            ports = list(serial.tools.list_ports.comports())
            sleep(3)
    else:
        # В этом варианте список должен быть с пустым выбором изначально
        print("Выбери порт")  # Заменить на выпадающий список
        for port in ports:
            print(f"{port.device}")  # Непосредственно список
        foo = int(input())
        port_name = ports[foo].device
    port = serial.Serial(port_name, 19200)
    return port


def fan_control(port):  # Ручной режим, чекбокс вентилятора
    port.write(b"$10,31,0001,1*")  # если значение изменилось на галочку
    port.write(b"$10,30,0001,1*")  # если значение изменилось на пустоту


def heat_control(port):  # Ручной режим, чекбокс обогрева
    fan_control(
        port)  # Если значение изменилось на галочку то въебать галочку и на вентилятор(отправлять значение не нужно)
    port.write(b"$10,21,0001,1*")  # если значение изменилось на галочку
    port.write(b"$10,20,0001,1*")  # если значение изменилось на пустоту


def iris_control(port):  # Моторы, диафрагма
    while (cond != 0):  # я предположу что есть переменная cond которая принимает значение 0 в 0, -1 в - и 1 в +
        if (cond == 1):
            port.write(b"$50,10,0100,0*")
        if (cond == -1):
            port.write(b"$50,20,0100,0*")
        sleep(3);


def focus_control(port):  # Моторы, фокус
    while (cond != 0):  # аналогично ирису
        if (cond == 1):
            port.write(b"$60,10,3000,0*")
        if (cond == -1):
            port.write(b"$60,20,3000,0*")
        sleep(3);


def zoom_control(port):  # Моторы, приближение
    while (cond != 0):  # аналогично ирису
        if (cond == 1):
            port.write(b"$70,10,3000,0*")
        if (cond == -1):
            port.write(b"$70,20,3000,0*")
        sleep(3);


def ir_control(port):  # Подсветка, IR
    port.write(b"$91,40,0001,1*")  # если значение изменилось на галочку
    port.write(b"$91,30,0001,1*")  # если значение изменилось на пустоту


def xn_control(port):  # Подсветка, XN
    port.write(b"$91,74,0001,1*")  # если значение изменилось на галочку
    port.write(b"$91,75,0001,1*")  # если значение изменилось на пустоту


def selfreboot():  # Перезапуск, плата
    port.write(b"$10,10,1000,0*")


def reboot_gps():  # Перезапуск, gps
    port.write(b"$10,40,0000,1*")


def selfreboot():  # Перезапуск, устройство 1
    port.write(b"$10,41,0000,1*")


def selfreboot():  # Перезапуск, устройство 2
    port.write(b"$10,42,0000,1*")
