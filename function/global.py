# global: 해당 함수에서 지역변수를 만들지 않고 함수 밖의 변수를 참조

a = 0

def func(): #global a에 1을 더해주는 함수
    global a
    a += 1
    
for i in range(10): #10번 더해줌
    func()
    
print(a) # 10    
