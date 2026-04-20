from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from calculator import main, obj

app = FastAPI()

# API_KEY = "mysecretkey"

class Operation(str, Enum):
    add       = "add"
    subtract  = "subtract"
    multiply  = "multiply"
    divide    = "divide"
    power     = "power"
    log       = "log"
    factorial = "factorial"

class CalculatorRequest(BaseModel):
    a: float
    b: float
    operation: Operation

@app.post("/calculate")
async def calculate_api(request: CalculatorRequest):

    if request.a is None or request.b is None or request.operation is None:
        return {"error": "Missing fields"}

    try:
        result = main(request.a, request.b, request.operation, obj)
        return {"result": result}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))