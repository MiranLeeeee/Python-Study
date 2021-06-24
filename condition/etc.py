'''
1. in(포함여부)
   a in 리스트, 튜플, 문자열, 딕셔너리: a가 존재하면 True를 반환
  <-> a not in: a가 없으면 True를 반환
2. pass(처리하고 싶지 않을 때)
   디버깅 과정 등에서 형태만 만들어 테스트하고 싶을 때 등 사용
'''

num = 3
numList = [1,2,3,4,5]

if num in numList:
  pass
else:
  print("1~5 사이 속하지 않는 정수입니다.")

print("프로그램을 종료합니다.")
