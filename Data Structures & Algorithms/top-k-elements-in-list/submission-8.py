class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        k_left = k
        result = []

        for n in nums:
            if n in frequency:
                frequency[n] += 1
            if n not in frequency:
                frequency[n] = 1
        
        frequencies = []

        for n, f in frequency.items():
            frequencies.append([f,n])

        sorted_freq = sorted(frequencies)
        # [[freq,num], ...]
        
        while len(result) < k:
            result.append(sorted_freq.pop()[1])
        return result