print("Введите a")
a = int(input())
print("Введите б")
b = int(input())
print("Введите с")
c = int(input())
print("Введите к")
k = int(input())
print("Введите d")
d = int(input())
if b!=0 and a!=0:
 print (abs(((a**2-b**3-c**3*a**2)*(b-c+c*(k-d/b**3))-(k/b-k/a)*c)**2-2000))
else:
 print ("oшибка, деление на 0")