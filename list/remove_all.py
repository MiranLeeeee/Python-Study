# remove함수는 일치하는 원소 하나만 제거하므로
# 특정 원소를 다 제거하기 위해서는 조건문을 사용 (comprehension)

a = [1,2,3,4,5,5,5]
remove_set = {3,5} # 제거하고자 하는 원소 집합

# result에 원소 i를 삽입할 것 -> a 순서대로 원소 i들이 들어감
# -> 원소 i는 remove_set에 일치하는 원소가 아닐 것
result = [i for i in a if i not in remove_set]
print(result)
