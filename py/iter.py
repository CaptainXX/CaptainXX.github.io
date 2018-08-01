#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinAndMax(L):
    i = 0
    while i < len(L) - 1:
        if L[i] > L[i + 1]:
            temp = L[i]
            L[i] = L[i + 1]
            L[i + 1] = temp
        i = i + 1
    return (L[0], L[len(L) - 1])

print(findMinAndMax([7, 1]))
print(findMinAndMax([7, 1, 3, 9, 5]))