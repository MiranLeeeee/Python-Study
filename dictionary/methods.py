'''
사전 자료형 관련 메소드
1. keys(): 키 데이터만 가져와 리스트로 이용
2. values(): 값 데이터만 가져와 리스트로 이용
'''

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

key_list = data.keys()
value_list = data.values()

print("key 리스트: ", key_list)
print("value 리스트: ", value_list)

# 키 값을 가져와 각 키의 값을 출력
for key in key_list:
  print(key, data[key])
