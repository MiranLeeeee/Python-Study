# 여러 개의 리스트 등에 같은 규칙을 적용 시 사용

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [10,9,8,7,6,5,4,3,2,1]

# map: 각각의 원소를 순서대로 가져와 적용
list3 = map(lambda a, b: a+b, list1, list2)

print(list(list3))
