 # get email from user 
Email = input("Enter your Email : ")

#Flages
space = 0
symbol = 0
upper = 0

# check the Email length is greater or equal to 6 OR not 
if len(Email) >= 6:
    # check the first index is alphabat OR Not
    if Email[0].isalpha():
        # check the ' @ ' in include and use One time OR NOT
        if ("@" in Email) and (Email.count("@") == 1):
            # check the . position for ' com ' and ' in'
            if (Email[-3] == ".") ^ (Email[-4] == "."):
                # check  " space, uppercase letters  and digits " for every Alphabat 
                for i in Email:
                    #check for Space  to ever index
                    if i.isspace():
                        space = 1
                     #check for Alphabat to ever index
                    elif  i.isalpha():
                         #check for Upperletter to ever index
                        if  i.isupper():
                            upper =1
                     #check for Digits  to ever index
                    elif  i.isdigit():
                        continue
                     #check for _ . and @  to ever index
                    elif (i == '_' or i == '.' or i == '@'):
                        continue
                    else:
                        symbol = 1

                if space == 1 or upper == 1 or symbol == 1:
                    print("Space Error Or Upper or Symbol Errors")
                else:
                    print("Rigth Email ")
            else:
                print(". Error ")
        else:
            print("@ Error ")

    else:
        print("First index Error ")

else:
    print("Invalid Email 1")