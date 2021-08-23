def encrypt(text,s):
result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text

      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
#check the above function
text = "CEASER CIPHER DEMO"
s = 4

print "Plain Text : " + text
print "Shift pattern : " + str(s)
print "Cipher: " + encrypt(text,s

#Caesar Cipher

## Overview of Caesar Cipher

 #- A cipher that is believed to be invented by the Roman General, Caesar.
 #- It is known to be the simplest and well-known Cipher/Decoding method.

 #- Input: A string of lowercase or uppercase letters((a to z, or A to Z), in alphabetical order)
 #- An integer between 0-25, indicating the shift of number
 #- There are 26 characters in English alphabet. And index starts from 0.
 #- So 0 to 25 basically indicates 26 English characters in alphabetical order at the input stage.)

### Procedure

 #- Traverse the given text, one English character at a time.
 #- And let's suppose that the shift is 3, meaning that in an alphabetical order,
 #- shift the string of all English Characters to the right 3(Shift) times, one by one.
 #- As a result, general alphabetical order changes, from
 #- A-B-C-D-E... -W-X-Y-Z to (Cipher code)
 #- X-Y-Z-A-B... -T-U-V-W. (Decipher code)
 #- So, depending on how big the shift is, the new string is generated.

#### Output

 #- For example,
 #- Text : ZXWW
 #- Shift : 3
 #- Cipher : WATT
