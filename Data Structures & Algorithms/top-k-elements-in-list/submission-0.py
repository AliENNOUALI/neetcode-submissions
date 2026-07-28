class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num,0)
        sorted_keys = sorted(res.keys(), key = lambda x: res[x], reverse = True)

        return sorted_keys[:k]