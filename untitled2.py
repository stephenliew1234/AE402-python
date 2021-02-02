import random 
num=random.randint(1,10)
x=input("what do number do you want to choose")
x=int(x)
if (x==num):
    print("get correct")
else:
    print("wrong")
    print("answer is num")