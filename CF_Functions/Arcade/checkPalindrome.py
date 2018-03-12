def checkPalindrome(inputString):
'''
Checks if string input is a palindrome (same forwards and backwards
'''
    back = inputString[::-1]
    if inputString==back:
        return True
    else:
        return False
