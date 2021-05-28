# 인덱싱: 리스트의 특정한 요소에 접근하는 것
# 파이썬 경우 인덱스는 양수, 음수(역순검색) 가능
# 음수 인덱스  ex) -1은 마지막에서 첫번째 요소를 의미

a = [1,2,3,4,6]
print(a[0]) # 1

# 음수 인덱스를 활용한 역순 인덱싱
print(a[-1]) # 6

# 인덱스를 통한 원소 값 수정 가능
a[4] = 5
print(a)

