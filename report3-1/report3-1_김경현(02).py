'''
파일 저장 명 : report3-1_김경현(02).py

작성일 : 2023년 6월 4일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 1부터 1000 사이의 소수를 구하여리스트에 저장한 후, 
소수와 소수의 개수를 출력하는 프로그램을 작성하시오.
'''
list = []

for i in range(1,1001) :
        dcount = 0      
          
        for j in range(1, i + 1) :
                if i % j == 0 : 
                        dcount = dcount + 1     
                        
        if dcount == 2 :        
                list.append(i)  
                
print('소수',(list))   
print('1부터 1000 사이의 소수 갯수는', len(list),'개 입니다.')  