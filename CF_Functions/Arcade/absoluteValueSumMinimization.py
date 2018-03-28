def absoluteValuesSumMinimization(a):
'''Takes a list of numbers and returns the value of x that when subtracted from the absolute value of all items in the list will return the smallest sum'''
    if len(a)%2==0:
        return(a[(len(a)//2)-1])
    return(numpy.median(a))


