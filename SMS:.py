class SMS:
   
    
    def __init__(self, name, DEP, session,sem,DoB,Roll_num):
        self.name = name
        self.DP = DEP
        self.session = session
        self.sem = sem
        self.DoB = DoB
        self.Roll_num = Roll_num
    def display_student_info(self):
        print("Student Name:", self.name)
        print("Department:", self.DP)
        print("Session:", self.session)
        print("Semester:", self.sem)
        print("Date of Birth:", self.DoB)
        print("Roll Number:", self.Roll_num)
        print()

class StudentManagementSystem: 

    def __init__(self):
        self.students = []
        

    def Create(self):
        print("Enter student details:")
            
        while True:
            name = input("Enter student's name: ")
            DEP = input("Enter student's department: ")

            while True:
                try:
                    session = int(input("Enter student's session: "))
                    sem = int(input("Enter student's semester: "))
                    DoB = input("Enter student's date of birth (YYYY-MM-DD): ")
                    Roll_num = int(input("Enter student's roll number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter valid data.")

            self.students.append(SMS(name, DEP, session, sem, DoB, Roll_num))
                
            break        
        print("Student added successfully!")
    
    def Retreive(self):
        
        roll_num = int(input("enter roll_num:"))
        for student in  self.students:    
            if student.Roll_num == roll_num:
                print()
                print("Student Details:")
                student.display_student_info()
            else:
                print("Student not found.")
                break
    


    def Update(self):
            roll_num = int(input("Enter roll number to update: "))
            for student in self.students:
                if student.Roll_num == roll_num:
                    print("Enter updated student details:")
                    student.name = input("Enter updated student's name: ")
                    student.DEP = input("Enter updated student's department: ")

                    while True:
                        try:
                            student.session = int(input("Enter student's session: "))
                            student.sem = int(input("Enter student's semester: "))
                            student.DoB = input("Enter student's date of birth (YYYY-MM-DD): ")
                            student.Roll_num = int(input("Enter student's roll number: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter valid data.")

                    print("Student updated successfully!")
                    return
            print("Student not found.")
    def Delete(self):
        roll_num = int(input("enter roll_num:"))
        for student in self.students:
            if student.Roll_num == roll_num:
                self.students.remove(student)
                print("Student Deleted Successfully!")
            else:
                print("Student not found.")
                break
    def choose_operation(self):
        while True:
            print("\nChoose an operation:")
            print("1. Create a new student")
            print("2. Retrieve student details")
            print("3. Update student details")
            print("4. Delete a student")
            print("5. Exit")

            try:
                Select = int(input("Enter your Select: "))
                
            except ValueError:
                print("Invalid input. Please enter a valid number.")

            if Select == 1:
                sms.Create()
            elif Select == 2:
                sms.Retreive()
            elif Select == 3:
                sms.Update()
            elif Select == 4:
                sms.Delete()
            elif Select == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
sms = StudentManagementSystem()
sms.choose_operation()
#sms.Create()
#sms.Retreive()
#sms.Update()
#sms.Delete()
#self, name, DP, session, sem, DOB, Roll_num