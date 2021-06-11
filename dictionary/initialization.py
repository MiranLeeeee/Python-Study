# dictionary 자료형 초기화

a = dict()
a['사과'] = 4000
a['바나나'] = 5000
print(a)

b= dict()
b = {
    '복숭아': 7000,
    '멜론': 10000
}
print(b)

#키를 통한 출력
print(b['복숭아'])

key_list = list(b.keys())
print(key_list)
