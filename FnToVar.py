def hello():
    print("Hello")

# print(hello)#prints memory address of fn


hi=hello #hello has two name hello and hi as they point to same mem address
hi()

say=print
say("Whoa! I can't believe this works 😮")