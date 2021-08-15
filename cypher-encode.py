def numCheck(input):
    try:
        num = int(input)
    except:
        return(False)
    else:
        return(num)

def encrypt(text):
    output = ''
    for character in text:
        output = output + chr(ord(character)+key) if ord(character)+key <= 90 else output + chr(65 + (ord(character)+key-91))
    return(output)

def decrypt(text):
    output = ''
    for character in text:
        print(key-(ord(character)-65))
        output = output + chr(ord(character)-key) if ord(character)-key >= 65 else chr(90-(key-(ord(character)-65)))
    return(output)

key = False
text = input('Enter your text: ').upper()
while key == False or key > 26:
    key = numCheck(input('Enter the key: '))
    if key == False:
        print(f'{key} is not a valid number.')
    elif key > 26:
        print(f'The key must not be higher than 26.')

print('Encrypt: '+encrypt(text)+'\nDecrypt: '+decrypt(text))