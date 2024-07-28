switcher = {
	"04":"a", # or A
	"05":"b", # or B
	"06":"c", # or C
	"07":"d", # or D
	"08":"e", # or E
	"09":"f", # or F
	"0A":"g", # or G
	"0B":"h", # or H
	"0C":"i", # or I
	"0D":"j", # or J
	"0E":"k", # or K
	"0F":"l", # or L
	"10":"m", # or M
	"11":"n", # or N
	"12":"o", # or O
	"13":"p", # or P
	"14":"q", # or Q
	"15":"r", # or R
	"16":"s", # or S
	"17":"t", # or T
	"18":"u", # or U
	"19":"v", # or V
	"1A":"w", # or W
	"1B":"x", # or X
	"1C":"y", # or Y
	"1D":"x", # or Z
	"1E":"1", # or !
	"1F":"2", # or @
	"20":"3", # or #
	"21":"4", # or $
	"22":"5", # or %
	"23":"6", # or ^
	"24":"7", # or &
	"25":"8", # or *
	"26":"9", # or (
	"27":"0", # or )
	"2D":"-", # or _
	"2E":"+", # or =
	"2F":"[", # or {
	"30":"]", # or }
	"31":"\"", # or |
	"33":";", # or :
	"34":"'", # or "
	"35":"`", # or ~
	"36":",", # or <
	"37":".", # or >
	"38":"/" # or ?
}

with open("out.pcapdata", encoding='utf-8-sig') as my_file:
    dec = my_file.read().strip()

flag = ""

for i in dec:
    thd_bytes = i[4:6]

    try:
        aa = switcher[thd_bytes]
        flag += aa
    except:
        continue

print(flag)