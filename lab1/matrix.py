import unittest
import numpy as np


def m_dot(X, Y):
    if X.shape[1] != Y.shape[0]:
        return None
    return [[sum(a * b for a, b in zip(X_ROW, Y_COL)) for Y_COL in zip(*Y)] for X_ROW in X]


def m_t(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
# print(Y)

#print(np.dot(X, Y))
#print(m_dot(X, Y))


class m_test(unittest.TestCase):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        super().__init__()

    def setUp(self):
        pass

    def test_mul(self):
        self.assertEqual(np.dot(self.X, self.Y), m_dot(self.X, self.Y))

    def test_x(self):
        self.assertEqual(self.X.T, m_t(self.X))

    def test_y(self):
        self.assertEqual(self.X.T, m_t(self.X))


    
    
# print(np.dot(X, Y), m_dot(X, Y))
# print(X.T == m_t(X))
# print(Y.T == m_t(Y))

arr = np.arange(50)
X = arr.reshape(10, 5)
#print(X)
arr = np.arange(100)
Y = arr.reshape(5, 20)
print(m_dot(X, Y) == np.dot(X, Y))
