'''
파일 저장 명 : 8장_0531_5_김경현.py

작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 8장 파일 입출력
'''
# 5명 학생 성적 저장 파일 만들기 실습 예제 8-2
# write() 메소드와 readline() 메소드를 이용하여 
# 학생 이름과 3과목의 성적을 리스트로 생성하여 파일에 저장.
# 입력 예 ) 홍길동 100 95 77

print("== 학생 정보 읽어오기 ==")
with open("student.txt", "r") as f :
    while True :
        std = f.readline()
        print(std,end='')
        
        if std == '' :
            break
        
print("== 학생 정보 읽어오기 ==")
with open("student.txt", "r") as f :
    while True :
        std = f.readline()
        studentlist = std.split()   # 빈칸을 기준으로 리스트 객체로 반환
        print(studentlist)
        
        if std == '' :
            break