'''
파일 저장 명 : 8장_0530_1_김경현.py

작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 8장 파일 입출력
'''
# open() 함수로 파일 쓰기 - 추가모드 a
f = open("text.txt", "w")   # 파일 오픈(추가)

f.write("추가 메세지입니다. \n")

f.close() 