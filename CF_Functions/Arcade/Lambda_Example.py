def isTestSolvable(ids, k):
    '''Splits an ID numeric and sums the string'''
    digitSum = lambda questionId: sum([int(i) for i in str(questionId)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
