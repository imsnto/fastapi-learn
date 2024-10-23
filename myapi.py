from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
	1: {
		"name": "Solaiman Hossain",
		"age": 25,
		"year": "class 12"
	}
}

class Student(BaseModel):
    name : str
    age  : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age  : Optional[int] = None
    year : Optional[str] = None
    
@app.get("/")
def index():
	return students
	
# path parameter
@app.get("/get-student/{id}")
def get_student(id: int = Path(..., description="The id of the student you want to view", gt=0, lt=20)):
	student = students.get(id)
	if student is None:
		# Return an error response if the student is not found
		raise HTTPException(status_code=404, detail="Student not found")
	return student

# query parameter
@app.get("/get-by-name/{id}")
def get_student(*, id : int, name : Optional[str] = None):
    if id in students:
        return students[id]
    
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "Not Found"}

@app.post("/create-student/{id}")
def create_student(id:int, student:Student):
    if id in students:
        return {"Error": "Student Exists"}
    students[id] = student
    return students[id]

@app.put("/update-student/{id}")
def update_student(id:int, student:UpdateStudent):
    if id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[id]['name'] = student.name
    if student.age != None:
        students[id]['age'] = student.age
    if student.year != None:
        students[id]['year'] = student.year
    return students[id]

@app.delete("/delete-student/{id}")
def delete_student(id:int):
    if id not in students:
        return {"Error": "Student does not exist"}
    
    del students[id]
    return {"Message": "Student deleted successfully"}
