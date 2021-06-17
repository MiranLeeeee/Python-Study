'''
sys.stdin.readline()
: 특히 입력받아야하는 데이터가 많아 빠르게 입력받아야하는 경우 사용하는 메서드
1. 입력 시 줄바꿈 (Enter)이 같이 입력되므로 rstrip()으로 처리할 것
2. 이진탐색, 정렬, 그래프 구현 등에 활용
'''
import sys

data = sys.stdin.readline().rstrip()
print(data)
