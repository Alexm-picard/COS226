def revString1(revString, stringRev = '', index = -1): #revString is the string to reverse and stringRev is the reversed string
    if(len(revString) == index * -1):
        print(revString)
        return stringRev + revString[0]
    else:
        return revString1(revString, stringRev + revString[index], index - 1)