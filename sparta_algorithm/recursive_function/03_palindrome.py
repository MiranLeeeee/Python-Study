input = "abcba"


def is_palindrome_rec(string):
    # 가운데 글자는 하나이므로 True로 넘김
    if len(string) <= 1:
        return True
    
    if string[0] != string[-1]:
        return False

    # 문장의 맨 앞과 끝을 넘겨줌
    return is_palindrome_rec(string[1:-1])

def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n-1-i]:
            return False
    return True


print(is_palindrome(input))
print(is_palindrome_rec(input))
