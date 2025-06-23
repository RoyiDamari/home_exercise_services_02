import requests

BASE_URL = "http://127.0.0.1:8000"


def view_all_students():
    resp = requests.get(f"{BASE_URL}/students/")
    for student in resp.json():
        print(
            f"ID: {student['id']} | {student['first_name']} {student['last_name']} | {student['email']} | Grade: {student['grade']}")


def search_student_by_id():
    student_id = input("Enter student ID: ")
    resp = requests.get(f"{BASE_URL}/students/{student_id}")
    if resp.status_code == 200:
        student = resp.json()
        print(
            f"{student['id']} | {student['first_name']} {student['last_name']} | {student['email']} | Grade: {student['grade']}")
    else:
        print(resp.json()["detail"])


def add_new_student():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    grade = float(input("Grade: "))
    resp = requests.post(f"{BASE_URL}/students/",
                         json={"first_name": first_name, "last_name": last_name, "email": email, "grade": grade})
    print(resp.json() if resp.status_code == 200 else resp.json()["detail"])


def update_student():
    student_id = input("ID to update: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    grade = float(input("Grade: "))
    resp = requests.put(f"{BASE_URL}/students/{student_id}",
                        json={"first_name": first_name, "last_name": last_name, "email": email, "grade": grade})
    print(resp.json() if resp.status_code == 200 else resp.json()["detail"])


def delete_student():
    student_id = input("ID to delete: ")
    resp = requests.delete(f"{BASE_URL}/students/{student_id}")
    print(resp.json() if resp.status_code == 200 else resp.json()["detail"])


def main():
    while True:
        print("\nWelcome to Student Grades Manager")
        print(
            "1. View all students\n2. Search by ID\n3. Add new student\n4. Update student\n5. Delete student\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_all_students()
        elif choice == "2":
            search_student_by_id()
        elif choice == "3":
            add_new_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
