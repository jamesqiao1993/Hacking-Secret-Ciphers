# Transposition Cipher Encryption
import sys
sys.path.append('..')
import pyperclip as pyper

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # print the enctypted string in ciphertext to the screen, with
    # a | (called "pipe" character) after it in case there are spaces at
    # the end of the encrypted message
    print(ciphertext + '|')

    # copy the encrypted string in ciphertext to the clipboard
    pyper.copy(ciphertext)
    
def encryptMessage(key, message):
    # Each string in ciphetext represent a column in the grid
    ciphertext = [''] * key

    # Loop through each column in ciphertext
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message
        while pointer < len(message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # Covert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

# If transpoitionEncrypt.py is run (instead of imported as a module) call
# the main() function
if __name__ == '__main__':
    main()
