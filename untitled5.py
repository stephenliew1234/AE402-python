score=input("how many scores would you like to put in?")
score=int(score)
scorelist=[]

for i in range(score):
   scoretemp=input("which score would you like to put in?")
   scoretemp=int(scoretemp)
   scorelist.append(scoretemp)
print(scorelist)

scoremax=scorelist[0]
scoremin=scorelist[0]
total=0
for i in range(score):
    if (scoremax < scorelist[i]):
        scoremax=scorelist[i]
    if (scoremin>scorelist[i]):
        scoremin=scorelist[i]
    total=scorelist[i]+total
avg=total/score
print(scoremax,scoremin,avg)wwww`
