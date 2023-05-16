'''
파일 저장 명 : 5장_0516_2_김경현.py

작성일 : 2023년 5월 16일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 사용자로부터 가장 좋아하는 월을 압력 받아 그 월에 해당되는 계절을 출력하는 프로그램을 메뉴형태로 while 문을 사용하여 작성하시오.
'''

# 1. 무한 반복하면서
while True :  
# 1) 월을 입력받는다
    month = int(input("가장 좋아하는 월은? : "))
# 2) 비교,판단하여 선택한다.
    if month == 0 :
        break
    elif month == 3 or month == 4 or month == 5 :
        print("{}월은 봄에 해당됩니다.".format(month))        
    elif month == 6 or month == 7 or month == 8 :
        print("{}월은 여름에 해당됩니다.".format(month))      
    elif month == 9 or month == 10 or month == 11 :
        print("{}월은 가을에 해당됩니다.".format(month))        
    elif month == 12 or month == 1 or month == 2 :
        print("{}월은 겨울에 해당됩니다.".format(month))   
    else :
        print("잘못된 월을 입력하였습니다.") 
            # 선택에 따른 결과 출력한다.
            