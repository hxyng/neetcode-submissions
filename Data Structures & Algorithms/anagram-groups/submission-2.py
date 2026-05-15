class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        '''
        defaultdict(<class 'list'>, {'act': ['act', 'cat'], 
        'opst': ['pots', 'tops', 'stop'], 
        'aht': ['hat']})
        '''

        for s in strs:
            sortedS = ''.join(sorted(s))

            groups[sortedS].append(s)

        return list(groups.values())
