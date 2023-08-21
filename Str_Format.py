# str.format() = optional method that gives users
#                more control when displaying output

# animal="cow"
# item="moon"
#
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item)) #positional argument
# print("The {animal} jumped over the {item}".format(animal="Dog",item="table")) #keyword argument
#
# text="The {} jumped over the {}"
# text=text.format(animal,item)
# print(text)

# name="Bro"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {name1:10}. Nice to meet you".format(name1="Bro"))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))



number = 1000
print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))#to add ',' after every 1000
print("The number pi is {:b}".format(number))#to binary
print("The number pi is {:o}".format(number))#to octadecimal
print("The number pi is {:x}".format(number))#to hexadecimal
print("The number pi is {:E}".format(number))#to scientific