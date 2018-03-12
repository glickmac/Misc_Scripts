def newRoadSystem(roadRegister):
    '''Checks if nodes have equal input and output edges in matrix'''   
    for i in range(len(roadRegister)):
        horizontal = roadRegister[i]
        vertical = [row[i] for row in roadRegister]
        if horizontal.count(True) != vertical.count(True):
            return(False)
    return(True)
