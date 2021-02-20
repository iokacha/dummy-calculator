import pytest
from function.calculator import Calculator, Units
from function.calculator import NonNumerical, UnitException

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

    result = calculator.sum(
        "1 Kilometers", 
        "1 Meters",
    )
    assert result == "1001 Meters"


def test_calculator_with_custom_output_unit():
    calculator = Calculator()
    result = calculator.sum(
        "3 Meters", 
        "5 Meters",
        "Milimeters"
    )
    assert result == "8000 Milimeters"

    result = calculator.sum(
        "1 Kilometers", 
        "5 Meters",
        "Milimeters"
    )
    assert result == "1005000 Milimeters"

def test_calculator_with_invalid_units():
    calculator = Calculator()
    with pytest.raises(UnitException) as ex:
        result = calculator.sum(
            "3 AlienMeter", 
            "5 Meters",
            "Milimeters"
        )
    assert "AlienMeter" in str(ex.value)
    with pytest.raises(NonNumerical) as ex:
        result = calculator.sum(
            "X Meters", 
            "5 Meters",
            "Milimeters"
        )
    assert "X" in str(ex.value)