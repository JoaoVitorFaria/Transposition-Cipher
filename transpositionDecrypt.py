import math, pyperclip
#code based on the book Cracking Codes with Python


def main():
    my_message =  'Cenoonommstmme oo snnio. s s c'
    
    for i in range(1,10):
        plaintext = decryptMessage(i, my_message)
        print('Key #%s: %s' %(i, plaintext))

        pyperclip.copy(plaintext)
        
    


def decryptMessage(key, message):
    #the number of colums is : length of message / key
    num_columns = int(math.ceil(len(message)/float(key)))
    num_rows=key
    #just remember: shades_boxes doesn't contain any symbol
    num_shades_boxes = (num_columns * num_rows)- len(message)
    #the descryption will be saved in the plaintext variable
    plaintext = ['']*num_columns

    column=0
    row=0
    
    for symbol in message:
        plaintext[column]+= symbol
        column+=1
        #it's just to verify if i'm in the end of a column, and if yes, jump to another row.
        if( column == num_columns) or (column==num_columns-1 and row>=num_rows- num_shades_boxes):
            column=0
            row+=1
    return ''.join(plaintext)


if __name__=='__main__':
    main()

        
