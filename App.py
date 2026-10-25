
from datetime import date


def add_student(students, student_id, name):
    if student_id in students:
        return False
    students[student_id] = name
    return True


def mark_attendance(records, student_id, status, attendance_date=None):
    if status not in ("Present", "Absent"):
        return False

    attendance_date = attendance_date or str(date.today())
    records[(student_id, attendance_date)] = status
    return True


def main():
    students = {}
    records = {}

    while True:
        print("\nSTUDENT ATTENDANCE SYSTEM")
        print("1. Add student")
        print("2. View students")
        print("3. Mark attendance")
        print("4. View attendance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")

            if add_student(students, student_id, name):
                print("Student added successfully!")
            else:
                print("Student ID already exists.")

        elif choice == "2":
            for sid, name in students.items():
                print(sid, "-", name)
            if not students:
                print("No students added yet.")

        elif choice == "3":
            student_id = input("Enter student ID: ")
            if student_id not in students:
                print("Student not found.")
                continue

            status = input("Present or Absent: ").strip().title()
            if mark_attendance(records, student_id, status):
                print("Attendance marked successfully!")
            else:
                print("Enter Present or Absent.")

        elif choice == "4":
            for (sid, day), status in records.items():
                print(students[sid], "|", day, "|", status)
            if not records:
                print("No attendance records yet.")

        elif choice == "5":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
  
