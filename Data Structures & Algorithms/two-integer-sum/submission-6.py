class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for key, value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                return [hashmap[difference], key]
            if value not in hashmap:
                hashmap[value] = key

        return 