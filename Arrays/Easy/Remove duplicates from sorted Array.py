# Unoptimized code

def removeDuplicates(self, nums: List[int]) -> int:
    start = 0
    end = 0
    for i in range(len(nums)-1):
        if nums[i] not in nums[i+1:]:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1
    if nums[start] < nums[-1]:
        nums[start], nums[-1] = nums[-1], nums[start]
    return start + 1

# Another method

def removeDuplicates(self, nums: List[int]) -> int:
    s = list(set(nums))
    s.sort()
    for i in range(len(s)):
        nums[i] = s[i]
    return len(s) 

# another method

def removeDuplicates(self, nums: List[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)
