'''
파일 저장 명 : 4장_0411_4_김경현.py

작성일 : 2023년 4월 11일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 두 수를 입력 받아 큰 수를 출력하는 프로그램을 작성하시오.
'''
# 1. 두 수를 입력받는다.
num = int(input("숫자를 입력 하시오 : "))
num1 = int(input("다음 숫자를 입력 하시오 : "))

# 2. 처음 입력한 수가 더 높다면
if num > num1 :
    print("{}가 더 높습니다." .format(num))
# 3. 두번째로 입력한 수가 더 높다면
else :
    print("{}가 더 높습니다." .format(num1))