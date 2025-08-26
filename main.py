from fastapi import FastAPI, HTTPException
from model_val import emp
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
        if employee.id == emp_id:  
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")  

# 3. add a new employee
@app.post('/employee', response_model=emp)
def add_emp(new_emp: emp):
    for employee in emp_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee already exists")
    emp_db.append(new_emp)   # ✅ fixed indentation
    return new_emp

# 4. update an employee
@app.put('/update_employee/{emp_id}', response_model=emp)
def update_emp(emp_id: int, updated_emp: emp):
    for index, employee in enumerate(emp_db):
        if employee.id == emp_id:
            emp_db[index] = updated_emp
            return updated_emp   # ✅ moved inside match, not loop
    raise HTTPException(status_code=404, detail="Employee not found")

# 5. delete an employee
@app.delete('/delete_emp/{emp_id}')
def delete_emp(emp_id: int):
    for index, employee in enumerate(emp_db):
        if employee.id == emp_id:
            deleted_emp = emp_db.pop(index)
            return {"message": f"Employee {deleted_emp.id} deleted successfully"}  # ✅ response fixed
    raise HTTPException(status_code=404, detail="Employee not found")
