'''
파일 저장 명 : report_1_김경현.py

작성일 : 2023년 4월 20일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 정수 하나를 입력받아 자릿수를 구하는 프로그램을 작성하시오. 그리고 입력받은 정수가 네 자리 수 이상이면 '네 자리 수 이상입니다.'를 출력하시오
'''

# 1. 정수를 입력받는다.
num = int(input("정수를 입력 하시오 : "))

# 2. 만약 한자리 정수를 입력받았다면
if -10 < num < 10 :
    print ("입력받은 정수는 한 자리 수입니다.")

# 3. 만약 두자리 정수를 입력받았다면
elif -100 < num < 100 :
    print ("입력받은 정수는 두 자리 수입니다.")

# 4. 만약 세자리 정수를 입력받았다면
elif -1000 < num < 1000 :
    print ("입력받은 정수는 세 자리 수입니다.")

# 5. 만약 네자리 이상 정수를 입력받았다면
else :
    print ("입력받은 정수는 네 자리 수 이상입니다.")