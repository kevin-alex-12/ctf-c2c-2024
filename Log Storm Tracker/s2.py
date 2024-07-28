from urllib.parse import unquote
# import re

er = []

with open('unicode.log') as f:
    y = f.readlines()


for line in y:
    esc = unquote(line.strip()[51:])

    with open("test.txt", "a") as myfile:
        try:
            myfile.write(esc)
            myfile.write("\n")
        except:
            er.append(esc)

print(er)