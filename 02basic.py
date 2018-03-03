# -*- coding: utf-8 -*-
import math

# Data type

# Int
# 1，100，-8080，0

# Float
# 1.23，3.14，-9.01
# 1.23e9, 1.2e-5

# String
# 'abc'，"xyz"
# Escape character:
# >>> print('I\'m \"OK\"!')
# I'm "OK"!
# r'' represents for no escape character by default
# >>> print(r'\\\t\\')
# \\\t\\

# bool
# True, False
# >>> True and True
# True
# >>> True or True
# True
# >>> not True
# False

# None

# String to ASCII
# >>> ord('A')
# 65
# ASCII to String
# >>> chr(66)
# 'B'

# list
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])


# if elif example
def bmi(height, weight):
    my_bmi = float(weight) / float(height) ** 2
    if my_bmi < 18.5:
        status = 'low weight'
    elif my_bmi < 25:
        status = 'normal'
    elif my_bmi < 28:
        status = 'over weight'
    elif my_bmi < 32:
        status = 'obesity'
    else:
        status = 'super obesity'
    # print('Your bmi is %f, and you are %s' % (my_bmi, status))
    return my_bmi, status


# if elif example 2
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# a function return 2 results
def quadratic(a, b, c):
    delta = math.sqrt(b * b - 4 * a * c)
    if delta < 0:
        raise TypeError('no solution')

    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    return x1, x2


# function's default parameter
def power(x, n=2):
    s = 1
    for _ in range(n):
        s *= x
    return s


# The single asterisk form ( *args ) is used to pass
# a non-keyworded, variable-length argument list
def calc(*args):
    sum = 0
    for num in args:
        sum += num * num
    return sum

# a=[6,2,4,5.4]
# print(calc(*a))

# game register system
# required information: ID password score
# other information: gender age height weight


user1 = {'ID': 'foo',
         'password': '1234',
         'score': 99,
         'gender': 'Male',
         'age': 27,
         'height': 1.78,
         'weight': 70,
         'other': 'eat a lot'}

user2 = {'ID': 'bar',
         'password': '1234',
         'score': 60,
         'gender': 'Female',
         'age': 18}

user3 = {'ID': 'bread',
         'password': '1234',
         'score': 0,
         'age': 27,
         'height': 1.80,
         'weight': 87}


# The double asterisk form is used to pass
# a keyworded, variable-length argument list
def onClick(**kw):
    if ('ID' in kw) and ('password' in kw) and ('score' in kw):
        print('Hello ' + kw['ID'] + ', your socre is ' + str(kw['score']))
        if 'height' in kw and 'weight' in kw:
            my_bmi, status = bmi(kw['height'], kw['weight'])
            print('Your bmi is %f, and you are %s' % (my_bmi, status))
            # bmi(kw['height'], kw['weight'])
    else:
        print('invalid data')

# onClick(**user1)
# onClick(**user2)
# onClick(**user3)


# Another example for *args
def product(*args):
    # args == ()
    if len(args) == 0:
        raise TypeError
    result = 1
    for arg in args:
        result = result * arg
    return result


# Recursive factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# Recursive fibonacci sequence
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# Solve the hanot tower problem using recursive
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)
# hanoi(3, 'A', 'B', 'C')


# Remove 'extra' spaces of a string
def trim(s):
    if s == '':
        return s
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    else:
        return s
# print(trim('   Abc D e   '))


# Find min and max simultaneously
def findMinAndMax(nums):
    if nums == []:
        return None, None
    max, min = nums[0], nums[0]
    for num in nums:
        if num > max:
            max = num
        if num < min:
            min = num
    return min, max


# list generator
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]


# Yanghui triangles, a practice for generator
def triangles():
    L = [1]
    while True:
        yield L
        L = L + [0]
        L = [L[i - 1] + L[i] for i in range(len(L))]


# fibonacci sequence kidnap edition generator
def fib2(n):
    a = 0
    b = 1
    for _ in range(n):
        yield(b)
        a, b = b, a + b
    return 'Done'


def fib3():
    a = 0
    b = 1
    yield(b)  # a = 0 b = 1
    a, b = b, a + b  # a = 1 b = 1
    yield(b)  # a = 1 b = 1
    a, b = b, a + b
    yield(b)
    a, b = b, a + b
    yield(b)
    a, b = b, a + b
    yield(b)
    a, b = b, a + b
    return 'Done'


g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# generator
def triangles2():
    L = [1]
    while True:
        yield L
        L = L + [0]
        L = [L[i] + L[i - 1] for i in range(len(L))]


def triangles3():
    L = [1]
    while True:
        yield L
        L = L + [0]
        G = []
        for i in range(len(L)):
            G.append(L[i] + L[i - 1])
        L = G


def triangles4():
    n = 1
    L = [1]
    yield L

    while True:
        n += 1
        G = L[:]
        L = [None for _ in range(n)]
        L[0], L[-1] = 1, 1
        for j in range(1, n - 1):
            L[j] = G[j - 1] + G[j]
        yield L


# test
n = 0
results = []
for t in triangles4():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('pass!')
else:
    print('fail!')
