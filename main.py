from database import create_database

from operations import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

create_database()



while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. view student")
    print("3. search student")
    print("4.update")
    print("5.delete")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")