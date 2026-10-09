class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = sorted(nums)
        n = len(x)
        count = 0
        hsh = {}
        seq = 0
        if n == 0:
            return 0
        for i in range(1,n):
            if x[i] == x[i-1] + 1:
                seq +=1
            elif x[i] == x[i-1]:
                continue
            else:
                hsh[count] = seq
                count+=1
                seq =0
        hsh[count] = seq
        return max(hsh.values()) + 1
            



        