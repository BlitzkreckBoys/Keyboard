class SMS:
   
    
    def __init__(self, name, DEP, session,sem,DoB,Roll_num):
        self.name = name
        self.DEP = DEP
        self.session = session
        self.sem = sem
        self.DoB = DoB
        self.Roll_num = Roll_num
    def display_student_info(self):
        print("Student Name:", self.name)
        print("Department:", self.DEP)
        print("Session:", self.session)
        print("Semester:", self.sem)
        print("Date of Birth:", self.DoB)
        print("Roll Number:", self.Roll_num)
        print()