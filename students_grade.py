student_grades = {}

while True:
    print("\n Student Grades")
    print("1. Add New Student")
    print("2. Update Student Grade")
    print("3. Print all Students Grades")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == '1':
        name = input("Enter student name:")
        grade = input("Enter student grade:")
        student_grades[name] = grade
        print(f"{name} added with grade {grade}")

    elif choice == '2':
        name = input("Enter student name to update:")
        if name in student_grades:
            grade = input("Enter new grade:")
            student_grades[name] = grade
            print(f"Grade for {name} updated to {grade}")
        else:
            print("Student not found.")

    elif choice == '3':
        if student_grades:
            print("\n Student Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")
        else:
            print("No student grades available.")
    
    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
            