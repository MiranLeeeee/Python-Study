'''
점근 표기법: 프로그램의 성능을 수학적으로 표기한 것
'''
input = [3, 5, 6, 1, 2, 4]


# 내가 한 방식과 일치
# 입력값에 따라 프로그램 성능이 달라짐
# 빅오표기법은 최악의 상황, 빅 오메가 표기법은 최적의 상황을 기준
def is_number_exist(number, array):
    for i in array: # array길이만큼 실행
        if i == number: # 비교 연산 1번 실행
            return True # N*1 = N만큼 실행
    return False

result = is_number_exist(60, input)
print(result)
