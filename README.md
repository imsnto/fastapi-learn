# FastAPI Student Management API

This project implements a RESTful API using FastAPI and Pydantic for managing student data. It supports CRUD operations (Create, Read, Update, Delete) for student records, with data validation using Pydantic models.

## Features
- **CRUD Operations**:
  - **GET**: Retrieve all students, a specific student by ID, or search by name.
  - **POST**: Create a new student record.
  - **PUT**: Update an existing student's details.
  - **DELETE**: Remove a student record.
- **Pydantic Validation**:
  - Uses `Student` model for creating students.
  - Uses `UpdateStudent` model for partial updates with optional fields.
- **Error Handling**: Returns meaningful HTTP errors (e.g., 404 for non-existent students).
- **Path and Query Parameters**: Supports ID-based lookups and name-based searches.
- **In-Memory Storage**: Stores student data in a dictionary (for demonstration purposes).

## Prerequisites
- Python 3.8+
- Required Python packages: `fastapi`, `pydantic`, `uvicorn`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/imsnto/fastapi-learn.git
   cd fastapi-learn
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi pydantic uvicorn
   ```

## Usage
1. **Run the FastAPI Application**:
   ```bash
   uvicorn myapi:app --reload
   ```
   - The server will start at `http://localhost:8000`.
   - The `--reload` flag enables auto-reload for development.

2. **Access the API**:
   - **Interactive Docs**: Open `http://localhost:8000/docs` in a browser to access the Swagger UI for testing endpoints.
   - **Example Endpoints**:
     - **Get all students**: `GET /`
       ```bash
       curl http://localhost:8000/
       ```
       Response: `{"1": {"name": "Solaiman Hossain", "age": 25, "year": "class 12"}}`
     - **Get student by ID**: `GET /get-student/1`
       ```bash
       curl http://localhost:8000/get-student/1
       ```
       Response: `{"name": "Solaiman Hossain", "age": 25, "year": "class 12"}`
     - **Create a student**: `POST /create-student/2`
       ```bash
       curl -X POST http://localhost:8000/create-student/2 -H "Content-Type: application/json" -d '{"name": "Alice Smith", "age": 20, "year": "class 11"}'
       ```
       Response: `{"name": "Alice Smith", "age": 20, "year": "class 11"}`
     - **Update a student**: `PUT /update-student/1`
       ```bash
       curl -X PUT http://localhost:8000/update-student/1 -H "Content-Type: application/json" -d '{"name": "Solaiman H."}'
       ```
       Response: `{"name": "Solaiman H.", "age": 25, "year": "class 12"}`
     - **Delete a student**: `DELETE /delete-student/1`
       ```bash
       curl -X DELETE http://localhost:8000/delete-student/1
       ```
       Response: `{"Message": "Student deleted successfully"}`

## Project Structure
```
├── .gitignore             # Git ignore file
├── main.py                # FastAPI application with student API
└── README.md              # Project documentation
```

## Notes
- The API uses an in-memory dictionary (`students`) for data storage, which resets when the server restarts. For production, consider using a database (e.g., SQLite, PostgreSQL).
- The `.gitignore` file should include `venv/`, `__pycache__/`, and other irrelevant files.
- Input validation is handled by Pydantic, ensuring type safety and constraints (e.g., positive ID, valid strings).

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## License
This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
