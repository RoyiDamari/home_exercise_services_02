from fastapi import FastAPI, HTTPException
import bl
from models import StudentRequest, StudentResponse
from exceptions import StudentNotFoundError, InvalidGradeError
import dal

app = FastAPI()

dal.init_db()


@app.get("/students/", response_model=list[StudentResponse])
def list_students():
    students = bl.list_students()
    return [StudentResponse(id=s[0], first_name=s[1], last_name=s[2], email=s[3], grade=s[4]) for s in students]


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    try:
        s = bl.get_student_by_id(student_id)
        return StudentResponse(id=s[0], first_name=s[1], last_name=s[2], email=s[3], grade=s[4])
    except StudentNotFoundError:
        raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students/", response_model=StudentResponse)
def add_student(student: StudentRequest):
    try:
        student_id = bl.add_student(student.first_name, student.last_name, student.email, student.grade)
        return StudentResponse(id=student_id, **student.dict())
    except InvalidGradeError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentRequest):
    try:
        bl.update_student_info(student_id, student.first_name, student.last_name, student.email, student.grade)
        return StudentResponse(id=student_id, **student.dict())
    except StudentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except InvalidGradeError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    try:
        bl.delete_student_by_id(student_id)
        return {"message": "Student deleted successfully"}
    except StudentNotFoundError:
        raise HTTPException(status_code=404, detail="Student not found")
