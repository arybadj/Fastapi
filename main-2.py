from fastapi import FastAPI, HTTPException
from models import emp
from typing import List

emp_db: list[emp] = []

app = FastAPI()

# 1. read all employees
@app.get('/employee', response_model=List[emp])
def get_emp():
    return emp_db

# 2. read specific employee
@app.get('/employee/{emp_id}', response_model=emp)
def get_spec_emp(emp_id: int):
    for employee in emp_db:
        if employee.id == emp_id:  # ✅ fixed: use employee.id instead of emp.id
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")  # ✅ added error handling

