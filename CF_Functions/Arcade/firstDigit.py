def firstDigit(inputString):
    import re
    ## Find all digits
    m = re.search("\d", inputString)
    ## Use group to return found item and start to return index in string
    return(m.group())
