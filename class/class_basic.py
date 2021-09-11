class Student:
    # 생성자
    def __init__(self, name):
        self.name = name
    # 메소드
    def sayHello(self):
        print("안녕 내 이름은 "+self.name)

student_1 = Student("이미란")
print(student_1.name)

student_2 = Student("김미란")
print(student_2.name)
student_2.sayHello()
