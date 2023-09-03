from time import *
import random as r

def mistake(paratest,user):
    error = 0
    for i  in range(len(paratest)):
        try:
            if paratest[i] != user[i]:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_st,time_end,user_input):
    time_delay = time_end - time_st
    time_r = round(time_delay,2)
    speed = len(user_input)/ time_r
    return round(speed,2)

while True:
    ck = input("Ready to test: yes/no:: ")
    if ck == "yes":
        test = ["A paragraph  is a self contained unit of discourage in writing.",
        "My name is Rajeshwar Swami" , "Welcome to my portfolio"]
        test1 = r.choice(test)
        print("***typing spedd***")
        print(test1)
        print()
        print()

        time_1 = time()
        test_input = input("Enter text : ")
        time_2 = time()

        print('Speed : ', speed_time(time_1,time_2,test_input),"w/sec")
        print("Error: ", mistake(test1,test_input))
    elif ck == "no":
        print("thank you for visiting")
        break
    else:
        print("wrong input")