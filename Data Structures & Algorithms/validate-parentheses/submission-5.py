class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        hashmap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        if len(s) == 0:
            return False

        for c in s:
            # check closing parentheses
            if c in hashmap:
                if not stack:
                    return False
                
                val = stack.pop()

                if val != hashmap[c]:
                    return False
                
            
            # add beginning parentheses
            else:
                stack.append(c)
        
        # keep popping until len is 0
        return len(stack) == 0