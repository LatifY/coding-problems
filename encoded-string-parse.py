def parse_code(txt):
    d = {"first_name":"","last_name":"","id":""}
    txt = txt.replace("0"," ").split()
    d['first_name'] = txt[0]
    d['last_name'] = txt[1]
    d['id'] = txt[2]
    return d

#alternative
import re
def parse_code2(txt):
	return dict(zip(('first_name', 'last_name', 'id'), re.split('0+', txt)))

print(parse_code("John000Doe000123"))