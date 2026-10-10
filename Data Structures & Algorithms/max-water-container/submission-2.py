

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0  , n-1
        s = set()
        while r > l:
            s.add((r-l)*min(heights[l],heights[r]))
            if min(heights[l],heights[r]) == heights[l]:
                l+=1
            else:
                r-=1
        return max(s)
                


            