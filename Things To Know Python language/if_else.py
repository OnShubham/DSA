def age_cal():
    
    
    age = 18
    
    if age <= 18:
        print("A")
    else:
        print("B")
        
        
# age_cal()



def result(total_marks):
    
    
    if total_marks <= 35:
        print("fail")
    elif total_marks >= 35 and total_marks <= 50:
        print("pass")
    elif total_marks >= 50 and total_marks <= 70:
        print("C")
    elif total_marks >= 70 and total_marks <= 80:
        print("B")
    elif total_marks >= 80 and total_marks <= 90:
        print("A")
    else:
        print("A+")
    
total_marks = int(input("enter the number"))
result(total_marks)