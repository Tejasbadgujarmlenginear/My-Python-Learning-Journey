import json

FILE = "students.json"

# Load existing students
def load_students():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save students
def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

# Add student
def add_student(students):
    try:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        student = {"roll": roll, "name": name, "age": age, "course": course}
        students.append(student)
        save_students(students)
        print("✅ Student added successfully!")
    except ValueError:
        print("❌ Invalid input, please enter correct values.")

# View all students
def view_students(students):
    if not students:
        print("No records found.")
    else:
        for s in students:
            print(f"Roll: {s['roll']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")

# Search student
def search_student(students):
    roll = int(input("Enter Roll No to search: "))
    for s in students:
        if s['roll'] == roll:
            print("🎯 Found:", s)
            return
    print("❌ Student not found.")

# Delete student
def delete_student(students):
    roll = int(input("Enter Roll No to delete: "))
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            save_students(students)
            print("🗑️ Student deleted successfully!")
            return
    print("❌ Student not found.")

# Main menu
def main():
    students = load_students()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()