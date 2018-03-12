def matrixElementsSum(matrix):
    my_list = []
    
    ## Find Zeros in matrix
    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if l==0:
                my_list.append([i,k])
    
    mrow = len(matrix)
    mcol = len(matrix[0])
    
    
    ## Change Matrix values to remove numbers under zeros 
    for item in my_list:
        x, y = item
        
        if x+1 == mrow:
            continue
        else:
            for k in range(x, mrow):
                matrix[k][y] = 0
    
    ## Sum matrix 
    sums = sum(map(sum, matrix))
    
    return(sums)

