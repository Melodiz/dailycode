class Solution(object):
    def isIsomorphic(self, s, t):
        data = {}
        used = set()
        for i in range(len(s)):
            if not data.get(s[i], 0):
                if t[i] in used:
                    return False
                data[s[i]] = t[i]
                used.add(t[i])
            elif data[s[i]]!= t[i]:
                return False
        return True
    

print(Solution.isIsomorphic(Solution, "badc", "baba"))