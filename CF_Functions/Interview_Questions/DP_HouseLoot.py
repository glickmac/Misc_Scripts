def houseRobber(nums):
    if(len(nums) == 0):
        return 0
    if(len(nums) < 3):
        return max(nums)
    
    totals = [None]*len(nums)
    totals[-1] = nums[-1]
    totals[-2] = max(nums[-2:])
    for i in range(len(nums)-3,-1,-1):
        totals[i] = max(totals[i+2] + nums[i],totals[i+1])
    
    return max(totals)
