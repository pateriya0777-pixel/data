from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import django

# --- STEP 1: CONFIGURE DJANGO FIRST ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_project.settings')
django.setup()

# --- STEP 2: NOW IMPORT MODELS ---
# This must happen AFTER django.setup()

from students.models import Student 

# --- STEP 3: REST OF THE APP ---
app = FastAPI()

# --- SCHEMA (The Shape of Data) ---
class StudentSchema(BaseModel):
    name: str
    age: int
    grade: str

# --- API ENDPOINTS ---

# 1. LIST & SEARCH (GET)
# Usage: /students (Get all) OR /students?grade=10 (Get only grade 10)
@app.get("/students")
def get_students(grade: str = None):
    # If ?grade=X is passed in the URL, filter by it
    if grade:
        students = Student.objects.filter(grade=grade)
    else:
        students = Student.objects.all()
    
    # .values() converts Django objects to a simple dictionary list
    return list(students.values())

# 2. CREATE (POST)
@app.post("/students")
def create_student(data: StudentSchema):
    student = Student.objects.create(
        name=data.name,
        age=data.age,
        grade=data.grade
    )
    return {"message": "Created", "id": student.id}

# 3. GET ONE (GET)
# Usage: /students/5
@app.get("/students/{student_id}")
def get_single_student(student_id: int):
    try:
        # Try to find the student in Django DB
        student = Student.objects.get(id=student_id)
        return {
            "id": student.id, 
            "name": student.name, 
            "grade": student.grade
        }
    except Student.DoesNotExist:
        # If not found, throw a 404 error
        raise HTTPException(status_code=404, detail="Student not found")

# 4. UPDATE (PUT)
# Usage: /students/5 (Needs JSON body with new data)
@app.put("/students/{student_id}")
def update_student(student_id: int, data: StudentSchema):
    try:
        student = Student.objects.get(id=student_id)
        
        # Update the fields
        student.name = data.name
        student.age = data.age
        student.grade = data.grade
        student.save() # Save changes to DB
        
        return {"message": "Updated successfully"}
    except Student.DoesNotExist:
        raise HTTPException(status_code=404, detail="Student not found")

# 5. DELETE (DELETE)
# Usage: /students/5
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    try:
        student = Student.objects.get(id=student_id)
        student.delete() # Delete from DB
        return {"message": "Deleted successfully"}
    except Student.DoesNotExist:
        raise HTTPException(status_code=404, detail="Student not found")