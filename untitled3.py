Math=input("please put math score")
Math=int(Math)
Englsih=input("please put english score")
English=input(English)
if (Math>= 90 and English >=90):
    print("get reward")
elif (Math<=60 and English <=60):
   print("get punished")
else (Math>=60 and English <=60):
    print("study more"  )
    