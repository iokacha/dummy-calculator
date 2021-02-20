from decimal import Decimal
import enum


# meter is the reference
class Units(enum.Enum):
    Kilometers  = 0.001
    Meters      = 1
    Decimeters  = 10
    Centimeters = 100
    Milimeters  = 1000
    
    

class Calculator:

    def sum(self, input1, input2, unit="Meters"):
        value1, unit1 = input1.split(" ")
        value2, unit2 = input2.split(" ")
        meter_value1 = self.to_meter(Decimal(value1), unit1)
        meter_value2 = self.to_meter(Decimal(value2), unit2)
        result = Decimal(meter_value1 + meter_value2).normalize()
        return f"{result} {unit}"
    
    def to_meter(self, value, unit):
        return value / Units[unit].value