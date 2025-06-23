from dal import *
from exceptions import StudentNotFoundError, InvalidGradeError


def list_students():
    return get_all_students()


def get_student_by_id(student_id: int):
    student = get_student(student_id)
    if not student:
        raise StudentNotFoundError(f"Student {student_id} not found")
    return student


def add_student(first_name, last_name, email, grade):
    if not 0 <= grade <= 100:
        raise InvalidGradeError("Grade must be between 0 and 100")
    return insert_student(first_name, last_name, email, grade)


def update_student_info(student_id, first_name, last_name, email, grade):
    if not 0 <= grade <= 100:
        raise InvalidGradeError("Grade must be between 0 and 100")
    if not get_student(student_id):
        raise StudentNotFoundError(f"Student {student_id} not found")
    update_student(student_id, first_name, last_name, email, grade)


def delete_student_by_id(student_id):
    if not get_student(student_id):
        raise StudentNotFoundError(f"Student {student_id} not found")
    delete_student(student_id)
