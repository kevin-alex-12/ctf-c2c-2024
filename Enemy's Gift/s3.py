from PIL import Image, ImageDraw

x = 300
y = 300

img = Image.new("RGB",(2000,1000),"white")
dr = ImageDraw.Draw(img)
n = 2

with open('out.pcapdata', encoding='utf-8-sig') as f:
    for line in f:
        cl = line.strip()
        coords = [j if j<128 else (j-256) for j in [int("0x"+cl[i:i+n], 16) for i in range(0, len(cl), n)]]
        x += coords[1]
        y += coords[2]
        # print(x, y)

        # if coords[0] != 0:
        dr.rectangle(((x - 2, y - 2), (x + 2, y + 2)), fill="black")

img.show()