'''
1. 재귀함수 예: 팩토리얼
n! = 1 * 2 * 3 * ... * (n-1) * n
0!와 1!의 값은 1
'''

def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n-1)

print(factorial(7))
