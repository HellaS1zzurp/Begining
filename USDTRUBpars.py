import urllib.request
import datetime
import time as ti

def calc():
    while True:
        try:
            z = input(str('Нужен калькулятор?\n'))
            if z == 'да':
                i = float(input('Сколько у тебя баксов?\n'))
                p = float(y[22:-1])
                d = i * p
                print(f'{i} * {p} = ', float('{:.4f}'.format(d)))
                continue
                    
        except BaseException as r:
            print('Ошибочное значение!Разделение идёт точкой "."!\n')
            
        finally:
            p = input('Хотите завершить?\n')
            if p == 'нет':
                calc()
            else:
                print('Пока!')
                ti.sleep(3)
                exit() 

path = 'https://api.binance.com/api/v3/ticker/price?symbol=USDTRUB'
time = datetime.datetime.now()

try:
    with urllib.request.urlopen(path) as r:
        print(f'Текущий курс USDTRUB на {time.strftime("%d-%m-%Y %H:%M")}: \n')
        x = r.read().decode('utf-8')
        y = str(x).replace('"', '')
        print(y, '\n')
        
finally:
    calc()
        
    
 
