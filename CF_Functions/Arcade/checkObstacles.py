def avoidObstacles(inputArray):
    '''Find difference between numbers jump by '''
    my_list = sorted(inputArray)
    count = 1
    found = False
    while not found:
        new_list = list(map(lambda x: x%count, inputArray))
        if 0 in new_list:
            count += 1
        else:
            return(count)
