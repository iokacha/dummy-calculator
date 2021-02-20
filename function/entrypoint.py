import json
from calculator import Calculator, NonNumerical, UnitException, FormatException


def sum(event, context):
    data = json.loads(event.get("body"))
    data1 = data.get("input1", '')
    data2 = data.get("input2", '')
    units = data.get("units", "Meters")

    try:
        calculator = Calculator()
        result = calculator.sum(data1, data2, units)
        status = 200
    except (UnitException, NonNumerical, UnitException, FormatException) as e:
        status = 400
        result = str(e)
    return {
        "statusCode": status,
        "body": json.dumps({
            "result": result
        })
    }
