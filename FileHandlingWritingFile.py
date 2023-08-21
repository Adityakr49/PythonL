text="Yooooooooooo\nThis some text\nHave a good one:\n"
text1="Have a nice day"

# a = 'append' (add to exist)
# w = 'write' (delete if something exist and then write)
# r = 'read'
with open('Text1_py.txt','a') as file:
    file.write(text1)