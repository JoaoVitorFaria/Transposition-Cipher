#code based on the book Cracking Codes with Python
import pyperclip, detectEnglish, transpositionDecrypt
#this is a brute force approach to break the transposition cipher
def main():
    my_message = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hacked_message = hackTransposition(my_message)
    
    if hacked_message == None:
        print("Failed to hack encryption")
    else:
        print("Copying hacked message to clipboard")
        print(hacked_message)
        pyperclip.copy(hacked_message)


def hackTransposition(message):
    print("Hacking...")
    print("(Press Ctrl-C(Windows) or Ctrl-D(Linux) to quit at any time.)")
    # as a brute force approach, this code tries all the possible keys and use the detectEnglish code to verify if there is a possible english result
    for key in range(1, len(message)):
        print("Trying key #%s..."%(key))
        decrypted_text = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decrypted_text):
            print()
            print("Possible encryption hack:")
            print("Key %s: %s"%(key, decrypted_text[:100]))
            print()
            print("Enter D if done, anything else to continue hacking:")
            response = input('>')

            if responde.strip().upper().startswith('D'):
                return decrypted_text
    return None

if __name__=='__main__':
    main()
