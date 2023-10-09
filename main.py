
# a = 10
# b = 10.0
# if a == b:
#     print(1)

# a = '10'
# print(a*100)

# a=10
# b="10"
# print(str(a))
# print(str(b))
# if str(a) == int(b):
#     print(1)
# elif int(a)==int(b):
#     print(2)
# elif str(a)==str(b):
#     print(3)
# else:
#     print(1)

# a = 5
# b = 6
# c = 7
# if a == b == c:
#     print(3)
# if a != b != c:
#     print(0)

# a = int(input("Year: "))
# if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
#     print(1)
# else:
#     print(0)

# day1 = int(input("Day1: "))
# month1 = int(input("Month1: "))
# year1 = int(input("Year1: "))
# day2 = int(input("Day2: "))
# month2 = int(input("Month2: "))
# year2 = int(input("Year2: "))
# if year1 > year2:
#     print(2)
# elif year2 > year1:
#     print(1)
# else:
#     if month1 > month2:
#         print(2)
#     elif month2 > month1:
#         print(1)
#     else:
#         if day1 > day2:
#             print(2)
#         elif day2 > day1:
#             print(1)
#         else:
#             print("=")

# a = str(input("Vvedi cislo: "))
# c = 0
# if int(a[0]) % 2 == 0:
#     c += 1
# if int(a[1]) % 2 == 0:
#     c += 1
# if int(a[2]) % 2 == 0:
#     c += 1
# print(c)
# a = int(input("Vvedi cislo a: "))
# b = int(input("Vvedi cislo b: "))
# c = int(input("Vvedi cislo c: "))
# d = int(input("Vvedi cislo d: "))
# if b == c == d:
#     print(a)
# if a == c == d:
#     print(b)
# if a == b == d:
#     print(c)
# if a == b == c:
#     print(d)
# как ходит король
# x1 = int(input("Vvedi cislo x1: "))
# y1 = int(input("Vvedi cislo y1: "))
# x2 = int(input("Vvedi cislo x2: "))
# y2 = int(input("Vvedi cislo y2: "))
# if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:  # if x1==x2-1 and y1==y2-1:
#     print(1)
# else:
#     print(0)
# как ходит ферзь
# x1 = int(input("Vvedi cislo x1: "))
# y1 = int(input("Vvedi cislo y1: "))
# x2 = int(input("Vvedi cislo x2: "))
# y2 = int(input("Vvedi cislo y2: "))
# if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
#     print(1)
# else:
#     print(0)
# # как ходит слон
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')
# # как ходит конь
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# dx = abs(x1 - x2)
# dy = abs(y1 - y2)
# if dx == 1 and dy == 2 or dx == 2 and dy == 1:
#     print('YES')
# else:
#     print('NO')
# # как ходит ладья
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')
# a = str(11)
# b = str(float(11))
# if a == b:
#     print(1)
# if int(float(a)) == int(float(b)):
#     print(2)
# if int(a) == b:
#     print(3)
# a = 1
# b = 2
# c = 3
# if not a == b == c:
#     a, b, c = c, a, b
#     print(a)
#     print(b)
#     print(c)
# if a == a:
#     a, b = c, a
#     print(a)
#     print(b)
#     print(c)
# if a == a:
#     a, c = b, a
#     print(a)
#     print(b)
#     print(c)
# print("Стороны:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a + b > c and a + c > b and b + c > a:
#     print("Треугольник существует")
# else:
#     print("Треугольник не существует")
# a = int(input("gram "))
# if a > 500:
#     b = a/1000*230
#     print("Price "+str(b))
# else:
#     b = a/1000*270
#     print("Price "+str(b))
# m = input("Enter: ")
# result = input("Единица измерения (b,kb,mb,gb,tb)")
# if result == 'b':
#     print(int(m)*8)
# if result == 'kb':
#     print(int(m)*1024*8)
# if result == 'mb':
#     print(int(m)*1024*1024*8)
# result = int(input("Введите число: "))
# a = 0
# for i in range(result+1):
#     a += i
#     print(a)
# result = int(input("Введите число: "))
# a = 1
# for i in range(1, result+1):
#     a = a/i
#     print(a)
# result = int(input("Введите число: "))
# a = 1
# r = 0
# for i in range(1, result+1):
#     a = i**i
#     r += a
#     print(r)
# a1 = [1, 2, 3, 4, 5]
# a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = 0
# for temp in a2:
#     if temp % 3 == 0:
#         r += 1
# print(r)
#     if temp % 2 == 0:
#         r += 1
#     else:
#         r-+-1
# print(r)
# n = int(input("Введите число: "))
# result = 0
# i = 0
# while n > i:
#     i = i+1
#     result = result+i
# print(result)
# n = int(input("Введите число: "))
# a = 0
# b = 0
# while a < n:
#     a = 2**b
#     b = b+1
#     if a > n:
#         break
#     print(a)
# if 'hello': #true
#     print(1)
# a = int(input("Vvedi cislo a: "))
# b = int(input("Vvedi cislo b: "))
# i = 0
# while a > b:
#     # print(a)
#     a = a-b
#     i = i+1
# print("Celaya cast: "+str(i))
# print("Ostatok: "+str(a))
# 1 вариант переворачивания числа (13 урок)
# a = int(input("Vvedi cislo a: "))
# x=a%10 #последнее число
# y=a//10%10 #десятки
# z=a//100 #сотни
# print(y)
# 2 вариант
# a = input("Vvedi cislo a: ")
# b=''
# for i in a:
#     b=i+b
# print(b)
#3 вариант
# n1 = int(input("Введите целое число: "))
# n2 = 0
# while n1 > 0:
#     # находим остаток - последнюю цифру
#     digit = n1 % 10
#     # делим нацело - удаляем последнюю цифру
#     n1 = n1 // 10
#     # увеличиваем разрядность второго числа
#     n2 = n2 * 10
#     # добавляем очередную цифру
#     n2 = n2 + digit
# print('"Обратное" ему число:', n2)
# # факториал
# n = int(input("Введите целое число: "))
# r=1
# for i in range(1,n+1):
#     r*=i
# print(r)
# урок 11 с факториалом
# n = int(input("Введите целое число: "))
# r=1
# s=0
# for i in range(1,n+1):
#     r*=i
#     s+=r
# print(s)

# 12 урок
# n = int(input("Введите целое число: "))
# i=1
# result = 0
# while i <= n:
#     result += i
#     i+=1
# print(result)
# 12 урок
# a = int(input("Введите целое число: "))
# b = int(input("Введите целое число: "))
# while a <= b:
#     print(a)
#     a +=1
# 12 урок
# n = int(input("Введите целое число: "))
# i=1
# while i <= n:
#     print(i)
#     i += i
# # урок 13 (% и //)
# a = int(input("Введите целое число: "))
# b = int(input("Введите целое число: "))
# ost=0
# while (a-b)>0:
#     ost+=1
#     a=a-b
# print(ost, a)

# проверка на простое число (урок 13 дз)
# n = int(input("Введите целое число: "))
# simple = True
# i=2
# while i < n:
#     # print(i, simple)
#     if n%i == 0:
#         simple = False
#         break
#     i += 1
# if simple:
#     print(1)
# else:
#     print(0)
# урок 14 числа Фибоначчи
# вывод чисел
# fib1 = fib2 = 1
# n = int(input())
# print(fib1, fib2, end=' ')
# while n > 2: # while fib2 < n - для вывода до числа большего N и убрать n-=1
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
#     n -= 1
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
# a=5
# b=a%6**2
# print(b)
# урок 14 ДЗ
# a = int(input("Введите целое число: "))
# b = int(input("Введите целое число: "))
# i = 1
# result = 0
# while i <= a:
#     result += i**b
#     i+=1
# print(result)
# урок 14 (задача повышенной сложности)
# -----------------
# import math
# n = int(input("Введите целое число N: "))
# x = float(input("Введите целое число X: "))
# result = 1 + x
# i = 2
# factorial = 1
# while i <= n:
#     factorial=math.factorial(i)
#     # for temp in range(2, i + 1):
#     #     factorial *= i
#     # print(factorial)
#     result += x**i/factorial
#     i+=1
#     print(result)
#-----------------------
# 11 lesson
# a=int(input("Введи a"))
# b=int(input("Введи b"))
# for i in range(a,b+1):
#     i+=i
# print(i)
# n=int(input("Введи n"))
# a=0
# for i in range(2,n+1):
#     a+=(i-1)*i
# print(a)
# n=True
# t=False
# print(n+t)
#----------------------
# # 14 урок
# a=0
# for temp in range(5):
#     a+=1
#     if a==3:
#         a+=2
#     if a==4:
#         a+=3
#     if a==5:
#         a+=4
#     else:
#         a+=1
#     print(a)
#--------------------------
# урок 15
# name = "fff"
# print("dfsdfds {0}".format(name), "sdf")
# a="hello"
# b=list(a)
# print(b)
# c=b[0]
# print(c)
# temp=[0,"hello"]
# print(temp[1][1])
# a=[int(input()),int(input())]
# print(a)
# # первый и последний
# a=[int(input()), int(input()), int(input())]
# print(a[0])
# print(a[-1])
# # нечетные
# a=int(input())
# b=[]
# c=1
# for i in range(1, a+1):
#     b.append(c)
#     c+=2
# print(b)
# # среднее арифметическое
# a=[int(input()), int(input()), int(input()), int(input())]
# r=0
# for i in a:
#     r+=i
# print(int(r/len(a)))
# print(a[0])
# # 16 урок
# # max число
# n=int(input("kol-vo"))
# items=[]
# max=0
# for i in range(n):
#     item = int(input("vvedi cislo"))
#     items.append(item)
# for i in items:
#     if i > max:
#         max = i
# print(max)
# min и нечетное число
# n=int(input("kol-vo"))
# items=[]
# min=99999
# for i in range(n):
#     item = int(input("vvedi cislo"))
#     items.append(item)
# for i in items:
#     if i%2==1:
#         if i < min:
#             min = i
# if min==99999:
#     print(0)
# else:
#     print(min)
# пары элементов
# n=int(input("kol-vo"))
# items=[]
# result=0
# for i in range(n):
#     item = int(input("vvedi cislo"))
#     items.append(item)
# for el in items:
# ///
# задача повышенной сложности
# n=int(input("kol-vo"))
# items=[]
# result=0
# for i in range(n):
#     item = int(input("vvedi cislo"))
#     items.append(item)
# for el in items:
#     result += items.count(el)-1
# r=result//2
# print(r)
# урок 17
# a=100
# if not a>100:
#     for i in range(10):
#         a+=1
#         if a%5==0:
#             a+=10
#             print(a)
# else:
#     print(0)
# a=0
# b=10
# while a < b:
#     for i in range(10):
#         a+=1
#         if i==3:
#             break
#     print(a)
# # ROT13
# n=input("Vvedi ")
# a='abcdefghijklmnopqrstuvwxyz '
# f=""
# со списком
# b=[]
# d=''
# # for i in n:
# #     c = int(a.index(i))
# #     f=c+13
# #     if f > 26:
# #         f-=26
# #     e=a[f]
# #     b.append(e)
# # for item in b:
# #     d+=item
# # print(d)
# со строками
# for i in n:
#     b=a.index(i)
#     c=int(b+14)
#     if c==27:
#         c=" "
#     elif c > 27:
#       c-=27
#     d=a[c]
#     f+=d
# print(f)
# урок 19
# def twinkle_twinkle():
#     print('a')
#     print('b')
#     print('c')
#     print('d')
#     print('e')
#     print('f')
# def repeat_lyrics():
#     twinkle_twinkle()
#     twinkle_twinkle()
# repeat_lyrics()
# def cel():
#     c=int(input("Temperature v C = "))
#     f=1.8*c+32
#     print(f)
# cel()
# def far():
#     f=int(input("Temperature v F = "))
#     c=5/9*(f-32)
#     print(c)
# far()
# a=input('C or T ')
# if a=='C':
#     cel()
# elif a=='T':
#     far()
# else:
#     print('Error')

# a=input('temperature ')
# if a=='C':
#     cel()
# elif a=='T':
#     far()
# else:
#     print('Error')

# lesson 21
# def sum(a, b):
#     print(a+b)
# c=input("a ")
# d=input("b ")
# sum(eval(c), eval(d)) # eval - принимает что-то как input(), но умеет считать, если ввести не число, а выражение
# def game(a,b=3):
# #     if b=='':
# #         b=3
# #     v = a % b
# #     y = b - v
# #     print(y)
# # game(112)
# import math
# def get_sum(*args): #неограниченное кол-во аргументов
#     n=0
#     for i in args:
#         n+=i
#     print(n)
# get_sum(1,2,3,4,5)
# get_sum(-1,0,math.inf)
# ????????
# def medic(*args):
#     if args[0]%args[1]==0:
#         print(0)
#     else:
#         print(args[1]-args[0]%args[1])
# medic(8,7)
# ДЗ
# def twinkle_twinkle():
#     print(1)
# def repeat_twinkle(k):
#     for i in range(k):
#         twinkle_twinkle()
# repeat_twinkle(int(input('kol-vo ')))



# урок 22
# def cislo(a):
#     return a**2
# b=cislo(float(input()))
# print(b)
# 23 урок
# def multiply(x: int, y: int) -> int:
#     print(x*y)
# multiply('>_> ', 10)
# def dnk(x):
#     a=x.count("A")
#     t=x.count("T")
#     c = x.count("C")
#     g = x.count("G")
#     print(a, t, c, g, sep=" ")
# dnk('AAGTGC')
# def dnk(x):
#     a=x.replace("T", "U")
#     print(a)
# dnk('TTCAG')
# import turtle
# turtle.setup(400,500)
# turtle.speed(100)
# n=50
# for i in range(n):
#     for i in range(4):
#         turtle.forward(n)
#         turtle.left(90)
#     n-=1
# turtle.mainloop()

# import requests
# from bs4 import BeautifulSoup
#
# url="https://skysmart.ru/programmirovanie-dlya-detej?direction=basics"
#
# head={"User-Agent":""}
#
# r=requests.get(url, headers=head)
# src=r.text
#
# source=requests.get(url, headers=head).text

# урок 20
# def a(w,z):
#     print(int(w)+int(z))
# a(144, 12**2)
# DZ
# def a():
#     a=3
#     b=4
#     c = str(a) + ' ' + str(b)
#     return c
# print(a())
# DZ 23
# def cep(str):
#     for i in str:
#         if i not in "ATCG":
#             return False
#     return True
#
# print(cep(input()))
# 26 словарь по словам
# def slovar(a):
#     y = a.split()
#     b = {}
#     for i in y:
#         b[i] = y.count(i) # вывод слов и их кол-ва в словарь
#     return b
# print(slovar(input()))

# def slovar(a):
#     y = a.split()
#     b = []
#     c = []
#     d = {}
#     # for i in y:
#     #     b.append(i)
#     #     c.append(y.count(i))
#     # d = dict.fromkeys(b, 0)
#     for i in y:
#         d[i] = d.get(i,0)+1
# print(slovar(input()))

from collections import Counter
import re


def most_common_words(text, num_words):
    # Извлекаем слова из текста, удаляя пунктуацию и приводя к нижнему регистру
    words = re.findall(r'\w+', text.lower())

    # Используем Counter для подсчета встречаемости слов
    word_counter = Counter(words)

    # Находим наиболее часто встречающиеся слова
    most_common = word_counter.most_common(num_words)

    return most_common


text = "а б в г д д г в б а текст сюда. Здесь можно вставить большой объем текста для анализа."
num_words = 5

common_words = most_common_words(text, num_words)
print(common_words)



