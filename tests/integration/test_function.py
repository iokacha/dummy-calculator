import json
import pytest
from function.entrypoint import *

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
    result = sum(body, "")
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


def test_lambda_sum_standard_custom_output(mocker):    
    result = call_calculator_sum({
        "input1": "18 Meters",
        "input2": "20 Meters",
        "units" : "Decimeters"
    })
    response = json.loads(result.get("body"))
    assert response["result"] == "380 Decimeters"
    assert result["statusCode"] == 200


def test_lambda_sum_empty_body(mocker):    
    result = call_calculator_sum({})
    response = json.loads(result.get("body"))
    assert result["statusCode"] == 400
    assert " Expecting 'Value Unit'" in response["result"]

def test_lambda_sum_empty_inputs(mocker):    
    result = call_calculator_sum({
        "input1": "",
        "input2": ""
    })
    response = json.loads(result.get("body"))
    assert result["statusCode"] == 400
    assert " Expecting 'Value Unit'" in response["result"]

def test_lambda_sum_malformed_inputs(mocker):    
    result = call_calculator_sum({
        "input1": "1",
        "input2": "Meters"
    })
    response = json.loads(result.get("body"))
    assert result["statusCode"] == 400
    assert " Expecting 'Value Unit'" in response["result"]
