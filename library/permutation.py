'''
순열과 조합
1. 순열: n개의 요소 중 r개로 일렬로 나열하는 경우 (순서 고려)
nPr = n*(n-1)*(n-2)*...(n-r+1)
2. 조합: n개의 요소 중 순서 고려 없이 r개 선택하는 경우
nCr = nPr/r!
'''

# 순열
from itertools import permutations

arr = ['가','나','다']

print(list(permutations(arr, 3)))
