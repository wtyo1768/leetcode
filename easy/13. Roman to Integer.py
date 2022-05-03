

class Solution:
    def romanToInt(self, s: str) -> int:
        d = { 
        'I':1,'V':5,'X': 10,'L': 50,'C':  100,'D': 500,'M':1000
        }
        ans = 0

        for i in range(len(s)):
            if i+1<len(s) and d[s[i]]<d[s[i+1]]:
                ans-=d[s[i]]
            else:
                ans+=d[s[i]]

        return ans


s = "IV"
print('Output', Solution().romanToInt(s))
# Output: 4

s = "III"
print('Output', Solution().romanToInt(s))
# Output: 3
# Explanation: III = 3.

s = "LVIII"
print('Output', Solution().romanToInt(s))
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

s = "MCMXCIV"
print('Output', Solution().romanToInt(s))
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
