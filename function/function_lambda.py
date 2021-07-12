# 내장 함수 람다 함수 응용 

arr = [('Lee', 160),('Park', 148), ('Bae', 187)]

def set_key(x):
  return x[1]

print(sorted(arr, key = set_key)) # 오름차순 정렬하고 key는 set_key함수를 통해 지정할 것임, 각 원소의 첫번째 index 값
print(sorted(arr, key=lambda x:x[1])) # 위와 동일하지만 lambda로 한 줄로 표현
