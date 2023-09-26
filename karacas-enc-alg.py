vowels = {"a":"0","e":"1","i":"2","o":"2","u":"3"}

def encrypt(word):
    word = word[::-1]
    new_word = ""
    for let in word:
        if(let in vowels):
            new_word += vowels[let]
        else:
            new_word += let
    return new_word+"aca"
print(encrypt("karaca"))