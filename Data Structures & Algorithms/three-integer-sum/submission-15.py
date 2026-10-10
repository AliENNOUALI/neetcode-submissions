class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        clear = sorted(nums)
        ls = []

        for i in range(len(clear)//2):
            if clear[i] == clear[i-1] and i > 0:
                continue 

            l, r = i+1, len(clear)-1   
            while l < r:
                if (clear[l] + clear[r]) == - clear[i]:
                    ls.append([clear[i],clear[l],clear[r]])
                    l+=1
                    while clear[l] == clear[l-1] and l<r:
                        l+=1
                elif (clear[l] + clear[r]) < - clear[i]:
                    l += 1
                    while clear[l] == clear[l-1] and l<r:
                        l+=1
                elif (clear[l] + clear[r]) > - clear[i]:
                    r -= 1
        return ls



        