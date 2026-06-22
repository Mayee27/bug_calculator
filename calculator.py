
import unittest

def divide(a, b):
    # Fix: added check to avoid division by zero and raise a meaningful exception instead
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b

def add(a, b):
    return a + b

class TestDivisionFunction(unittest.TestCase):

    def test_divide_by_non_zero(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

if __name__ == '__main__':
    try:
        result = divide(10, 0)  
        print(result)
    except ZeroDivisionError as e:
        print(e)
    unittest.main(argv=[''], verbosity=2, exit=False)
