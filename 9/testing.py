from unittest import TestCase
from numpy import array, subtract, linalg
from math import factorial

class TestArith(TestCase):
    def test_add(self):
        self.assertEqual(1, 4 - 3)
    def test_leq(self):
        self.assertTrue(3 <= 2 * 3)

n0 = array([1, 0, 0, 0])
n1 = array([0, 1, 0, 0])
n2 = array([0, 0, 1, 0])
n3 = array([0, 0, 0, 1])

# set subtracted vectors as columns
s = array([subtract(n1, n0), subtract(n2, n0), subtract(n3, n0)])
m = []
for i in range(len(s[0])-1):
    m.append([s[0][i], s[1][i], s[2][i]])
m = array(m)
d = linalg.det(m)
n = len(s)

print(s)
print(m)
print(d, n)
print(d/factorial(n))
