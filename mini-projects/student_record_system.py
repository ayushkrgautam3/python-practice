students = {}

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        students[roll] = [name, marks]
        print("Student added")

    elif choice == 2:
        for roll in students:
            print("Roll:", roll, "Name:", students[roll][0], "Marks:", students[roll][1])

    elif choice == 3:
        roll = input("Enter roll number to search: ")
        if roll in students:
            print("Name:", students[roll][0], "Marks:", students[roll][1])
        else:
            print("Student not found")

    elif choice == 4:
        roll = input("Enter roll number to delete: ")
        if roll in students:
            del students[roll]
            print("Deleted successfully")
        else:
            print("Student not found")

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")
