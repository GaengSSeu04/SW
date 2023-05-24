'''
파일 저장 명 : 6장_0524_1_김경현.py

작성일 : 2023년 5월 24일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 6장 시퀀스 자료형
        04. 리스트
'''
#튜플 생성
tuple = ()  # 빈 튜플 생성.
tuple2 = ('a',) # 원소가 하나여도 쉼표는 필수!!!
tuple3 = ("a",'b','c')

color = ('white','black','red','white','blue','green','white')
print("color 내용 : ", color)
print("color의 길이 : ", len(color))
print("white 개수 : ", color.count('white'))
print("green의 위치 : ", color.index('green'))

# 실습 예쩨 6-7
# 2개의 튜플을 하나의 리스트로 만들기
fruit = ('사과','배','딸기','수박','망고')
price = (2000,4500,8000,12000,5500)

# 결과 : [사과,2000,배,4500, ....]
fp_list = []    # 2개의 튜플 내용이 저장 될 리스트 생성.
fp_tuple = ()   # 2개의 튜플 내용이 저장 될 튜플 생성.

for i in range(len(fruit)) : 
    fp_list.append(fruit[i])
    fp_list.append(price[i])  
    # fp_tuple,append(fruit[i])     # 튜플은 변경이 안됨. 추가 안됨.
    
print("과일 목록 : ", fruit)
print("과일 목록 : ", price)
print("과일의 가격 리스트 : ", fp_list)

'''
fp_list.append(fruit[0])
fp_list.append(fruit[0])

fp_list.append(fruit[1])
fp_list.append(fruit[1])

fp_list.append(fruit[2])
fp_list.append(fruit[2])
'''
