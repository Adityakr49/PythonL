import time
# while loop =a statement that will execute it's block of code,
#             as long as it's condition remains true

# name=""
# name-None
# while len(name)==0:
#     name=input("Enter your name: ")
# print("Hello "+name)


# for loop= a statement that will execute it's block of code
#           a limited amount of times

#           while loop = unlimited
#           for loop = limited

# for i in range(10):
#     print((i+1))
#
# for i in range(50,100):
#     print(i)

# for i in range(50,101,2):
#     print(i)
#
# for i in "Bro Code":
#     print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new Year!")