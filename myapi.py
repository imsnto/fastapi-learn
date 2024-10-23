from fastapi import FastAPI, Path, HTTPException
from typing import Optional

app = FastAPI()

students = {
	1: {
		"name": "Solaiman Hossain",
		"age": 25,
		"class": "B.Sc"
	},
	2: {
		"name": "Hasan Mahmud",
		"age": 24,
		"class": "B.Sc"
	}
}

@app.get("/")
def index():
	return {"name": "Solaiman"}
	
# path parameter
@app.get("/get-student/{id}")
def get_student(id: int = Path(..., description="The id of the student you want to view", gt=0, lt=3)):
	student = students.get(id)
	if student is None:
		# Return an error response if the student is not found
		raise HTTPException(status_code=404, detail="Student not found")
	return student

# query parameter
@app.get("/get-by-name")
def get_student(name : Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "Not Found"}
