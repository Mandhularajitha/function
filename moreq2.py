money=int(input("enter the money"))
student_expension=int(input("enter the  persons number"))
total_money=money*student_expension
if total_money<5000:
    print("Hum budget ke andar hain")
elif total_money==5000:
    print("budget is equal to 5000")
else:
    print("badget morethan 5000")    
