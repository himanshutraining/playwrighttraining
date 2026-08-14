class Student :

    school_name=None
    school_address=None

    def __init__(self):
            #Non static variable
            self.rollNo=None
            self.name=None
            self.mailId=None
            self.percentage=None

    @staticmethod
    def display_school_name():
            return Student.school_name

    
    @staticmethod
    def display_school_address():
            return Student.school_address
            
    def display_student_detail(self):
            print("Roll No", self.rollNo)
            print("Name", self.name)
            print("Mailid", self.mailId)
            print("Percentage", self.percentage)
            print("***********************************************************************")