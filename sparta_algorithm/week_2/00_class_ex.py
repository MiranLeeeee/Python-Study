class Person:
    # constructor 생성자 함수
    # __init__: 객체가 생성되었을 때 실행됨
    def __init__(self, param_name):
        # print("I am created!", self)
        self.name = param_name

    # 클래스 내 메소드 선언
    def talk(self):
        print("안녕! 나는", self.name)

person_1 = Person("루피")
print(person_1.name)
person_1.talk()

person_2 = Person("뽀로로")
print(person_2.name)
