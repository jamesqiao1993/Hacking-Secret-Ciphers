#Reverse Cipher反转加密

#加密
message = 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)

#解密
#message = 'Three can keep a secret, if two of them are dead.'
translated2 = ''

i = len(message) - 1
while i >= 0:
    translated2= translated2 + translated[i]
    i = i - 1

print(translated2)
