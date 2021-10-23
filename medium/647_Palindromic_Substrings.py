



class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        for i in range(len(s)):
            # aba
            count = self.helper(i, i, s)
            ans += count
            # abba
            count = self.helper(i, i+1, s)
            ans += count
        return ans
    
    
    def helper(self, l, r, s):
        count = 0
        while(l>=0 and r<len(s) and s[l]==s[r]):
            r+=1
            l-=1
            count+=1
        return count


s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
print('Output :', Solution().countSubstrings(s))


s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa". 
print('Output :', Solution().countSubstrings(s))