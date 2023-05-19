def check(self, nums: List[int]) -> bool:
    c = 0
    for i in range(len(nums)):
        if nums[i] > nums[i-1]:
            continue
        elif nums[i] < nums[i-1]:
            if c > 1:
                return False
            c += 1
    if c <= 1:
        return True
