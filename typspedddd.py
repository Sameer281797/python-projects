from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error
    
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
if __name__ == '__main__' :       
    while True:
        ck = input(" ready for test : (yes/no) : ")
        if ck == "yes":
            test = ["A paragraph is a self contained unit of discourse in writing dealing with a particular point or idea." ,
                    "amanda loves to play basketball and she is a really deserving player to represent her country and make her parents teacher school and citizens of country proud on her." ,
                    "in this youtube channel wscube we will provide every essential tools to make your programming skills better." ,
                "there are nine planets in our solar system and there names are mercury venus earth mars jupiter saturn uranus neptune and pluto."]

            test1 = r.choice(test)
            print("*****typing speed*****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter :  ")
            time_2 = time()

            print('speed : ',speed_time(time_1,time_2,testinput)," w/s")
            print("Error : ",mistake(test1,testinput))
        
        elif ck == "no":
            print("Thakn you")
            break
        else:
            print("Wrong input")
        

