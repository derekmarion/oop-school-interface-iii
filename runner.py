from classes.school import School



def start_school_interactive():
    school = School("Ridgemont High")
    running = True
    
    while running:
        option = input(
            "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n\n"
        )

        match option:
            case "1":
                school.get_students
            case "2":
                school_id = input("Enter student id:")
                student = school.get_student_by_id(school_id)
                print(student)
            case "3":
                student_data = {'role':'student'}
                student_data['name']      = input('Enter student name:')
                student_data['age']       = input('Enter student age: ')
                student_data['school_id'] = input('Enter student school id:')
                student_data['password']  = input('Enter student password:')
                
                school.add_student(student_data)
            case "5":
                running = False

start_school_interactive()