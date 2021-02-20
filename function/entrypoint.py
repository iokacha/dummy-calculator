import json
from .calculator import Calculator, NonNumerical, UnitException


def sum(event, context):
    calculator = Calculator()
    body = json.loads(event.get("body"))
    data1 = body.get("input1")
    data2 = body.get("input2")

    try:
        result = calculator.sum(data1, data2)
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
