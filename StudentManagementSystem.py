# List to store students
students = []

# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    students.append(name)  # Just store the name for simplicity
    print(f"Student {name} added!")

# Function to display all students
def display_students():
    if not students:
        print("No students added yet.")
    else:
        print("\n--- List of Students ---")
        for student in students:
            print(student)
        print("-------------------------")

# Main function
def main():
    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
