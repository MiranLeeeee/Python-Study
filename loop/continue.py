'''
반복문 제어 1. continue
: 반복문 continue 뒤 남은 코드는 실행하지 않고 바로 다음 반복을 실행하기 위함
'''

# 1~10까지 수 중 홀수만 출력하기
for i in range(1, 11):
    # 짝수일 때는 출력하지 않고 다음 반복을 실행
    if i % 2 == 0:
        continue
    print(i)
