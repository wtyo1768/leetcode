

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        bond, tail = len(haystack), len(needle)
        if tail==0:  return 0
        if bond==0: return -1
        
        for i in range(bond):
            if i+tail>bond:break
            j = 0
            while(haystack[i]==needle[j]):
                i+=1
                j+=1
                if j==tail: return i-tail

        return -1



haystack = "hello"
needle = "ll"
print('Output', Solution().strStr(haystack, needle))
# Output: 2

haystack = "aaaaa"
needle = "bba"
print('Output', Solution().strStr(haystack, needle))
# Output: -1

haystack = ""
needle = ""
print('Output', Solution().strStr(haystack, needle))
# Output: 0
