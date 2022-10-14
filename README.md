# School Interface III

## Step 1: Adding A Student 

Let's make it so our user can add student information to our database. We'll need to do a few things here. First, we'll have to add a new case to our if statement. 

```Python
# runner.py
if mode == '1':
    school.list_students()
elif mode == '2':
    student_id = input('Enter student id:')
    student = school.find_student_by_id(student_id)
    print(str(student))
elif mode == '3':  
    school.add_student(student_data)
elif mode == '5':
    break  
```

Just like before we call a method that we have not defined yet. This method should take a dictionary containing all the data to make a new student object. From here, we need to do two things. First, we need to ask the user for the student's name, age, student_id number, and password. Next, we need to put those values into a dictionary and then pass that dictionary to our method. We can do this with multiple `input()` calls. 

```Python
# runner.py

elif mode == '3':
    student_data = {'role':'student'}
    student_data['name']      = input('Enter student name:\n')
    student_data['age']       = input('Enter student age: \n')
    student_data['school_id'] = input('Enter student school id: \n')
    student_data['password']  = input('Enter student password: \n')
  
    school.add_student(student_data)
elif mode == '5':
    break
```
Let's finish up the functionality for this feature by going into our school class and writing our `add_student()` method. This method will need to create a new instance of a student object and add it to the `self.students` variable. When you're done, run the program. Enter some test data when prompted. Next, choose the option to list all the students. You should see the test student you entered listed at the end of your `self.students` list.


## Step 2: Deleting Records  

The last feature we need to implement is the ability to delete a student record. Follow the same procedure as before. First, add a condition to the if statement. What information will you need from the user in order to delete a record? How will you get it and pass it to your method? Then, in `school.py` define a method `delete_student()`. Are you noticing duplicated code? Maybe you can refactor!
