import random
pt = 'HELLO WORLD'

# pt = input("Enter Plain Text").upper()
plain_text_alpha = list(('abcdefghijklmnopqrstuvwxyz').upper())
# key = [random.sample('qwertyuiopasdfghjklzxcvbnm'.upper()) for _ in range(26)]
key = list(random.sample('qwertyuiopasdfghjklzxcvbnm'.upper(),26))
print(key)
print(plain_text_alpha)
def ciphertext(plain_text, plain_text_alph, key, encryptedtext=None):
    for i in plain_text:
        if(plain_text_alph.__contains__(i)):
            encryptedtext += key[plain_text_alph.index(i)]
        else :
            encryptedtext += i
    return encryptedtext
def decrypt(enc_text, plain_text_alph,key):
    dt = ''
    for i in enc_text:
        if  plain_text_alph.__contains__(i):
            dt += plain_text_alph[key.index(i)]
        else:
            dt+= i
    return dt

encrypted = ciphertext(pt,plain_text_alpha,key,'')
decrypted = decrypt(encrypted,plain_text_alpha,key)
print(encrypted)
print(decrypted)