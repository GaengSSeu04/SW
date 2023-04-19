'''
파일 저장 명 : 4장_0419_2_김경현.py

작성일 : 2023년 4월 19일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 현재 월을 입력 받아 계절을 출력하시오.
'''

# 1. 첫번째 숫자를 입력받는다.
num = int(input("첫번째 숫자를 입력 하시오 : "))
# 2. 연산자를 입력받는다
cal = input("연산자를 입력하시오 : ")
# 3. 두번째 숫자를 입력받는다.
num1 = int(input("두번째 숫자를 입력 하시오 : "))


if cal == "+" :
    print("{} {} {} = {} 입니다.".format(num,cal,num1,num + num1))
elif cal == "-" :
    print("{} {} {} = {} 입니다.".format(num,cal,num1,num - num1))
elif cal == "*" :
    print("{} {} {} = {} 입니다.".format(num,cal,num1,num * num1))
elif cal == "/" :
    print("{} {} {} = {} 입니다.".format(num,cal,num1,num / num1))
# 4. 아니면
else :
    print("해당 연산자가 없습니다.")