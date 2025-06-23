from pydantic import BaseModel, EmailStr, Field


class StudentRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    grade: float = Field(..., ge=0, le=100)


class StudentResponse(StudentRequest):
    id: int
