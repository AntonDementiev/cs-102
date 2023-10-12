import unittest
import sys
sys.path.append(r'/Users/anton_dem/Desktop/Labs/Proga/cs-102')
from src.lab1.calculator import plus, minus, multiply, divide

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_plus(self):
        self.assertEquals(plus(2, 2), f"Сумма: {4}")
    
    def test_minus(self):
        self.assertEquals(minus(5, 2), f"Разность: {3}")
    
    def test_multiply(self):
        self.assertEquals(multiply(5, 2), f"Произведение: {10}")
    
    def test_divide(self):
        self.assertEquals(divide(10, 2), f"Частное: {float(5)}")