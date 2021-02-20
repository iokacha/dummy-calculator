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