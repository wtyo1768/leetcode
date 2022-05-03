












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




class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0
        self.s = s
        self.l = len(s)

        for i in range(0, self.l):
            # if i%2==0:
            self.helper(i, i+1)
            self.helper(i, i)

        return self.ans


    def helper(self, s, e):
        while(s>=0 and e<self.l and self.s[s]==self.s[e]):
            s-=1
            e+=1
            self.ans+=1


s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
print('Output :', Solution().countSubstrings(s))


s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa". 
print('Output :', Solution().countSubstrings(s))