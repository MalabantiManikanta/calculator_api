# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS middleware configuration
origins = [
    "http://localhost:8080",  # Allow this origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class CalculationRequest(BaseModel):
    operation: str
    number1: float 
    number2: float

@app.post("/calculate")
def calculate(request: CalculationRequest):
    operation = request.operation.lower()
    num1 = request.number1
    num2 = request.number2

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Use add, subtract, multiply, or divide.")

    return {"operation": operation, "number1": num1, "number2": num2, "result": result}
