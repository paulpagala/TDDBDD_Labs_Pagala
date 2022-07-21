import pytest

class Calculator:
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("This calculator's name is " + base_calculator.name)

    #change the name

    base_calculator.name = "Changed Calculator"
    print("This calculator's name is " + base_calculator.name)
    #print(calc.add(1,1))

    assert True

def test_lab4_test2(base_calculator):
    print("This calculator's name is "+ base_calculator.name)

    assert True

def test_subtract():
    assert Calculator.subtract(base_calculator,9, 5) == 4
    assert Calculator.subtract(base_calculator,4, 9) == -5
    assert Calculator.subtract(base_calculator,6, 6) == 0
    assert Calculator.subtract(base_calculator,5, 4) == 1

def test_multiply():
    assert Calculator.multiply(base_calculator,5, 4) == 20
    assert Calculator.multiply(base_calculator,-4,5) == -20
    assert Calculator.multiply(base_calculator,-3,-2) == 6
    assert Calculator.multiply(base_calculator,3, 0.5) == 1.5
    assert Calculator.multiply(base_calculator,3, 0) == 0
    assert Calculator.multiply(base_calculator,3, 4) == 12

