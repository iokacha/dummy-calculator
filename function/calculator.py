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
        self._validate_units(unit1, unit2, unit)
        self._validate_values(value1, value2)
        # conversion
        meter_value1 = self._from_unit_to_meter(decimal.Decimal(value1), unit1)
        meter_value2 = self._from_unit_to_meter(decimal.Decimal(value2), unit2)
        return meter_value1, meter_value2

    def _validate_units(self, unit1, unit2, output_unit):        
        try:
            Units[unit1].value
            Units[unit2].value
            Units[output_unit].value
        except KeyError:
            raise UnitException()
    
    def _validate_values(self, value1, value2):        
        try:
            decimal.Decimal(value1)
            decimal.Decimal(value2)
        except decimal.InvalidOperation:
            raise NonNumerical()


            