'''
파일 저장 명 : 8장_0531_4_김경현.py

작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 8장 파일 입출력
'''
# print() 함수로 파일에 저장. 매개변수 file의 값으로 파일 객체에 저장.
f = open("ptext.txt", "w")

print ("컴퓨터공학부", file=f)
print ("202395003", file=f) # 다음 위치에 쓰기(파일에 출력)
print ("김경현", file=f)

f.close()

# with open("ptext.txt", "w") as f :
#print ("컴퓨터공학부", file=f)
#print ("202395003", file=f) # 다음 위치에 쓰기(파일에 출력)
#print ("김경현", file=f)
    