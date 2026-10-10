class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        clear = sorted(nums)
        ls = []

        for i in range(len(clear)//2):

            l, r = i+1, len(clear)-1   
            while l < r:
                if (clear[l] + clear[r]) == - clear[i]:
                    if [clear[i],clear[l],clear[r]] not in ls:
                         ls.append([clear[i],clear[l],clear[r]])
                    l+=1
                    continue
                elif (clear[l] + clear[r]) < - clear[i]:
                    l += 1
                elif (clear[l] + clear[r]) > - clear[i]:
                    r -= 1
        return ls



        