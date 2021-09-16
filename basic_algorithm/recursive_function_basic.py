# 재귀함수(Recursive function)

def recur():
	print("재귀함수의 예입니다.")
	recur();

recur();


# 재귀함수는 종료조건이 필요!

def recur(i) :
	if i==0: 
		return;
	print(i, "번째 실행중..")
	recur(i-1)

recur(5)		
