a ="HelloWorld"
key = "a"
# a = input("Enter Plain Text :")
# key = input("Input Key:(Only First Letter will be Considered.) ")
encryptedtext = ''
def ciphertext(a, key, encryptedtext=None):
    try:
        key = int(key[0])
    except Exception as e:
        key = ord(key[0]) - (ord('A') if key.isupper() else ord('a'))
    finally:
        for i in range(len(a)):
            encryptedtext += chr((ord(a[i]) + key) % (26 + (ord('A') if a[i].isupper() else ord('a'))))
    return encryptedtext


print(ciphertext(a, key,''))
