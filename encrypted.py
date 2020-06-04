message = input('Digite uma mensagem: ')
encrypted = ''
for letter in message:
    if letter == '':
        encrypted += ''
    else:
        encrypted += chr(ord(letter) + 5)

print(encrypted)