from collections import Counter

with open("secret.txt") as f:
    s = f.readlines()

full = ""

for text in s:
    cl = text.strip("\n")
    
    if cl == "":
        continue
    else:
        full += cl

# counter = Counter(full)
# print(counter)

# re = full.replace("q", "e")
# re = re.replace("i", "t")
# re = re.replace("r", "a")

print(full)