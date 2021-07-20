input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:
        for compare_num in array:
            # 자신보다 큰 수가 생긴 것이니 다음 숫자로 넘어감
            if num < compare_num:
                break
        # 자신이 제일 큰 것임
        # for-else else문은 for문의 break 등에 걸리지않고 완전히 실행되었을 경우
        else:
            return num

    # return max(array)


result = find_max_num(input)
print(result)
