
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''

        for i in range(len(s)):
            # odd 'aba'
            res = self.helper(i, i, s)
            if len(res) > len(ans):
                ans = res
            
            #even 'abba'
            res = self.helper(i,i+1, s)
            if len(res) > len(ans):
                ans = res
        return ans

    def helper(self, l, r, s):
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        return  s[l+1:r]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        self.s = s 
        self.l = len(s)
        for i in range(self.l):
            ans = max(self.helper(i, i), ans, key=len)
            
            ans = max(self.helper(i, i+1), ans, key=len)

        return ans

    def helper(self, s, e):
        while(s>=0 and e<self.l and self.s[s]==self.s[e]):
            s-=1
            e+=1

        return self.s[s+1:e]
        
            




s = "babad"
# Output: "bab"
# "aba" is also a valid answer.
print(Solution().longestPalindrome(s))


s = "cbbd"
# Output: "bb"
print(Solution().longestPalindrome(s))


s = "a"
# Output: "a"
print(Solution().longestPalindrome(s))


s = "ac"
# Output: "a"
print(Solution().longestPalindrome(s))
