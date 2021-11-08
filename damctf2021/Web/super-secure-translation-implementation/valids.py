import string
import base64

allowed = string.printable[:-5] # all printable characters except special ones (like newlines)
print(allowed)
disallowed = ['.', ' ', 'T', 'J', '2', '7', 'I', 'E', 'w', 'O', 'D', 'R', 'k', 'p', 'Q', 'y', 'U', 's', 'i', 'V', '5', 'z', 'm', 'q', 'B', '0', 'g', 'x', 'A', 'j', 'X', '8', 'f', 'n', 'F', 'G', 'a', 'W', 'K', '9', 'S', '3', 'C', 'H', 'L', 'Z', 'v', 'Y', 't', 'M', '!', 'P', 'N']
for char in disallowed:
    if char in allowed:
        allowed = allowed.replace(char, '')

desired = "\157\160\145\156"

output = []


for i in desired:
    if i not in allowed:
        output.append('ch('+str(ord(i))+')')
    else:
        output.append(i)

print('+'.join(output))
