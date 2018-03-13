def arrayChange(inputArray):
    copy = inputArray
    delta = 0
    value = 0
    for item in range(0, len(copy)-1):
        if copy[item] >= copy[item+1]:
            delta = copy[item] - copy[item+1] + 1
            value += copy[item] - copy[item+1] + 1
            copy[item+1] = copy[item+1] + delta
            
    
    return(value)
