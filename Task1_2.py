try:
    with open('myfile.txt') as file_object:
        print(file_object.read())
except FileNotFoundError:
    print('There is no such file in this directory!')
