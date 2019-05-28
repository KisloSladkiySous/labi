import random
print ("Введите границы промежутка для угадывания числа")
print ("Левая граница")
x = int(input())
print ("Правая граница")
y = int(input())
number = random.randint(x, y)
igra = False
while igra == False:
    predict = int(input('Введите ваше число: '))
    if predict == number:
        print('Поздравляю! Вы выиграли!')
        fortune = True
    else:
        if predict > number:
            print('Загаданное число меньше!')
        else:
            print('Загаданное число больше!')
