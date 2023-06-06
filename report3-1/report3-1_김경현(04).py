'''
파일 저장 명 : report3-1_김경현(04).py

작성일 : 2023년 6월 4일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 다음과 같은 튜플에서 중복된 숫자와 중복 횟수를 출력하고, 
중복이 제거된 요소를 리스트로 출력하는 프로그램을 작성하시오.
'''

num = (1,2,4,4,2,3,7,7,9,3) 
print("최초의 튜플:", num)

a_list = [] 
a_list1 = []

for i in num :
    if i not in a_list :
        if num.count(i) >= 2 :
            print("중복된 숫자 :", i ,",", num.count(i),"회")
            a_list.append(i)
            a_list1.append(i)

print("중복이 제거된 리스트 :", list(set(num)))


