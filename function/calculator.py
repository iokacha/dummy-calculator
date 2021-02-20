from decimal import Decimal
class Calculator:

    def sum(self, input1, input2, unit="Meters"):
        value1, unit1 = input1.split(" ")
        value2, unit2 = input2.split(" ")
        result = (Decimal(value1) + Decimal(value2)).normalize()
        return f"{result} {unit}" 