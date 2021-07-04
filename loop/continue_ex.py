
scores = [93, 88, 78, 60, 97, 95, 90]
#1번, 6번 학생이 부정행위자일 경우 F임 
# 부정행위자 집합
cheating_student_list = {1, 6}

for i in range(7):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 90:
        print(i+1, "번 학생은 A+입니다.")
