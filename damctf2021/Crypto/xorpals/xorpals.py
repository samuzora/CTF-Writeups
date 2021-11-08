with open('flags.txt', 'r') as f:
    words = f.readlines()

def bytexor(str, key):
    return bytes([c ^ key for c in str])

for word in words:
    word = word[:-1]
    for key in range(256):
        temp = bytexor(bytes.fromhex(word), key)
        if b'dam{' in temp:
            print(temp)
            break
    else:
        continue
    break
