shift = 3

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for symbol in plaintext:
        symbol_code = ord(symbol)
        if 65 <= symbol_code < 88 or 97 <= symbol_code  <= 119:
            ciphertext += chr(symbol_code  + shift)
        elif 87 < symbol_code  < 91 or 119 < symbol_code  < 123:
            ciphertext += chr(symbol_code  - (26 - shift))
        else:
            ciphertext += symbol
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for symbol in ciphertext:
        symbol_code = ord(symbol)
        if 68 <= symbol_code <= 91 or 100 <= symbol_code <= 122:
            plaintext += chr(symbol_code - shift)
        elif 64 < symbol_code < 68 or 96 < symbol_code < 100:
            plaintext += chr(symbol_code+ (26 - shift))
        else:
            plaintext += symbol
    return plaintext

if __name__ == "__main__":
    while True:
        choice_message = input("Выберете действие (зашифровать / дешифровать): ")
        if choice_message.lower() == 'зашифровать':
            plaintext = input("Введите слово, которое хотите зашифровать: ")
            if plaintext == '':
                print('Пустая строка!')
            else:
                print(encrypt_caesar(plaintext, shift))
        elif choice_message.lower() == 'дешифровать':
            ciphertext = input("Введите слово, которое хотите зашифровать: ")
            if ciphertext == '':
                print('Пустая строка!')
            else:
                print(decrypt_caesar(ciphertext, shift))
        else:
            print('Ошибка операции, выберете что-то из этого (зашифровать / дешифровать): ')
