# User sinup and signin program
user_dict = {}
while True:
    print("1,Sinup") 
    print("1,Signin") 
    print("3,exit")
    opt = int(input("Enter your option"))
    if opt == 1:
        print("***User ragistion***")
        username = input("Enter User name")
        pwd = input("pwd")
        if username in user_dict:
            print("User is Exist")
        else:
            user_dict[username] = pwd
            print("User is Ragister Successfully")
    elif opt == 2:
        print("***SignIn***")
        username = input("Enter User name")
        pwd = input("Pwd")
        if username in user_dict:
            if user_dict[username] == pwd:
                print(f"{username} Wellcome To Page")
            else:
                print("Invalid Password")
        else:
            print("Invalid Username")
    elif opt == 3:
        break
    else:
        print("Input option 1-3") 