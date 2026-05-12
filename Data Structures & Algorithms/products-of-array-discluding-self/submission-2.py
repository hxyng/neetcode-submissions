class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length

        for i in range(length):
            product = 1
            for j in range(length):
                if i == j:
                    continue
                product = nums[j] * product
            result[i] = product
        
        return result


