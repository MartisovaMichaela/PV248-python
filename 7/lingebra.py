#!/usr/bin/env python3

from numpy import loadtxt, linalg, array, allclose, dot
from pprint import pprint as pp
import re

matrix = loadtxt("matrix.txt")
print("matrix:\n", matrix)
print("\n===\n")

# ex1
print("determinant:", linalg.det(matrix))
print("inverse:\n", linalg.inv(matrix))
print("\n===\n")

# ex2
# 2 * x0 + 3 * x1 = 10
# 3 * x0 + 2 * x1 = 10
a = array([[2, 3], [3, 2]])
b = array([10, 10])
x = linalg.solve(a, b)
print("result:", x)
print("correct answer?", allclose(dot(a, x), b))
print("\n===\n")

# ex3
# TODO parse input: remove variables
# TODO present output
# 2x + 3y = 5
#  x -  y = 0
f = open("equation.txt", "r")
s = f.read().split()
pp(s)
a = []
b = []
for i in s:
    parts = i.split("=")
    a.append(re.split('\+|-', parts[0]))

    b.append(parts[1])
print(a)
print(b)
