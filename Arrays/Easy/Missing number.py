def missingNumber(self, nums: List[int]) -> int:
    '''
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
    '''


    l = len(nums) 
    return l*(l+1)//2 - sum(nums)
