def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        # 문자가 알파벳이 아니면 다음으로 넘어감 -> 공백처리
        if not char.isalpha():
            continue

        # ord() -> 문자를 아스키코드로 변환
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1


    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
