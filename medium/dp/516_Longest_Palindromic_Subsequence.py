



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_len = len(s)
        dp=[[0]*s_len for _ in range(s_len)]
        
        for i in range(s_len-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, s_len):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][s_len-1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        
        prev_dp = [0] * l

        for i in range(l-1, -1, -1):
            
            dp = [0] * l 
            dp[i] = 1
            for j in range(i+1, l):
                
                if s[i]==s[j]:                         
                    dp[j] = prev_dp[j-1] + 2
                else:
                    dp[j] = max(prev_dp[j], dp[j-1])
            # print('-------')
            # print(dp)
            # print(prev_dp)
            # dp, prev_dp = prev_dp, dp
            prev_dp = dp
        #因最後的loop有交換 所以再換回來
        return prev_dp[-1]


s = "bbbab"
# Output: 4
print('Output :', Solution().longestPalindromeSubseq(s))
# Explanation: One possible longest palindromic subsequence is "bbbb".



s = "cbbd"
# Output: 2
print('Output :', Solution().longestPalindromeSubseq(s))
# Explanation: One possible longest palindromic subsequence is "bb".
