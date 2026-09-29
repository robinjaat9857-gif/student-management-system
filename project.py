students  = []
while True:
    print("\n=====  STUDENT MANAGEMENT SYSTEM  ====")
    print("1.Add Student")
    print("2. Show Students")
    print("3. Search Students")
    print("4. Delete Student")
    print("5. Exit")

    choice =  input("Enter your choice: ")
    
    # add student 
    if choice == "1":
        name = input("Enter the student name: ")
        roll_no = input("Enter the roll number: ")
        marks  = float(input("Enter the marks: "))
        student  = {
            "name" : name,
            "roll_no" : roll_no,
            "marks" : marks
        }
        
        students.append(student)
        print("Student added successfully!")
    
    # show students
    elif choice == "2":
        if  len(students) == 0:
            print("No students found.")
        else :
            print("\n----- Student List -----")
            for student  in students:
                print("Name:",student["name"])
                print("Roll_NO:",student["roll_no"])
                print("Marks:",student["marks"])
                print("---------------")
    #Search Student
    elif choice == "3":
        roll_no  = input("Enter roll number to search: ")
        found = False
        for  student in students: 
            if student["roll_no"] == roll_no:
                print("\nStudent  Found!")
                print("Name:", student["name"])
                print("Roll_No:", student["roll_no"])
                print("Marks:", student["marks"])
                found = True
        if not  found:
            print("Student not found.")
    # Delete Student 
    elif choice == "4":
        roll_no = input("Enter  roll number to delete: ")
        for student in students:
            if student["roll_no"] == roll_no:
                students.remove (student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")
    # Exit 
    elif choice  ==  "5":
        print("Thank you for using Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")