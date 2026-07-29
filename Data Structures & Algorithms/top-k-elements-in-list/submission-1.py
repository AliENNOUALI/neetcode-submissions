class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [ [] for i in range(len(nums)+1) ]
        for num in nums:
            res[num] = 1 + res.get(num,0)
        for n,c in res.items():
            freq[c].append(n)

        df = []
        for i in range(len(freq)-1,0,-1):
            for s in freq[i]:
                df.append(s)
                if len(df) == k:
                    return df