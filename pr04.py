# To implement Polyalphabetic cipher encryption-decryption
# Write a program to implement Polyalphabetic cipher encryption-decryption.

# Importing required modules
import os
import time


# Function to decrypt text
def decrypt(enc_text, plain_text_alph,key):
    dt = ''
    for i in enc_text:
        if  plain_text_alph.__contains__(i):
            dt += plain_text_alph[key.index(i)]
        else:
            dt+= i
    return dt

# Function to encrypt text
def encrypt(plain_text, plain_text_alph, key):
    encryptedtext = ''
    for i in plain_text:
        if(plain_text_alph.__contains__(i)):
            encryptedtext += key[plain_text_alph.index(i)]
        else :
            encryptedtext += i
    return encryptedtext

# Function to generate key
def generateKey(plain_text, key):
    key = key.upper()
    key = key.replace(' ', '')
    key = list(key)
    if len(key) == len(plain_text):
        return key
    else:
        for i in range(len(plain_text) - len(key)):
            key.append(key[i % len(key)])
    return key

# Function to generate key table
def generateKeyTable(key):
    key.replace('J', 'I')
    ListTemp = list(key)
    keyList = []
    for i in ListTemp:
        if i not in keyList:
            keyList.append(i)
    ListTemp = list("abcdefghijklmnopqrstuvwxyz".upper())
    ListTemp.remove('J')
    for i in ListTemp:
        if i not in keyList:
            keyList.append(i)
    keyTable = []
    for i in range(5):
        keyTable.append(keyList[5 * i: 5 * i + 5])
    return keyTable

# Function to generate plain text alphabet
def generatePlainTextAlph():

    # List of alphabets
    alphabets = list("abcdefghijklmnopqrstuvwxyz".upper())

    # Removing J from the list
    alphabets.remove('J')

    # Returning the list
    return alphabets

# Function to generate key alphabet
def generateKeyAlph(keyTable):
    keyAlph = []
    for i in range(5):
        for j in range(5):
            keyAlph.append(keyTable[i][j])
    return keyAlph

# Function to generate cipher text
def generateCipherText(plain_text, keyTable, keyAlph):
    cipherText = []
    for i in range(0, len(plain_text), 2):
        x = 0
        y = 0
        x1 = 0
        y1 = 0
        if plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[0:i + 1] + str('X') + plain_text[i + 1:]
        for j in range(5):
            for k in range(5):
                if keyTable[j][k] == plain_text[i]:
                    x = j
                    y = k
                if keyTable[j][k] == plain_text[i + 1]:
                    x1 = j
                    y1 = k
        if x == x1:
            if y < 4:
                y += 1
            else:
                y = 0
            if y1 < 4:
                y1 += 1
            else:
                y1 = 0
        elif y == y1:
            if x < 4:
                x += 1
            else:
                x = 0
            if x1 < 4:
                x1 += 1
            else:
                x1 = 0
        else:
            y, y1 = y1, y
        cipherText.append(keyTable[x][y])
        cipherText.append(keyTable[x1][y1])
    return cipherText

# Function to generate plain text
def generatePlainText(cipher_text, keyTable, keyAlph):
    