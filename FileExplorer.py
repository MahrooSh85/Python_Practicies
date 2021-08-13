import os


def showDatFiles(where):
    files = os.listdir(where)
    for file in files:
        if(os.path.isdir(file)):
            showDatFiles(where+"/"+file)
        elif(file.endswith('.txt')):
            print(where+"/"+file)


print("please enter the path: ")
path = input()
showDatFiles(path)

# print(os.listdir("/Users/mahroo/Programming_area/repositories/python_practicies/"))
# print(os.path.isdir("/Users/mahroo/Programming_area/repositories/python_practicies/anghezi"))