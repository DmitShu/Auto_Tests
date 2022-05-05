import pytest
from app.calculator import Calculator

class TestCalc:
    # Позитивные тесты
    def setup(self):
        self.calc = Calculator

    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

