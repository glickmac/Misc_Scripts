def extractEachKth(inputArray, k):
    index = []       
    z = [x for x in range(0,len(inputArray)) if (x+1)%k!=0]
    [index.append(inputArray[z[y]]) for y in range(len(z))]
    return(index)
