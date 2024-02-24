first_name=input("Enter your name:")
print(f"Hello {first_name}")
second_name=input("Enter you Partern's Name:")
both_name=first_name+second_name
final_name=both_name.lower()
t=final_name.count("t")
r=final_name.count("r")
u=final_name.count("u")
e=final_name.count("e")
first_digit=t+r+u+e
l=final_name.count("l")
o=final_name.count("o")
v=final_name.count("v")
e=final_name.count("e")
second_digit=l+o+v+e
score=int(str(first_digit)+str(second_digit))
if score <10 or score >=90:
  print(f"Your score is {score} is and You are like coke and mentos")
elif score >40 and score<90:
  print(f"Your score is {score} and you are alright together")
else:
  print(f"Your score is {score} and you love so much to each other ....You should Kiss now!!!")