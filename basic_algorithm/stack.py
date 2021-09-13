'''
스택: 선입후출의 자료구조 -> 입출구가 동일한 형태 (Last In First Out)
'''

# 파이썬 스택: 리스트로 구현

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

stack.pop() #마지막 원소 꺼내기
print(stack) 
print(stack[::-1]) # 위(top)에서 부터 출력
