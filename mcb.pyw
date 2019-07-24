#! python3

# mcb.pyw saves and loads the multiple content to be copied
# It does so by saving it in different variables that are accessible outside

import sys, shelve, pyperclip
#sys is needed to receive the commmand line arguments
#shelve is needed to access the variables outside the python world
# pyperclip is needed to copy paste the elements of shelve files

# Command-line arguments
# mcb.pyw save <keyword> : Copy the clipoard a word named 'keyword'
# mcb.pyw <keyword> : Loads 'keyword' to clipboard
# mcb.pyw list : List all keywords on clipboard

mcbShelf = shelve.open('mcb')

#saving clipboard content in a keyword
if(len(sys.argv==3) and sys.argv[1].lower()=='save'):       #saving clipboard content in a keyword
    mcbShelf[str(sys.argv[2])]=pyperclip.paste              #content corresponding to the keyword is earlier copied in pyperclip and here its pasted
elif(len(sys.argv==2)):                                     
    if(sys.argv[1].lower()=='list'):                        
        pyperclip.copy=str(list(mcbShelf.keys()))           #copying all the names of keywords saved in it
    elif(sys.argv[1].lower()=='delete'):
        mcbShelf.clear()                                    #deleting all the names of keywords saved in it
    else:
        pyperclip.copied=str(mcbShelf[sys.argv[1]])         #copying the content corresponding tothe demanding keyword in command line which can later be pasted outside using normal operaration

mcbShelf.close()