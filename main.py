import os
import subprocess

def read_from_file(fileName):
    try:
        with open(fileName, 'r') as file:
            lines = file.readlines()

        list = []

        for line in lines:
            if line.split('"')[0] == "app = ":
                x = [line.split('"')[1], 1]
                print(x[0])
                print(x[1])
                list.append(x)
            else:
                x = [line.split('"')[1], 0]
                print(x[0])
                print(x[1])
                list.append(x)

        return list

    except FileNotFoundError:
        print("File error!")


result = read_from_file("configuration.txt")

for process in result:
    if process[1] == 0:
        subprocess.Popen(['firefox', process[0]])
    else:
        subprocess.Popen(process[0])


