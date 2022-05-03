
from numpy import linspace


class Solution:
    def longestPrefix(self, s):
        if len(s)==0: return ""
        lps = [0] * len(s)
        j, i = 0, 1

        while(i<len(s)):
            if s[i]==s[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j>0:
                    j=lps[j-1]
                else:
                    i+=1
        v = lps[-1]
        if v==0: return ""
        return s[-v:]


s = "level"
print('Output', Solution().longestPrefix(s))
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

s = "ababab"
print('Output', Solution().longestPrefix(s))
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
