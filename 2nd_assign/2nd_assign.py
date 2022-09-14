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