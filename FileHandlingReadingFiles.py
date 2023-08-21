
with open("Text_py.txt") as file:
    print(file.read())

# print(file.closed)#will close automatically for you

try:
    with open("C:\Users\adity\PycharmProjects\Learning\venv\BroCode\Text_py.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")