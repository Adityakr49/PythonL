# Lambda function = function writtern in one line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# lambda parameter:expression

# def double(x):
#     return x*2
# print(double(5))

double=lambda x:x*2
print(double(5))

muliply=lambda x,y:x*y
print(muliply(7,7))

add =lambda x,y,z:x+y+z
print(add(5,6,7))


full_name=lambda first_name,last_name:first_name+" "+last_name
print(full_name("Aditya","Singh"))

age_check=lambda age:True if age>=18 else False
print(age_check(18))

