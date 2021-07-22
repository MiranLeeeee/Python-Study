'''
[내가 한 방식]
input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    arr = [0] * 26
    for i in input:
        if i.isalpha():
            arr[97-ord(i)] += 1

    max_num = max(arr)
    return chr(arr.index(max_num)+97)


result = find_max_occurred_alphabet(input)
print(result)

'''

input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    # 알파벳 리스트와 입력한 문자열 각각 원소를 비교하여 빈도수 계산
    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if alphabet == char:
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)
