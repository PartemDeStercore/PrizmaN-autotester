from pickle import load
import serial
import serial.tools.list_ports
from time import sleep
def voltage_calibration(comport): #TODO test
    in_volt=int(float(input("Введи текущее напряжение на БП: "))*100)
    l=100
    r=200
    m=(l+r)//2
    while r-l>2:
        comport.write(bytes(f"$99,30,0{m},0*", 'utf-8'))
        #sleep(1)
        ans=comport.readline().decode("utf-8")
        if ans!='A\n':print("Something goes wrong")
        print(f"debug {m}")
        comport.write(b"$20,10,0001,1*")#ПРИНЯТЬ А
        #sleep(1)
        now_volt=int(float(comport.readline().decode("utf-8")[12:-2])*100)
        if in_volt<now_volt:r=m
        else:l=m
        m=(r+l)//2
    comport.write(b"$99,20,0001,0*")
def heat_check(comport): #TODO test
    comport.write(b"$20,30,0001,1*")
    body_t=int(comport.readline().decode("utf-9")[9:-1])
    if body_t<20 or body_t>25:
        print(f"На внутреннем термисторе ошибка! Показывает {body_t}")
    comport.write(b"$20,20,0001,1*")
    heat_t=int(comport.readline().decode("utf-9")[9:-1])
    flag=0
    if heat_t<20:
        print(f"На внешнем термисторе ошибка! Показывает {heat_t}")
        flag=int(input("Выполнить принудительно?(0 - нет, 1 - да)"))
    elif flag:
        print("Включил ТЭН, должен закрутиться вентилятор")
        comport.write(b"$10,21,0001,1*")
        ans=comport.readline().decode("utf-8")
        print(f"Ответ: {ans}")
        sleep(3)
        print("Выключаю вентилятор")
        comport.write(b"$10,30,0001,1*")
        ans=comport.readline().decode("utf-8")
        print(f"Ответ: {ans}")
        while heat_t<35:
            sleep(15)
            comport.write(b"$20,20,0001,1*")
            heat_t=int(comport.readline().decode("utf-9")[9:-1])
            print(f"Температура:{heat_t}")
        print("Успех, выключаю ТЭН")
        comport.write(b"$10,20,0001,1*")
        ans=comport.readline().decode("utf-8")
        print(f"Ответ: {ans}")
# def motors_check():
#     
# def ir_check():
#     


ports = list(serial.tools.list_ports.comports())#определение порта
port_name=""
if len(ports)==1:
    port_name=ports[0].device
elif len(ports)==0:
    print("В портах пусто, повторяю попытку")
    while len(ports)==0:
        ports = list(serial.tools.list_ports.comports())
        sleep(3)
else:
    print("Выбери порт")
    for port in ports:
        print(f"Порт: {port.device}")
    foo=int(input())
    port_name=ports[foo].device
print(f"Выбран порт {port_name}")
port=serial.Serial(port_name,19200)

params_file=open("command_codes.bin","rb")
params=load(params_file)
params_file.close()
exit_flag=1
while exit_flag>0:
    print("Что показать?")
    for i in range(len(params)):
        print(f"{i+1}) {params[i][1]}")
    print(f"{len(params)+1}) Калибровка вольтметра")
    variant=int(input())-1
    while variant>=len(params)+1:
        print(f"Вариантов всего {len(params)+1}")
        variant=int(input())-1
    if variant==len(params):
        print("Запускаю калибровку вольтметра")
        voltage_calibration(port)
    if params[variant][-1]<2:
        print(f"Посылаю команду {params[variant][2]}")
        port.write(bytes(params[variant][0], 'utf-8'))
    else:
        print(f"Введите параметр(по умолчанию {params[variant][-1]})")
        par=int(input())
        while par>9999 or par<0:
            print("Инвалид ввод")
            par=int(input())
        code=bytes(params[variant][0][:7]+("0"*(4-len(str(par))))+str(par)+params[variant][0][-3:], 'utf-8')
        print(f"Посылаю команду {params[variant][2]}")
        print(f"debug {code}")
    answer = port.readline().decode('utf-8')
    print(f"Ответ: {answer}")
    sleep(3)
port.close()
