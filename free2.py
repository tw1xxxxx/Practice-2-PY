import math
ZNarray, CHarray, znak = [], [], ''
print('\n\nВас приветствует умный калькулятор П50-8-22\nПосмотри что я умею:\n  Сложение  (+)\n  Вычетание  (-)\n  Умножение (*)\n  Деление (/)\n  Возведение в степень (**)\n  Корень (sqrt)\n  Синус (sin)\n  Косинус (cos)\n  Тангенс (tg)\n  Факториал (!)')
try:
    while znak != 'res': 
        a = int(input('\n Введите число '))
        CHarray.append(a)
        znak = str(input('Укажите знак либо "res" '))
        ZNarray.append (znak) if znak in ['+', '-', '/', '*', '**', 'sqrt', 'sin','cos','tg', '!', 'res'] else print('\nЗнак не был принят')
        all = CHarray[0]
except: print('Вы допустили ошибку, попробуйте еще раз')
for i in range(len(CHarray)):
    try:   
        if   ZNarray[i] == '+' : all += CHarray[i+1]
        elif ZNarray[i] == '-' : all -= CHarray[i+1]
        elif ZNarray[i] == '/' : all /= CHarray[i+1] if CHarray[i+1]!=0 else  print('На 0 делить нельзя')
        elif ZNarray[i] == '*' : all *= CHarray[i+1]
        elif ZNarray[i] == '**' : all = all**(CHarray[i+1])
        elif ZNarray[i] == 'sqrt' : all += math.isqrt(CHarray[i+1])
        elif ZNarray[i] == 'sin' : all += math.sin(CHarray[i+1])
        elif ZNarray[i] == 'cos' : all += math.cos(CHarray[i+1])
        elif ZNarray[i] == 'tg' : all += (math.tan(CHarray[i+1]))
        elif ZNarray[i] == '!': 
            for m in range (all):
                if m == 0 : m = 1
                all *=(m)
    except IndexError: 
        print('\nВы ошиблись с вводом знака, в следующий раз будте внимательнее')
        break
print(all)