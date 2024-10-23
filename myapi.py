from fastapi import FastAPI, Path, HTTPException

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
