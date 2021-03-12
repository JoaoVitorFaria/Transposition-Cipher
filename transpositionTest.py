#code based on the book Cracking Codes with Python
#importing the modules that cointain the functions to encrypt and decrypt with the transposition cipher
import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    #define the seed, which is takes as initial number to produce another numbers with random.
    random.seed(42)
    for i in range(20):
        #random.randint takes the two arguments and return a random integer between those numbers.
        #duplicating this string a random number of times to create a new test
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)
        message=list(message)
        #scrambling the characters in the string that we converted to a list
        random.shuffle(message)
        #converting the scrambled list back to string
        message= ''.join(message)
        print('Test #%s: "%s..."' %(i+1, message[:50]))

        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)
            #Finally, we check if the original message is the same as the decrypted message
            if message != decrypted:
                print('Mismatch with key %s and message %s.' %(key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()
        print('Transposition cipher test passed.')

if __name__=='__main__':
    main()
