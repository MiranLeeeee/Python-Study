'''
입력
1. input(): 한 줄의 문자열을 입력받는함수
2. map(): 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
'''

# 데이터 하나만 입력할 경우
n = int(input())

# 개수가 정해진 경우
a, b, c = map(int, input().split())
print(a, b, c)

# 정해지지 않는 개수만큼 입력한 경우
# 입력한 데이터를 공백으로 나누어 int형으로 지정하여 리스트에 저장
a = list(map(int, input().split()))
print(a)
