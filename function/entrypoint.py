import json
from calculator import Calculator, NonNumerical, UnitException


def sum(event, context):
    data1 = event.get("input1")
    data2 = event.get("input2")
    units = event.get("units", "Meters")

    try:
        calculator = Calculator()
        result = calculator.sum(data1, data2, units)
        status = 200
    except (UnitException, NonNumerical) as e:
        status = 400
        result = str(e)
    return {
        "statusCode": status,
        "body": json.dumps({
            "result": result
        })
    }
