key_max_size = 26

alphabet = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 
    'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 
    'X': 23, 'Y': 24, 'Z': 25
}

def getMessage() -> str: # solicita el mensaje a encriptar
    print('Introduzca el mensaje:')
    return input().upper()

def getAction () -> str: # solicita la accion a realizar (encriptar o desencriptar)
    while True:
        print('Seleccione una accion:' + '\n'
              '[e] encriptar' + '\n'
              '[d] desencriptar')
        action = input().lower()
        if action in ['e','d']:
            return action
        else:
            print('Seleccione una accion valida')

def getKey() -> int: # solicita la clave
    key = 0
    while True:
        print(f'Introduzca la clave (1-{key_max_size})')
        key = int(input())
        if (key >= 1 and key <= key_max_size):
            return key
        else:
            print(f'Introduzca una clave valida (1-{key_max_size})')

#message debe venir en mayus
def encryptDecryptMessage(message: str, key: int, action: str) -> str: # encripta o desencripta el mensaje
    encrypted = ''
    for letter in message:
        if letter in alphabet:
            encrypted += encryptLetter(letter, key, action)
        else:
            encrypted += letter
    return encrypted

def encryptLetter(letter: str, key: int, action: str) -> str: # encripta una letra
    letter_value = alphabet[letter]

    if action == 'e':
        encrypted_value = (letter_value + key) % key_max_size
    elif action == 'd':
        encrypted_value = (letter_value - key) % key_max_size

    for key, value in alphabet.items():
        if value == encrypted_value:
            return key

action = getAction()

if action == 'e':
    key = getKey()
    message = getMessage()
    print(encryptMessage(message, key))

