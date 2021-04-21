# python script to encrypt plain text and decrypt user input by brute forcing a caesar cypher from user input at the command line
import string
import collections


def caesar(pText, offset):
   upper = collections.deque(string.ascii_uppercase)
   lower = collections.deque(string.ascii_lowercase)

   upper.rotate(offset)
   lower.rotate(offset)

   upper =''.join(list(upper))
   lower =''.join(list(lower))

   return pText.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase,lower))


plainText = input("Enter plaintext(A-Z,a-z only):")
if plainText.replace(" ","").isalpha() is False:
    print("Only letters are allowed!")
    plainText = input("Enter plaintext(A-Z,a-z only):")

if plainText.replace(" ","").isalpha() is True:
    for i in range(len(string.ascii_uppercase)):
        print("["+str(i)+"]"+caesar(plainText.replace(" ",""),i))