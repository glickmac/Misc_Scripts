def allLongestStrings(inputArray):
    my_list = []
    max = 0
    for item in inputArray:
        item_length = len(item)
        if item_length >= max:
            max = item_length
    for item in inputArray:
        if len(item) == max:
            my_list.append(item)
    return(my_list)
