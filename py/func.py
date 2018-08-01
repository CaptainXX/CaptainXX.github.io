#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, *, city='Beijing', gender):
    print('name:',name,'age:', age, city, gender)

def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
	
def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=' ,kw)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
	
def trim(s):
    if s == '':
        #print(s)
        return s
    while s[0] == ' ':
        s = s[1:len(s)]
        if s == '':
            #print(s)
            return s
        #print(s)
    while s[-1] == ' ':
        s = s[0:-1]
        #print(s)
    #print(s)
    return s

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles():
    L = [1]
    while True:
        yield(L)
        L = [1] + [L[i - 1] + L[i] for i in range(1, len(L))] + [1]
        
def normalize(name):
    newname = name[0].upper()
    for i in range(1, len(name)):
        newname =  newname + name[i].lower()
    return newname
    
def prod(L):
    def multi(x, y):
        return x * y
    return reduce(multi, L)

def str2float(s):
    digit = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    def char2num(s):
        return digit[s]
    def fn(x, y):
        return x*10 + y
    news, dot = '', 1
    for r in s:
        if r == '.':
            p = dot
            continue
        else:
            dot = dot * 10
            news = news + r
    return reduce(fn, map(char2num, news)) / p

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0
    
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

def nums(): #所有自然数
    n = 1
    while True:
        yield n
        n = n + 1

        
def is_palindrome(n):
    L = []
    while n > 0:
        L.append(n % 10)
        n = n // 10
        #print(L)
    for i in range(len(L)//2):
        if L[i] != L[len(L)-1-i]:
            return False
    return True

def by_name(t):
    return t[0]

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
    
def createCounter():
    i = [0]
    def counter():
        i[0] = i[0] + 1
        return i[0]
    return counter
