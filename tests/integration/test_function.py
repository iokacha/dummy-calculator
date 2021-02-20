import json
import pytest
from function import entrypoint

def api_gateway_event(body):
    return {
        "body": body,
        "resource": "/{proxy+}",
        "requestContext": {
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef"
        },
        "headers": {
            "User-Agent": "Custom User Agent String"
        },
        "httpMethod": "POST",
        "path": "/sum",
    }

def call_calculator_sum(request_body):
    body = api_gateway_event(json.dumps(request_body))
    result = entrypoint.sum(body, "")
    return result

def test_lambda_sum_standard(mocker):    
    result = call_calculator_sum({
        "input1": "18 Meters",
        "input2": "20 Meters"
    })
    response = json.loads(result.get("body"))
    assert response["result"] == "38 Meters"
    assert result["statusCode"] == 200


def test_lambda_sum_with_invalid_unit(mocker):    
    result = call_calculator_sum({
        "input1": "18 AlienMeter",
        "input2": "20 Meters"
    })
    response = json.loads(result.get("body"))
    assert "AlienMeter" in response["result"]
    assert result["statusCode"] == 400

    