class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [0] * l2
        for i in range(1, l1):
            prev = dp[0]
            for j in range(1, l2):
                tmp = dp[j]
                if word1[i-1] == word2[j-1]:
                    prev += 1
                    dp[j] = prev
                    # dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[j] = max(dp[j-1], dp[j])
                    # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                prev = tmp  

        return l1-1-dp[-1] + l2-1-dp[-1]



word1 = "sea"
word2 = "eat"
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
print('Output :', Solution().minDistance(word1, word2))
# Output: 2

word1 = "leetcode"
word2 = "etco"
# Output: 4
print('Output :', Solution().minDistance(word1, word2))
