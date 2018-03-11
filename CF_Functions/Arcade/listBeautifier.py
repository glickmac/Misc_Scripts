def listBeautifier(a):
'''
For a = [3, 4, 2, 4, 38, 4, 5, 3, 2], the output should be
listBeautifier(a) = [4, 38, 4]
'''

    res = a[:]
    while res and res[0] != res[-1]:
        first, *res, last = res
    return res
