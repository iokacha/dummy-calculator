import pytest
from function.calculator import Calculator

def test_calculator_meter():
    calculator = Calculator()
    # first test 
    result = calculator.sum(
        "3 Meters", 
        "5 Meters"
    )
    assert result == "8 Meters"
