#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
    
@log
def now():
    print('2018-1-31')
    
now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
    
@logger('DEBUG')
def today():
    print('2018-1-31')
    
today()
print(today.__name__)



def metric(fn):
    time.clock()
    print('%s executed in %s ms' % (fn.__name__, time.clock()))
    return fn
    
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

print(fast(11, 22), slow(11, 22, 33))