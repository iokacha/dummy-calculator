# Unit test : 
  - pip3 install -y requirements.txt
  - PYTHONPATH=$PWD pytest tests/unit

# Function Integration tests : 
  - PYTHONPATH=$PWD pytest tests/integration

# Build and Deploy using AWS SAM CLI
  - Local Build & Test : 
    * sam build --use-container
    * sam local start-api
    * curl --header "Content-Type: application/json" --request POST http://localhost:3000/sum/

  - Deploy 
    * sam deploy --guided 
# Test Live and feedback  : 
  - curl -H "Content-Type: application/json" \
    --request POST \
    --data @payload
    --request POST https://0sglngibng.execute-api.us-east-1.amazonaws.com/Prod/sum/

```
    '{"input1":"1 Meters",      "input2":"2 Meters"}'                 => HTTP 200       {"result": "3 Meters"}
    '{"input1":"1 Decimeters",  "input2":"2 Meters"}'                 => HTTP 200       {"result": "2.1 Meters"}
    '{"input1":"1 Kilometer",   "input2":"2 Meters"}'                 => HTTP 200       {"result": "1002 Meters"}
    '{"input1":"1 OK",   "input2":"2 Meters", "units" : "Meters"}'    => HTTP 400       {"result": "Exception at OK : Invalid Metric Unit Exception"}
    '{}'                                                              => HTTP 400       {"result": "Exception at  : Invalid Format Exception, Expecting 'Value Unit'"}
```