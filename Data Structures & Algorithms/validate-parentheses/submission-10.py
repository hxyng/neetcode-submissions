class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        pairs = {
            ")" : "(", 
            "}" : "{", 
            "]" : "["
        }

        for c in s:
            if c in pairs:
                if not stack:
                    return False
                
                # make sure that char c is in pairs, then pop
                val = stack.pop()
                
                if val != pairs[c]:
                    return False
            

            # add opening c to stack
            else:
                stack.append(c)
        
        return len(stack) == 0