def uniqueValue(unique, data):
    nextValue = data.pop()
    if(nextValue in unique): # if the next element isn't unique stop recussion
        print("Not all values in list are unique") 
        return False
    if(len(data) == 0): #if end of list end reccusion
        print("All values in list are unique")
        return True
    else: #calls the recussion and adds value to list of unique values
        unique.append(nextValue)
        return uniqueValue(unique, data)
unique = []
data = [1,1,2,3,4,5,6]
uniqueValue(unique, data)