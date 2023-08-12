from morse3 import Morse as m
def en_morse(plain_text):
    cipher_text=m(plain_text).stringToMorse()
    print(cipher_text)
    return cipher_text
def de_morse(cipher):
    plain_text=m(cipher).morseToString()
    print(plain_text)
    return plain_text
