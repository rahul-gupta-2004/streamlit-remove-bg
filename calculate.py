from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Simple Calculator")

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}

@app.get("/")
def root():
    return {"message": "Try endpoints: /add?a=5&b=3, /subtract, /multiply, /divide"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
