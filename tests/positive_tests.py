import pytest
from app.calculator import Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_calculator_multiply_correctly(self):
        assert self.calc.multiply(self, 2, 5) == 10

    def test_calculator_division_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_calculator_subtraction_correctly(self):
        assert self.calc.subtraction(self, 13666, 13000) == 666

    def test_calculator_adding_correctly(self):
        assert self.calc.adding(self, 20000000000000, 1) == 20000000000001