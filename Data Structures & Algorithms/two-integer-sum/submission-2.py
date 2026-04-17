class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, k in enumerate(nums):
            n2 = target - nums[i]
            
            if n2 in seen:
                if i < seen[n2]:
                    return [i, seen[n2]]
                else:
                    return [seen[n2], i]

            seen[k] = i

        return []

