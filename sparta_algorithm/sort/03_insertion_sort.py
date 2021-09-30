'''
필요할 때만 삽입하여 정렬
정렬되지 않은 배열과 정렬할 배열을 따로 정의
정렬할 배열에 새 값을 넣으면 정렬된 상태를 유지하기위해
비교함
[4, 6, 2, 5]
4vs6 <- 2

'''

input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i-j-1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break


insertion_sort(input)
print(input) 
