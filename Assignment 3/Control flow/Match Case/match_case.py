# Match Case:
# It is similar like switch statement in other languages like(typescript/javascript) but more flexible.
# It provides more cleaner and readable alternative to traditional if elif else statements.

def student_result(grade):
    match grade:
        case 90:
            print("Excellent, A+1")
        case 80:
            print("A+1")
        case 70:
            print("A")
        case 60:
            print("B")
        case 50:
            print("C")
        case 40:
            print("Need to Work Hard!")
        case _:
            print("Default case!")    #like else in if else
            

student_result(90)   #Excellent, A+1
student_result(80)   #A+1
student_result(40)   #Need to Work Hard
student_result(20)   #Default case