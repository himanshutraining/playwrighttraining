from demo3_package.student import Student

Student.school_name="SchoolName123"
Student.school_address="Address123"

print(Student.school_name, Student.school_address)

stu1=Student()

stu1.name="Name1"
stu1.rollNo=1001
stu1.mailId="abc@xyz.com"
stu1.percentage="90%"

print(stu1.name, stu1.rollNo, stu1.mailId,stu1.percentage)

stu1.display_student_detail()