def centuryFromYear(year):
    remainer = year % 100
    if remainer == 0:
        return year/100
    else:
        return int(year/100)+1
