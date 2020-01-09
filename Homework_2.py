
# Задача 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
i = 1

while i < 6:
    print(i, "00000000000000000")
    i = i + 1
    if i == 6:
    break
'''
# Задание 2. Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
Greeting = int(input('Введите 10 цифр и я отвечу сколько из них цифра "5":'))
i= 0
while Greeting>0:
    last=Greeting%10
    if last==5:
        i= i+1

    Greeting=Greeting//10
print('Ответ:', i)

'''

#Задача 3 Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
    sum+=i
print(sum)

'''

#Задача 4 Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
sum = 1

for i in range(1,11):
    sum*=i
print(sum)

'''

#Задача 5 Вывести цифры числа на каждой строчке.
'''

integer_number = int(input('Введите число:'))

#print(integer_number%10,integer_number//10)

while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number // 10
'''

#Задача 6 Найти сумму цифр числа.
'''
Greeting=int(input('Введите ряд цифр сумму которых нужно найти:'))
sum = 1
while Greeting>0:
    last=Greeting%10
    sum=sum+last
    Greeting=Greeting//10
print(sum)

'''
#Задача 7 Найти произведение цифр числа.
'''
Greeting=int(input('Введите ряд цифр произведение которых нужно найти:'))
pr = 1
while Greeting>0:
    last=Greeting%10
    pr=pr*last
    Greeting=Greeting//10
print(pr)
'''
#Задача 8 Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
#Задача 9 Найти максимальную цифру в числе
'''
Greeting = int(input('Введите чичло и я назову максимальную цифру в этом числе:'))
max=0
y=0
while Greeting>0:
    last=Greeting%10
    if last > y:
        y=last
    Greeting=Greeting//10
print(y)
'''
# Задача 10 Найти количество цифр 5 в числе
'''
Greeting = int(input('Введите число и я отвечу сколько из них цифра "5":'))
i= 0
while Greeting>0:
    last=Greeting%10
    if last==5:
        i= i+1

    Greeting=Greeting//10
print('Ответ:', i)
'''