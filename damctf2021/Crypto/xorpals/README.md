# crypto/xorpals

Author: m0x

One of the 60-character strings in the provided file has been encrypted by single-character XOR. The challenge is to find it, as that is the flag.

Hint: Always operate on raw bytes, never on encoded strings. Flag must be submitted as UTF8 string.

---

XOR Encryption: Performs eXclusive-OR operations on individual bytes of plaintext and key (pt[0] ^ key[0]) 

```
1 ^ 1 = 0
0 ^ 1 = 1
1 ^ 0 = 1
0 ^ 0 = 0
```

In Python, the XOR operator is the caret (^)

The file provided is a list of 99 strings of length 60 bytes (120 digits as each byte is 2 hex digits)

We could potentially copy each string and paste it into Cyberchef XOR Bruteforce Recipe, and search for the flag format in the output. However that is too slow

Another way is to write our own XOR Bruteforce. Since the key is only 1 byte, we have a total of 16**2=256 combinations in hex notation. Since hex can be expressed as decimal, we can bruteforce the key via range(256), eg. 0-255.  

What bytes([c ^ key for c in str]) does: stores the value of c in an iterable for c in str (done via []), and converts this list into a byte literal.

bytes.fromhex() converts the input from hex into a byte literal (note: byte literal are actually arrays of ints from 0-255 in Python; thus for byte object b=b'abc', b[0] == ord('a') == 97. This was really confusing for me as byte objects accept and output valid ASCII bytes, so I assumed that byte objects were just byte strings. (For non-ASCII bytes, they must be properly escaped via '\x'.))

Lastly, I check for the flag format in the byte object. Flag: b'dam{antman_EXPANDS_inside_tHaNoS_never_sinGLE_cHaR_xOr_yeet}'
