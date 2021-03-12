import time, os, sys, transpositionEncrypt, transpositionDecrypt
#teste
#code based on the book Cracking Codes with Python
def main():
    #define the archive that i want to encrypt ou decrypt
    inputFileName = 'frankenstein.txt'
    #define the name of the encrypted/decrypted archive
    outputFileName= 'frankenstein.encrypted.txt'

    myKey=10
    #you could change this parameter to decrypt
    myMode= 'encrypt'

    if not os.path.exists(inputFileName):
        print("The file %s does not exist. Quitting..."%(inputFileName))
        sys.exit()

    if os.path.exists(outputFileName):
        print("This will overwrite the file %s. (C)ontinue or (Q)uit ?"%(outputFileName))
        response=input('>')
        if not response.lower().startswith('c'):
            sys.exit()

    #here i'm opening  my input file.
    fileObj = open(inputFileName)
    content = fileObj.read()
    fileObj.close()

    print('%sing...'%(myMode.title()))

    startTime= time.time()
    if myMode == 'encrypt':
        translated= transpositionEncrypt.encryptMessage(myKey, content)

    elif myMode == ' decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)

    totalTime= round(time.time()-startTime, 2)
    print("%sion time: %s seconds"%(myMode.title(), totalTime))

    #here i'm writing the encrypted/decrypted message
    outputFileObj= open(outputFileName, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()


    print('Done %sing %s (%s characteres).'%(myMode, inputFileName, len(content)))
    print("%sed file is %s."%(myMode.title(), outputFileName))


if __name__=='__main__':
    main()

