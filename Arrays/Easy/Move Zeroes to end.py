def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    c = nums.count(0)
    while 0 in nums:
        nums.remove(0)
    nums += [0]*c
