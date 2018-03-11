def makeArrayConsecutive2(statues):
    verts = list(range(min(statues),max(statues)+1))
    temp3 = list(set(verts) - set(statues))
    return len(temp3)
