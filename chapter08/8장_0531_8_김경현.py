'''
파일 저장 명 : 8장_0531_5_김경현.py

작성일 : 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 8장 파일 입출력
'''
# 3과목의 평균 점수를 계산하여 출력
        
print("== 학생 정보 읽어오기2 ==")
with open("student.txt", "r") as f :
    while True :
        std = f.readline()      
        if std == '' :
            break
        
        studentlist = std.split()   # 빈칸을 기준으로 리스트 객체로 반환
        name = studentlist[0] # 첫번째 항목을 name에 저장
        
        sum = 0
        for i in range(1, 4) :
            sum = sum + int(studentlist[i])
            
        print("{}의 평균 성적 : {}점 " .format(name, sum/3))
        
    