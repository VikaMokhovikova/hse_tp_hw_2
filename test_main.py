import unittest
import pytest
import main
import time
import math

# import matpotlib

class MyTest(unittest.TestCase):
    with open ('file1.txt', 'r') as file1:
        array = list(map(int, file1.readline().split()))

    def test_min(self):
        self.assertEqual(main._min(self.array), min(self.array))

    def test_max(self):
        self.assertEqual(main._max(self.array), max(self.array))

    def test_sum(self):
        self.assertEqual(main._sum(self.array), sum(self.array))

    def test_mult(self):
        self.assertEqual(main._mult(self.array), math.prod(self.array))

    def test_time(self):
        time_begin = time.time()
        self.assertEqual(main._min(self.array), min(self.array))
        print('\nЗатраченное время на тест:', time.time() - time_begin)
if __name__ == '__main__':
    unittest.main()


'''
with open('file1.txt', 'r') as file1:
    array = list(map(int, file1.readline().split()))


def test_min():
    assert main._min(array) == min(array)


def test_max_():
    assert main._max(array) == max(array)


def test_sum_():
    assert main._sum(array) == sum(array)


def test_mult_():
    assert main._mult(array) == math.prod(array)


def test_time_():
    time_begin = time.time()
    assert main._min(array) == min(array)
    print('Затраченное время на тест:', time.time() - time_begin)


if __name__ == '__main__':
    pytest.main()
'''
