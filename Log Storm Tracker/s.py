from urllib.parse import unquote
import re

with open('out.txt') as f:
    y = f.readlines()

er = []

for line in y:
    esc = unquote(line.strip())

    if ("{" in esc) or ("}" in esc):
        print(esc)
    
#     val = re.findall(r'\d+', esc)
    
#     ra = range(int(val[1]), int(val[2])+1)

#     try:
#         char = ra[int(val[0])-1]
#     except:
#         er.append(val)

#     print(chr(char), end="")

# print()
# print()
# print(er)