'''
일단 맨 뒤 요소는 제일 큰 숫자가 가므로
다음 정렬때는 맨 뒤를 빼고 다시 정렬하면 됨
1. 파이썬 교환은 쉬움
a, b = b, a
'''

input = [5, 7, 3, 8, 1]


def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1): #마지막 제외
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


bubble_sort(input)
print(input)
