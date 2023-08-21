# Scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created

name="Bro" #global var(available inside and outside functions)

def display_name():
    name="code" #local scope (availabe only inside this function)
    print(name)

display_name()
print(name)