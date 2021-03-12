#code based on the book Cracking Codes with Python
import pyperclip
#Transposition Cipher Encryption Code
def main():
    my_message = 'Common sense is not so common.'
    # the key must be from 2 to half the message size.
    my_key=8 

    #calling the function that gonna encrypt my_message
    ciphertext = encriptMessage(my_key, my_message)

    # this | is to verify it there is spaces at the end of the message
    print(ciphertext+'|')

    pyperclip.copy(ciphertext)
    
def encryptMessage(key, message):
    #each of this string represent a column in the grid
    ciphertext=['']*key
    for column in range(key):
        current_index = column
        #keep looping until current_index goes past the message length
        while current_index < len(message):
            ciphertext[column]+= message[current_index]
            current_index+=key
    #convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

if __name__=='__main__':
    main()
    
