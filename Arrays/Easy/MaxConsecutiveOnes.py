
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    maxOnes = 0
    c = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            c += 1
        if maxOnes < c:
            maxOnes = c
        if nums[i] != 1:
            c = 0

    return maxOnes
