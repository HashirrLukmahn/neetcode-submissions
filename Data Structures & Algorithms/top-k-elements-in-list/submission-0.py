class Solution:
    from collections import Counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        Frequency = Counter(nums).most_common(k)

        return list(map(lambda x: x[0], Frequency))