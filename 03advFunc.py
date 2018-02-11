# -*- coding: utf-8 -*-
# homemade list generator (map func)
from math import cos, pi
from functools import reduce

# function as input
# 'listGenerator' a implementation of 'map' function
def listGen(f, list):
    result = []
    for num in list:
        result.append(f(num))
    return result


print(listGen(cos, [pi, 3.14]))


def normalize(name):
    return name[0].upper() + name[1:].lower()


# test:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# example of reduce function
def prod(list):
    def fn(x, y):
        return x * y
    return reduce(fn, list)


# test:
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# pre-defined dictionary for str2nums
DIGITS = {'0': 0,
          '1': 1,
          '2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9}


def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    a, b = s.split('.')
    a = reduce(fn, map(char2num, a))
    length = len(b)
    b = reduce(fn, map(char2num, b))
    b = b / 10 ** length
    return a + b


# test:
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# Palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_palindrome_2(n):
    num = n
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n = n // 10
    return num == reverse


# test:
output = filter(is_palindrome_2, range(1, 1000))

print('1~1000:', list(output))

if list(filter(is_palindrome_2,
               range(1, 200))) == [1, 2, 3, 4, 5,
                                   6, 7, 8, 9, 11,
                                   22, 33, 44, 55,
                                   66, 77, 88, 99,
                                   101, 111, 121, 131,
                                   141, 151, 161, 171,
                                   181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


# test
L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


# test
L2 = sorted(L, key=by_score)
print(L2)


'''
def createCounter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter
'''

# study until mid-night
def createCounter():
    def counter():
        counter.cnt += 1
        return counter.cnt
    counter.cnt = 0
    return counter


# 测试:
counterA = createCounter()

print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5

counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# Lambda 
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print (L)