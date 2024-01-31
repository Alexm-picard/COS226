def maximum(data, prevMax):
    nextNum = data.pop()
    if(len(data) == 0):
        return prevMax
    if(nextNum > prevMax):
        return maximum(data, nextNum)
    else:
        return maximum(data, prevMax)

data = [1,2,3,4,1,2,3,6,3,7,234,234,54,764]
prevMax = 0
dataMax = maximum(data, prevMax)
print(dataMax)