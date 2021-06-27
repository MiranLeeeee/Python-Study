'''
while문 예제
1~100까지 짝수의 합 구하기
'''

i = 1
total = 0

while i <= 100:
  if i % 2 == 0:
    print(i)
    total += i
  i+=1

print(total)
