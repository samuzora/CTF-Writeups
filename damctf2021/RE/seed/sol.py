#!/usr/bin/env python3
import sys
import time
import random
import hashlib

def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()

def main():
    for s in range(1609459200, 1636293118):
        random.seed(s, version=2)

        x = random.random()
        flag = hash(x)

        if 'b9ff3ebf' in flag:
            #with open("./flag", "w") as f:
                #f.write(f"dam{{{flag}}}")
            #f.close()
            print(f"dam{{{flag}}}")
            break

        #print(f"Incorrect: {x}")
    #print("Good job <3")

if __name__ == "__main__":
    main()
