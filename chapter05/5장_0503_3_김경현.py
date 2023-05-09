'''
파일 저장 명 : 5장_0503_3_김경현.py

작성일 : 2023년 5월 3일
학과 : 컴퓨터공학부
학번 : 202395003
이름 : 김경현
설명 : 
'''
# 1. 정수를 입력 받는다. (배수 - input_num)
# 2. 입력 받은 정수가 1부터 (num)
# 3. 합계는 0
# 4. 수가 10까지 반복하면서 (num)
#       a 수를 1 증가시킨다.
#   1) 만약에 수가 입력받은 수의 배수이면 :
#       1 합계를 계산한다.
#       b-1 수를 1 증가시킨다.
#       c 수를 1 증가시킨다.
#   2) 아니면(배수가 아니면) : 
#       b -1 수를 1 증가시킨다.
#       1 다시 처음으로 돌아간다. continue
#   e 수를 1 증가시킨다.
# 5. 합계를 출력한다.

input_num = int(input("정수 입력하시오 : "))
num = 0
sum = 0
while num <= 10 : 
    num = num + 1   # 증감식
    if num % input_num == 0 :
        sum = sum + num
    else :
        continue
print("{}의 배수의 합 : {}" .format(input_num,sum))

print("===============================")

input_num = int(input("정수 입력하시오 : "))
num = 0
sum = 0
while num <= 10 : 
    if num % input_num == 0 :
        sum = sum + num
        num = num + 1   # 증감식
    else :
        num = num + 1   # 증감식
        continue
print("{}의 배수의 합 : {}" .format(input_num,sum))

print("= for 반복문 ===============================")

input_num = int(input("정수 입력하시오 : "))

sum = 0

for num in range(1, 11) :
    if num % input_num != 0 :
        continue
    else :
        sum = sum + num
         
print("{}의 배수의 합 : {}" .format(input_num,sum))



