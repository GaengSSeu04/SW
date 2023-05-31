'''
파일 저장 명 : 8장_0531_2_김경현.py

작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 8장 파일 입출력
'''
# writelines() 메소드
list1 = ['월요일\n', '화요일\n', '수요일\n', '목요일\n', '금요일\n', '토요일\n', '일요일\n']

# readline() 메소드 사용하여 무한 반복문으로 읽기
print("== 무한 반복문으로 이용하여 읽기 ==")
with open("Linetest.txt", "r") as f :
    while True :
        line = f.readline()
        print(line, end='')
        
        if line == '' :
            break