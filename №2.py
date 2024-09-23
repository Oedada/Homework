from random import randint
a = [0]*10
print("-----Вывод значений-----")
for i in range(10):
    a[i] = randint(0,20)
    print(a[i], end = " ")