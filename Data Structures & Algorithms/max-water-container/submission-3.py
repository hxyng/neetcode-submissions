class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            
            h = min(heights[l], heights[r])
            w = r - l
            res = max(w*h, res)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l, r = l + 1, r - 1
            
        return res
            
