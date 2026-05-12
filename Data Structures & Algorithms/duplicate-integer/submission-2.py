class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()

        for n in nums:
            if n not in hashtable:
                hashtable.add(n)
            elif n in hashtable:
                return True

        return False