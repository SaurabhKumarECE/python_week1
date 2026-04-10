
# Mini Project: Student Record Management System


import json  # for saving data in file

# Dictionary to store student data
students = {}

# 1. Add Student
def add_student():
    name = input("Enter student name: ")
    
    try:
        marks = float(input("Enter marks: "))
        students[name] = marks
        print(" Student added successfully.")
    except ValueError:
        print(" Invalid marks!")



# 2. Display Records
def display_students():
    if not students:
        print(" No student records found.")
        return

    print("\n--- Student Records ---")
    for name, marks in students.items():
        print(f"Name: {name} | Marks: {marks}")



# 3. Calculate Average Marks
def calculate_average():
    if not students:
        print(" No data available.")
        return

    avg = sum(students.values()) / len(students)
    print(f" Average Marks: {avg:.2f}")



# 4. Save to File
def save_to_file(filename="students.json"):
    try:
        with open(filename, "w") as f:
            json.dump(students, f)
        print(" Data saved to file.")
    except Exception as e:
        print(" Error saving file:", e)


# 5. Load from File
def load_from_file(filename="students.json"):
    global students
    try:
        with open(filename, "r") as f:
            students = json.load(f)
        print(" Data loaded successfully.")
    except FileNotFoundError:
        print(" No previous data file found.")
    except Exception as e:
        print(" Error loading file:", e)



# Menu System
def menu():
    while True:
        print("\n====== Student Record System ======")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()

        elif choice == '2':
            display_students()

        elif choice == '3':
            calculate_average()

        elif choice == '4':
            save_to_file()

        elif choice == '5':
            load_from_file()

        elif choice == '6':
            print(" Exiting program...")
            break

        else:
            print(" Invalid choice! Try again.")



# Run Program
if __name__ == "__main__":
    load_from_file()  # load existing data (if any)
    menu()