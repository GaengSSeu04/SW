'''
파일 저장 명 : 4장_0412_1_김경현.py

작성일 : 2023년 4월 12일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 입력 받은 정수가 양수인지 음수인지 0인지 판단하는 프로그램을 작성하시오.
'''
# 1. 정수를 입력받는다.
num = int(input("숫자를 입력 하시오 : "))
# 2. 만약 정수가 0보다 크면 
#       1) "00은 양수입니다.""
if num > 0 :
    print("{}은 양수입니다." .format(num))
# 3. 아니고 만약 정수가 0보다 작으면
#       1) "00은 음수입니다."
elif num < 0 :
    print("{}은 음수입니다." .format(num)) 
# 4. 아니면 
#       1) "0입니다"
else :
    print("{}은 0입니다." .format(num))