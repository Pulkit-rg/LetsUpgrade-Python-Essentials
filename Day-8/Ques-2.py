
file= open("hello.py","r")
try:
    file.write("Hello")
except IOError:
    print(" 'hello.py' File is opened in write mode, Can't be modified.")

file.close()























