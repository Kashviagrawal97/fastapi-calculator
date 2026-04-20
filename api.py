from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from enum import Enum
from calculator import main, obj

app = FastAPI()

class Operation(str, Enum):
    add       = "add"
    subtract  = "subtract"
    multiply  = "multiply"
    divide    = "divide"
    power     = "power"
    log       = "log"
    factorial = "factorial"


class NumbersRequest(BaseModel):
    a: float
    b: float


@app.post("/calculate")
async def calculate_api(
    operation: Operation = Query(..., description="Select operation"),
    request: NumbersRequest = None
):

    if request is None:
        return {"error": "Missing fields"}

    try:
        result = main(request.a, request.b, operation.value, obj)
        return {"result": result}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))