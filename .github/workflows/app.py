students = []

def add_student(name, roll):
    students.append({"name": name, "roll": roll})

def list_students():
    for s in students:
        print(s["roll"], s["name"])

def delete_student(roll):
    global students
    students = [s for s in students if s["roll"] != roll]

if __name__ == "__main__":
    add_student("Harshika", 1)
    add_student("vanshika", 2)
    list_students()
    delete_student(2)
    print("After delete:")
    list_students()
