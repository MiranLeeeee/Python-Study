input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        # 문자가 알파벳이 아니면 다음으로 넘어감 -> 공백처리
        if not char.isalpha():
            continue

        # ord() -> 문자를 아스키코드로 변환
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index+ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char


result = find_not_repeating_character(input)
print(result)
