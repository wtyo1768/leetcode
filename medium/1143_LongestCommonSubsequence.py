class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        l1, l2 = len(text1)+1, len(text2)+1
        dp = [0] * l2
        for i in range(1, l1):
            prev = dp[0]
            for j in range(1, l2):
                tmp = dp[j]
                if text1[i-1] == text2[j-1]:
                    prev += 1
                    dp[j] = prev
                    # dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[j] = max(dp[j-1], dp[j])
                    # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                prev = tmp
        return dp[-1]


text1 = "abcde"
text2 = "ace" 
# Output: 3  
print('Output :', Solution().longestCommonSubsequence(text1, text2))


text1 = "abc"
text2 = "abc"
# Output: 3  
print('Output :', Solution().longestCommonSubsequence(text1, text2))


text1 = "abc"
text2 = "def"
# Output: 0
print('Output :', Solution().longestCommonSubsequence(text1, text2))