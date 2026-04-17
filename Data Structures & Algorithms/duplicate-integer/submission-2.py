class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        noDuplicate = set(nums)

        return len(noDuplicate) != len(nums)
