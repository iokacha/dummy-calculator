import pytest
from function.calculator import Calculator, Units

def test_calculator_meter_and_integer_only():
    calculator = Calculator()
    result = calculator.sum(
        "3 Meters", 
        "5 Meters"
    )
    assert result == "8 Meters"

def test_calculator_meter_and_float_values():
    calculator = Calculator()
    result = calculator.sum(
        "3.2 Meters", 
        "5.7 Meters"
    )
    assert result == "8.9 Meters"

def test_calculator_different_input_unit():
    calculator = Calculator()
    result = calculator.sum(
        "3 Decimeters", 
        "5 Meters",
    )
    assert result == "5.3 Meters"

    result = calculator.sum(
        "3 Milimeters", 
        "5 Meters",
    )
    assert result == "5.003 Meters"
    
    result = calculator.sum(
        "3 Milimeters", 
        "5 Milimeters",
    )
    assert result == "0.008 Meters"

