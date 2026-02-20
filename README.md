# FastAPI Calculator Demo

A simple RESTful API built with FastAPI that provides basic calculator operations and product management functionality.

## Features

- **Calculator Operations**: Addition, subtraction, multiplication, and division
- **Product Management**: CRUD operations for product data stored in JSON file
- **RESTful API**: Clean and intuitive API endpoints
- **Interactive Documentation**: Auto-generated Swagger UI

## API Endpoints

### Calculator Endpoints
- `GET /add?a=5&b=3` - Add two numbers
- `GET /subtract?a=10&b=4` - Subtract two numbers  
- `GET /multiply?a=6&b=7` - Multiply two numbers
- `GET /divide?a=20&b=5` - Divide two numbers

### Product Management Endpoints
- `GET /items` - Get all products
- `GET /items/{id}` - Get a specific product by ID
- `POST /items` - Add a new product
- `PUT /items/{id}` - Update an existing product
- `DELETE /items/{id}` - Delete a product

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rahul-gupta-2004/fastapi-demo
cd fastapi-demo
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

3. Run the Server:
```bash
uvicorn calculate:app --reload
```
The API will be available at http://localhost:8000

## Installation

Once the server is running, you can access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

├── calculate.py          # Calculator API endpoints

├── json_handle.py        # Product CRUD operations

├── hello.py              # Simple hello world endpoint

├── test_calculate_api.py # Test script for calculator API

├── data.json            # Product data storage

├── requirements.txt     # Project dependencies

└── README.md            # This file

## Dependencies

- FastAPI
- Uvicorn
- Requests (for testing)

## Live Demo
The API is deployed and available at:

https://fastapi-demo-3wek.onrender.com
