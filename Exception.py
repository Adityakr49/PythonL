# exception = events detcted during execution that interupt the flow of a program

try:
    numerator=int(input("Enter a number to divide: "))
    denominator=int(input("Enter a number to divide by: "))
    result=numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't devide by zero: idiot: ;)")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("Something went Wrong ;(")
else:
    print(result)#if there is no exception
finally: #even if exception happen this will execute
    print("Outside the try catch")
    print("This will always execute")