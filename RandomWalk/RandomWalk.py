__author__ = 'zhan'

from numpy import *
f2 = float(2)
f4 = float(4)
f3 = float(3)
f5 = float(5)
Q = array([[0, 1/f2, 0, 0, 0, 0, 0, 0, 1/f2],
           [1/f5, 0, 1/f5, 1/f5, 0, 1/f5, 1/f5, 0, 0],
           [0, 1/f2, 0, 0, 1/f2, 0, 0, 0, 0],
           [0, 1/f2, 0, 0, 1/f2, 0, 0, 0, 0], #v3
           [0, 0, 1/f3, 1/f3, 0, 0, 0, 0, 1/f3],
           [0, 1/f2, 0, 0, 0, 0, 0, 1/f2, 0],
           [0, 1/f2, 0, 0, 0, 0, 0, 1/f2, 0], #v6
           [0, 0, 0, 0, 0, 1/f2, 1/f2, 0, 0],
           [1/f2, 0, 0, 0, 1/f2, 0, 0, 0, 0]])
p = array([0, 1/f2, 0, 0, 0, 0, 0, 0, 1/f2])
for i in range(0, 100):
    p = dot(transpose(p), Q)

print p