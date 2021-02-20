import decimal
import enum


# meter is the reference
class Units(enum.Enum):
    Kilometers  = decimal.Decimal("0.001")
    Meters      = decimal.Decimal("1")
    Decimeters  = decimal.Decimal("10")
    Centimeters = decimal.Decimal("100")
    Milimeters  = decimal.Decimal("1000")

class UnitException(Exception):
    pass

class NonNumerical(Exception):
    pass

class Calculator:

    def sum(self, input1, input2, unit="Meters"):
        value1, value2 = self._prepare_in_meter(input1, input2, unit)
        sumed_in_meter = decimal.Decimal(value1 + value2).normalize()
        result = self._from_meter_to_unit(sumed_in_meter, unit)
        return f"{result} {unit}"
    
    # internal methods 
    def _from_unit_to_meter(self, value, unit):
        return value / Units[unit].value

    def _from_meter_to_unit(self, value, unit):
        return value * Units[unit].value
        
    def _split(self, input):
        value, unit = input.split(" ")
        return value, unit
    
    def _prepare_in_meter(self, input1, input2, unit):
        value1, unit1 = self._split(input1)
        value2, unit2 = self._split(input2)
        # Input validation
        self._validate_unit(unit1)
        self._validate_unit(unit2)
        self._validate_unit(unit)
        self._validate_numeric(value1)
        self._validate_numeric(value2)
        # conversion
        meter_value1 = self._from_unit_to_meter(decimal.Decimal(value1), unit1)
        meter_value2 = self._from_unit_to_meter(decimal.Decimal(value2), unit2)
        return meter_value1, meter_value2

    def _validate_unit(self, unit):        
        try:
            Units[unit].value
        except KeyError as e:
            raise UnitException(f"Exception at {unit} : Invalid Metric Unit Exception")
    
    def _validate_numeric(self, value):        
        try:
            decimal.Decimal(value)
        except decimal.InvalidOperation:
            raise NonNumerical(f"Exception at {value} : Invalid Numeric Value Exception")


            