class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            
            # val : index
            hashmap = {}

            # target - n = a number in hashmap, 
            # return indecies, else keep going

            for i, n in enumerate(nums):
                diff = target - n

                if diff in hashmap:
                    # return index of first, then second
                    if hashmap[diff] != i:
                        return [hashmap[diff],i]

                hashmap[n] = i