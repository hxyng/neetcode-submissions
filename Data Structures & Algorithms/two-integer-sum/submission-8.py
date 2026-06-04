class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if n not in hashmap:
                hashmap[diff] = i
            if n in hashmap and hashmap[n] != i:
                return [hashmap[n], i]
            

