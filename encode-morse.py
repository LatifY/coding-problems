print("Made By Latif Yılmaz (2020)")

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}#This is our dictionary. As the name says! Here, we keep our information!

def encode_morse(msg):
    newmsg = ""#This little string will be our morse code in the future :)
    msg = msg.upper()#We need to upper msg to convert. Cuz our dictionary contains upper chars.
    for char in range(len(msg)):
        newmsg+=char_to_dots[msg[char]]
        if(msg[char] != ' '):#We shouldn't leave a space any more because it is already a space :)
          newmsg+=" "
    return newmsg[:-1]#There will be an unnecessary space at the end of the sentence. We have to use substring to remove this. In this way, we can delete the last character of the string.


while True:
  print(encode_morse(str(input(": "))))

#Made by Latif Yılmaz
#2020