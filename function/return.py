# 파이썬 함수는 반환 값이 여러 개가 가능

def returnMulDiv(a, b):
  return a*b, a/b

m, d = returnMulDiv(6,2)
print("곱셈: ", m)
print("나눗셈: ", d)
