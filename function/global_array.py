# 배열은 global 키워드없이 함수 내에서 활용가능
# 하지만 함수 내에 같은 이름을 가진 배열 선언 시 우선적으로 함수 내 배열을 사용

array = [1, 2, 3, 4, 5]

def add():
  array.append(len(array)+1)
  print(array)

add() #[1, 2, 3, 4, 5, 6]
