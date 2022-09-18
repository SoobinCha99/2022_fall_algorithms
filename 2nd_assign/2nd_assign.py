'''
#1st question 
id_pw = {} #initiallize id_pw dictionary
print("menu: [1]register [2]log in [3]delete account [0]exit program") 

while True:
    user_input_menu = input("select menu") #get menu
    user_input_menu = int(user_input_menu)
    
    #program exit menu
    if user_input_menu == 0: 
        print("existing program")
        break 
    
    #account register menu
    elif user_input_menu == 1: 
        register_id = input("enter perfered id") 
        if register_id in id_pw: #check for already existing account  
            print("id already exist")
        else: 
            register_pw = input("enter perfered password")
            id_pw[register_id] = register_pw 
            print("registered")

    #login menu
    elif user_input_menu == 2: 
        input_id = input("enter id")
        if input_id in id_pw: 
            input_pw = input("enter password")
            if input_pw == id_pw[input_id]:
                print("log in sucessful")
            else: 
                print("wrong password")
        else: 
            print("non existing id")
    
    #account delete menu
    elif user_input_menu == 3: 
        delete_id = input("enter id to delete")
        if delete_id in id_pw: 
            delete_pw = input("enter password")
            if delete_pw == id_pw[delete_id]: 
                del id_pw[delete_id]
                print("user account deleted")
            else: 
                print("worng password")
        else: 
            print("non existing id")
'''

'''
#2nd question 

import random #import random module 

operator = {0:"+", 1:"-", 2:"/", 3:"*"} #dictionary for random operator  

#lookup dict for calculation
operation = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y, 
            '/': lambda x, y: x / y,
            '*': lambda x, y: x * y}

count = 0 #variable for correct answers count 

user_settings = input("set integer limit") #get user input for integer limit
while True: 
    a = random.randrange(1,int(user_settings)) #get random int
    b = random.randrange(1,int(user_settings))

    operator_key = random.randrange(0,4) #get random operator 

    user_answer = input("what is {0}{1}{2}".format(a,operator[operator_key],b)) #get user input 

    if int(user_answer) == operation[operator[operator_key]](a,b): #process when correct 
        print(operation[operator[operator_key]](a,b))
        print("well done")
        count = count + 1 #count correct answers 
        
    else:  #process when wrong
        print("close, try again next time")
        print(operation[operator[operator_key]](a,b))
        print(count)
        break 
'''