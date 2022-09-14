'''
#1st question 

import random #import module for random number

print("덧셈 공부를 해봅시다!")

#count = 0 #variable to count correct problems

for i in range(0,9999):
    a = random.randrange(1,100) #create random int variable 
    b = random.randrange(1,100)
    answer = a+b #calculate correct answer 

    print(a,"+",b,"=", end=' ') #show user the problem 
    user_input = int(input()) #create input variable 
    print(user_input) 

    if user_input == answer: #when correct 
        print("잘했어요!")
        #count = count + 1 #update count variable 
    else: #when incorrect 
        print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")
        #print("총 맞힌 문제의 수",count) 
        print("총 맞힌 문제의 수",i) #show num of correct problems
        break 
'''

'''
#2nd question

print("숫자 4개 입력(작성 예시: 1 2 3 4)") 

x,y,w,z = input().split() #get input 
x,y,w,z = int(x), int(y), int(w), int(z) #convert input string to integer dtype

avg_condition = (x+y+w+z) / 4 > 60 #define average condition
min_condition = x>40 & y>40 & w>40 & z>40 #define min condition

#print output  
if avg_condition == True & min_condition == True: 
    print("합격") #print 합격 when both conditions are met
else: 
    print("불합격")
'''

'''
#3rd question 

print("주민 등록 번호를 입력하세요.(001212-4)") 
user_input = input() #get id  
print(user_input)  #prind id 

#get gender from id 
def print_gender(user_input):  
    gender = user_input.split('-')[1]
    if  gender ==1:
        print("당신의 성별은 남자이며,")
    else: 
        print("당신의 성별은 여자이며,")

#get belt from id 
def print_belt(user_input): 
    birth_year = birth_year = user_input[0:2]
    if birth_year==0:
        print ("원숭이 띠이다.")

    elif birth_year==1:
        print("닭 띠이다.")

    elif birth_year==2:
        print("개 띠이다.")

    elif birth_year==3:
        print("돼지 띠이다.")

    elif birth_year==4:
        print("쥐 띠이다.")

    elif birth_year==5:
        print("소 띠이다.")

    elif birth_year==6:
        print("범 띠이다.")

    elif birth_year==7:
        print("토끼 띠이다.")

    elif birth_year==8:
        print("용 띠이다.")

    elif birth_year==9:
        print("뱀 띠이다.")

    elif birth_year==10:
        print("말 띠이다.")

    else:
        print("양 띠이다.")

#print output 
print_gender(user_input)
print_belt(user_input)
'''

'''
#4th question

#define break conditions 
break_condition1 = 'x'
break_condition2 = 'X'
break_condition3 = 'ㅌ'

#loop till break conditions are met 
while True: 
    user_input1 = input("숫자 입력(종료 : x)>>>") #get input     

    if user_input1 == break_condition1: #evaluate break condition
        break 
    elif user_input1 == break_condition2: 
        break 
    elif user_input1 == break_condition3:
        break 
    else: #print output when break conditions are not met 
        user_input2 = input("특수 문자>>>")  
        print(user_input2 * int(user_input1))
'''

'''
#5th question 

#define break conditions 
break_condition1 = '0'
break_condition2 = 'o'
break_condition3 = 'ㅐ'

#initialize dictionary
ad_book = {} 

print("주소록 프로그램 시작")

while True: 
    print("------------")
    print("[1]추가 [2]검색 [3]삭제 [4]변경 [5]전체 주소록 보기 [0]종료") 
    user_input_menu = input("메뉴를 입력하세요") #get menu from user 
    
    #evaluate break conditions  
    if user_input_menu == break_condition1: 
        break 
    elif user_input_menu == break_condition2:
        break 
    elif user_input_menu == break_condition3: 
        break 

    #add address 
    elif int(user_input_menu) == 1: 
         user_input_name = input("추가하고자 하는 이름 입력")
         user_input_ph = input("추가하고자 하는 연락처 입력")
         ad_book[user_input_name] = user_input_ph
    
    #search address
    elif int(user_input_menu) == 2: 
        user_input_search = input("검색하고자 하는 이름 입력")
        print(ad_book[user_input_search])

    #remove address 
    elif int(user_input_menu) ==3: 
        user_input_pop = input("삭제하고자 하는 이름 입력")
        ad_book.pop(user_input_pop)
        print("찾는 이름은 없습니다.")

    #change address 
    elif int(user_input_menu) ==4:
        user_input_change_key = input("변경하고자 하는 이름 입력")
        user_input_change_value = input("변경하고자 하는 연락처 입력")
        ad_book[user_input_change_key] = user_input_change_value
        
    #view whole address book 
    elif int(user_input_menu) == 5: 
        for k,v in ad_book.items(): 
            print(k,v)
'''

