class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #creates a dictionary that has a default value of a list

        for s in strs:
            binary = [0] * 26 #create list consisting 26 0s

            for c in s:
                binary[ord(c) - ord('a')] += 1 #increment index for char

            result[tuple(binary)].append(s) #binary key, append string in list

        return list(result.values()) # setting the result values to a list