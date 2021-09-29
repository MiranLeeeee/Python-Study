# 가장 최소값을 찾아서 맨 앞에 요소와 바꿔치기
'''
가장 최소값이 맨 앞요소를 제외하고 다시 최소값을 찾는 방식
'''
input = [5, 7, 4, 8, 3]


def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(len(array)-i):
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index] =array[min_index], array[i]
    


selection_sort(input)
print(input)
