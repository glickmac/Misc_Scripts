def firstDuplicate(a):
    oldies={}
    notfound=True
    for i in range(len(a)):
        try:
            if oldies[a[i]]==a[i]:
                notfound=False
                return a[i]     
        except:
            oldies[a[i]]=a[i]
    if notfound:
        return -1  
