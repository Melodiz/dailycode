class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t): 
            flag = False
            for i in range(len(s)):
                if s[i]!=t[i] and flag: return False
                elif s[i]!=t[i]: flag = True
            return flag
        elif abs(len(s)-len(t)) > 1: return False
        else:
            for i in range(min(len(s), len(t))):
                if s[i]!=t[i]: 
                    if len(s) < len(t): 
                        for j in range(min(i+1, len(t)), len(s)):
                            if s[j]!=t[j+1]: return False
                        return True
                    else:
                        for j in range(min(i+1, len(t)), len(t)):
                            if s[j+1]!=t[j]: return False
                        return True
            return True    
    
solver = Solution()

def run_test(s, t, expected):
    output = solver.isOneEditDistance(s, t)
    print(f"Input: s='{s}', t='{t}'")
    print(f"Output: {output}, Expected: {expected} -> {'✅' if output == expected else '❌'}")
    print("-" * 20)

# Test Case 1: Replace operation
run_test(s="apple", t="apply", expected=True)

# Test Case 2: Insert operation
run_test(s="apple", t="apples", expected=True)

# Test Case 3: Delete operation
run_test(s="aple", t="apple", expected=True)

# Test Case 4: Identical strings
run_test(s="apple", t="apple", expected=False)

# Test Case 5: More than one edit (same length)
run_test(s="apple", t="axple", expected=True) # A single replace
run_test(s="apple", t="axpyl", expected=False) # Two replaces

# Test Case 6: More than one edit (different length)
run_test(s="a", t="abc", expected=False)

# Test Case 7: Empty string cases
run_test(s="", t="a", expected=True)
run_test(s="", t="", expected=False)

# Test Case 8: General false case
run_test(s="teacher", t="detacher", expected=False)
