from itertools import product

# 중복 순열
arr = ['가','나','다']

# 같은 원소가 들어있어도 허용
# 2개씩 뽑아 중복허용한 모든 순열 출력
print(list(product(arr, repeat=2)))
