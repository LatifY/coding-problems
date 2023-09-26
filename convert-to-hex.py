#txt to ascii print(ord('A'))
#ascii to txt print(chr(65))
def convert_to_hex(txt):
    data = []
    for let in txt:
        data.append(ord(let))
    return(" ".join("{:01x}".format(c) for c in data))

print(convert_to_hex("Hello Word"))