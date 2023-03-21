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


def fillerLetter(pt):
    k = len(pt)
    pt = pt.upper()
    new_word = ''
    if k % 2 == 0:
        for i in range(0, k, 2):
            if pt[i] == pt[i + 1]:
                new_word = pt[0:i + 1] + str('X') + pt[i + 1:]
                new_word = fillerLetter(new_word)
                break
            else:
                new_word = pt
    else:
        for i in range(0, k-1, 2):
            if pt[i] == pt[i + 1]:
                new_word = pt[0:i + 1] + str('X') + pt[i + 1:]
                new_word = fillerLetter(new_word)
                break
            else:
                new_word = pt
    return new_word

def createGroupList(pt):
    ptList= list(pt)
    group = []

# pt = input("Enter Plain Text").upper()
# key = input("Enter Key").upper()
key = "playfair"
keyTable = generateKeyTable(key)
print(keyTable)

# fillerLetter("illustrate")
