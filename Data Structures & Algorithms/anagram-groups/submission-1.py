class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #creates a dictionary that has a default value of a list

        for s in strs:
            count = [0] * 26 #create list consisting 26 0s

            for c in s:
                count[ord(c) - ord('a')] += 1 #increment index for char

            result[tuple(count)].append(s) #count key, append string in list

        return list(result.values()) # setting the result values to a list