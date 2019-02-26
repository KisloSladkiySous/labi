import random
koll=0;
print ("Введите границы промежутка для угадывания числа")
print ("Левая граница")
x = int(input())
print ("Правая граница")
y = int(input())
n = random.randint(x,y)
m = int(input())
while m!=n:
 if m<x or m>y:
  print("Введенное число вне границ")
  koll=koll-1
 m = int(input())
 koll=koll+1
else:
    print("Мои поздравления,загаданное мною число=",n,"Количество попыток",koll)