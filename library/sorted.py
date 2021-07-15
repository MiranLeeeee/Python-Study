# 내장된 정렬 함수

print(sorted([1,4,3,2]))# 오름차순: [1,2,3,4]
print(sorted([1,4,3,2],reverse=True))# 내림차순: [4,3,2,1]

# key를 사용하여 원하는 key값으로 정렬 가능
arr = [('Kim', 170),('Park', 184), ('Lee',160)]
# 키가 큰 순서대로 출력 
print(sorted(arr, key=lambda info:info[1], reverse=True))
