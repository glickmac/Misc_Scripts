def roadsBuilding(cities, roads):
    ## Process roads, move larger number to second position
    for item in roads:
        if item[0]>item[1]:
            item[0], item[1] = item[1], item[0]
            
    ## Find all permutations
    my_list = []
    for i in range(cities):
        for j in range(i+1, cities):
            k = [i,j]
            my_list.append(k)
            
    ## Compare lists
    new_roads = []
    for z in my_list:
        if z not in roads:
            new_roads.append(z)
    
    
    return(new_roads)
