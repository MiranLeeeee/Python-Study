'''
반복문 제어 2. break
: 반복문을 즉시 빠져나오기 위해 사용
'''
i = 1

# 10미만의 양수 출력
while True:
    if i == 10:
        break
    print(i, "10미만의 양수")    
    i+=1
