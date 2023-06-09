'''
파일 저장 명 : report_6_김경현.py

작성일 : 2023년 4월 20일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 두 개의 숫자를 입력받아 두 개의 수가 모두 짝수이면 두 수를 더한 결과를 출력하고, 그렇지 않고 둘 중 하나가 홀수이면 몇 번째 입력한 수를 짝수로 입력해야 하는지 출력하시오.  
'''

# 1. 두 개의 정수를 입력받는다.
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

# 2. 만약 두 개의 정수가 모두 짝수라면
if num1 % 2 == 0 and num2 % 2 == 0 :
    print(num1,"+",num2,"=",num1+num2)

# 3. 만약 두번째 정수만 홀수라면
elif num1 % 2 == 0 and num2 % 2 == 1 :
    print("두 번째 정수를 짝수로 입력하세요.")
    
# 4. 만약 첫번째 정수만 홀수라면
elif num1 % 2 == 1 and num2 % 2 == 0 :
    print("첫 번째 정수를 짝수로 입력하세요.")

# 5. 아니라면
else :
    print("두 숫자 모두를 짝수로 입력하세요.")
