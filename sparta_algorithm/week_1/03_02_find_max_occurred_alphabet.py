input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        # 문자가 알파벳이 아니면 다음으로 넘어감 -> 공백처리
        if not char.isalpha():
            continue

        # ord() -> 문자를 아스키코드로 변환
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    
    # 빈도수 가지고 있는 alphabet_occurrence_array배열에서 최대 빈도수와 인덱스를 검색
    max_occurrence = 0
    max_alphabet_index = 0

    for i in range(len(alphabet_occurrence_array)):
        if max_occurrence < alphabet_occurrence_array[i]:
            max_occurrence = alphabet_occurrence_array[i]
            max_alphabet_index = i

    return chr(max_alphabet_index+ord('a'))


result = find_max_occurred_alphabet(input)
print(result)
