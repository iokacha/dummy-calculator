from decimal import Decimal
import enum


# meter is the reference
class Units(enum.Enum):
    Kilometers  = Decimal("0.001")
    Meters      = Decimal("1")
    Decimeters  = Decimal("10")
    Centimeters = Decimal("100")
    Milimeters  = Decimal("1000")
    
    

class Calculator:

    def sum(self, input1, input2, unit="Meters"):
        value1, value2 = self.prepare_in_meter(input1, input2, unit)
        result = Decimal(value1 + value2).normalize()
        return f"{result} {unit}"
    
    def to_meter(self, value, unit):
        return value / Units[unit].value

    def split(self, input):
        value, unit = input.split(" ")
        return value, unit
    
    def prepare_in_meter(self, input1, input2, unit):
        value1, unit1 = self.split(input1)
        value2, unit2 = self.split(input2)
        
        meter_value1 = self.to_meter(Decimal(value1), unit1)
        meter_value2 = self.to_meter(Decimal(value2), unit2)
        return meter_value1, meter_value2