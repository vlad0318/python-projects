import base64

def encode():
    message = input('input the message that you want to encode: ')
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)

def decode():
    message = input('input the message that you want to decode: ')
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64decode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)

answere = 'y'
while answere == 'y' or answere == 'Y':
    print('***************************')
    print('*hit 1 to encode a message*')
    print('*hit 2 to decode a massage*')
    print('***************************')
    choice = int(input('chose an option: '))
    if choice == 1:
        encode()
    elif choice == 2:
        decode()
    else:
        print('invalid input')

    answere = input('do you want to use this program again: ')
