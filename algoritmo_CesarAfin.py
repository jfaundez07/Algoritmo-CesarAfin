from aritmeticaModular import sumaModular, restaModular, coprimos, inversoModular, multiplicaciónModular

# posicion_encriptada = (a * x + b) % n
# posicion_desencriptada = (a^-1 * (posicion_encriptada - b)) % n



alphabet = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 
    'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'Ñ': 15, 'O': 16, 'P': 17, 
    'Q': 18, 'R': 19, 'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 
    'X': 25, 'Y': 26, 'Z': 27
}

n_max = len(alphabet)
print(n_max)

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

def getA() -> int: # solicita la constante de amplificacion
    a = 0
    while True:
        print(f'Introduzca la constante de amplifiacion (a > 1, excepto 2)')
        a = int(input())
        if validateA(a):
            return a
        else:
            print(f'Introduzca una constante de amplifiacion valida (a > 1, excepto 2)')

def getB() -> int: # solicita la constante de desplazamiento
    b = 0
    while True:
        print(f'Introduzca la constante de desplazamiento (1-{n_max})')
        b = int(input())
        if (b >= 1 and b <= n_max):
            return b
        else:
            print(f'Introduzca una constante de desplazamiento valida (1-{n_max})')

def validateA(a: int) -> bool: # valida que el valor de a sea valido
    if a < 1:
        return False
    elif not coprimos(a, n_max):
        return False
    return True
    
def encryptMessage(message: str, a: int,b: int) -> str: # encripta o desencripta el mensaje
    encrypted = ''
    for letter in message:
        if letter in alphabet:
            encrypted += encryptLetter(letter, a, b)
        else:
            encrypted += letter
    return encrypted

def encryptLetter(letter: str, a: int, b: int) -> str: # encripta una letra
    letter_value = alphabet[letter] # letter_value  corresponde a la x en posicion = (a * x + b) % n
    amplified_letter_value = a * letter_value # a * x

    encrypted_value = sumaModular(amplified_letter_value, b, n_max) # (amplified_letter_value + b) % n_max
    print(encrypted_value)
    for b, value in alphabet.items():
        if value == encrypted_value:
            return b
        
def decryptMessage(message: str, a: int,b: int) -> str: # desencripta el mensaje
    decrypted = ''
    for letter in message:
        if letter in alphabet:
            decrypted += decryptLetter(letter, a, b)
        else:
            decrypted += letter
    return decrypted
        
def decryptLetter(letter: str, a: int, b: int) -> str: # desencripta una letra
    letter_value = alphabet[letter] 
    modular_inverse = inversoModular(a, n_max) 
    difference = letter_value - b
    encrypted_value = multiplicaciónModular(modular_inverse, difference,n_max)
    print(encrypted_value)
    for b, value in alphabet.items():
        if value == encrypted_value:
            return b


def main():
    while True:
        print('\nContinuar? (s: SI)')
        choice = input().lower()

        if choice != 's':
            break

        action: str = getAction()
        a: int = getA()
        b: int = getB()
        message: str = getMessage()
        
        if action == 'e':
            encrypted_message = encryptMessage(message, a, b)
            print(f'Mensaje encriptado: {encrypted_message}')
        elif action == 'd':
            decrypted_message = decryptMessage(message, a, b)
            print(f'Mensaje desencriptado: {decrypted_message}')

main()