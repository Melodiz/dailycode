class Solution:
    def addSpaces(self, s: str, spaces) -> str:
        result = []
        last_space = 0
        
        for space in spaces:
            result.append(s[last_space:space])
            result.append(' ')
            last_space = space
        
        result.append(s[last_space:])
        
        return ''.join(result)