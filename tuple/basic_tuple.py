'''
튜플: 리스트와 유사하나 한번 선언되면 변경 불가 (문자열도 변경 불가)

1. 소괄호로 표현하며 적은 양의 메모리를 사용하므로 공간효율적
2. 리스트와 달리 서로 다른 성질의 데이터를 묶어야할 때 사용
ex) 최단 경로 알고리즘에서 (비용, 노드번호) 형태에 실수, 정수형태에 사용
3. 해싱의 키 값을 사용: 변경이 불가하므로 해싱의 키 값으로 지정해놓음
'''

a = (1,2,3,4,5)
print(a[4])

print(a[0:3])
