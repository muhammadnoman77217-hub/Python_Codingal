att= float(input("Enter your attendance out of 100 : "))
if att>=75:
    print("you re eligible to write the exam")
else:
    tour_reason=input("do you have a tour reason ?(yes/no) ")
    if tour_reason == "yes" and att>60:
        print("you are eligible since you have more than 60 and a tour reason")
    else:
        print("not eligible")