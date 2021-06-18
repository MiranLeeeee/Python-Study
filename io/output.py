'''
출력
1. print() 함수를 이용하고 출력 후 줄바꿈 수행
2. end 속성을 이용해 줄바꿈 대신 다른 속성값 등으로 수행가능
'''

print("Hello") # 줄바꿈 포함
print("World")

print("Hello", "World") #,는 구분자이면서 공백으로 구분
print("Hello", end = " ") # end속성 값 이용
print("World", end = " ")

# 정수형 등은 +로 문자열과 결합하기 위해서 형변환이 필요
a = 29
print("좋아하는 숫자는 " + str(a)+"입니다.")
