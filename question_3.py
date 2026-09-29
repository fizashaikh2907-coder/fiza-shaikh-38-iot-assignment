
 Lab 4 - Question 3
 
 Task:
 Create a list of student names:
 students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
 Ask the user to enter a student name.
 If the name exists, display:
 Student Found
 Otherwise:
 Student Not Found


def main():
    print("=" * 45)
    print("           STUDENT NAME SEARCH               ")
    print("=" * 45)

    # Given list of students
    students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
    print(f"Students List: {students}\n")

    # Ask the user to enter a student name
    search_name = input("Enter a student name: ").strip()

    # Search in the list (using case-insensitive comparison for best accuracy)
    found = False
    for student in students:
        if student.lower() == search_name.lower():
            found = True
            break

    # Display the result exactly as requested
    print("-" * 45)
    if found:
        print("Student Found")
    else:
        print("Student Not Found")
    print("-" * 45)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
