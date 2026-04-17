class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}

        for i,n in enumerate(nums):
            dup[n] = i

        if (len(dup) == len(nums)):
            return False
        else:
            return True
    
