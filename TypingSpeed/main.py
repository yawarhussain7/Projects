from time import *

import random as r

# check the spelling error 
def mistake(para,user):
    error = 0
    
    for i in range(len(para)):
        
        try:
            if para[i] != user[i]:
                error = error + 1
        except:
           error = error + 1

    return error

# check the speed of typing 
def speed_time(start,end,text):
    time_consume = end - start
    time_Round = round(time_consume,2)

    speed = len(text)/time_Round

    return round(speed)



while True:
    check = input("Do you want to start :> yes / no :> ")
    if(check == "yes"):
        test = ["It was a bright cold day in April, and the clocks were striking thirteen",
                "Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind,",
                    " slipped quickly through the glass doors of Victory Mansions, ",
                    "though not quickly enough to prevent a swirl of gritty dust from entering "]

        test1 = r.choices(test)
        print("<<<<<<<<<<<<<<<< Typing Speed >>>>>>>>>>>>>>>>\n");
        print(test1)
        print("\n\n")

        start_time = time()
        test_input = input("Enter :> ")

        end_time = time()

        print("Speed :> ",speed_time(start_time,end_time,test_input),"words/sec")
        print("Errors :> ",mistake(test,test_input))
    
    elif check == 'no':
        print("Program Close !")
        break;
    else:
        print('Invlid input ')