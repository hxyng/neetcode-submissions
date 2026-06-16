class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 0 indexed
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
                continue
            if total > target:
                right -= 1
                continue
            
            if total == target:
                return [left + 1, right + 1]
        
        left, right = left + 1, right + 1