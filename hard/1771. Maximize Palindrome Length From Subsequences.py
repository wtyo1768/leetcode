class Solution:
    def longestPalindrome(self, word1, word2) -> int:
        l1, valid = len(word1), False
        s = word1 + word2
        res = 0
        s_len = len(s)
        dp=[[0]*s_len for _ in range(s_len)]    
        
        for i in range(s_len-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, s_len):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if i<l1 and j>=l1: res = max(res, dp[i][j])
                else:   
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return res


word1 = "cacb"
word2 = "cbba"
# Output: 5
# Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.
print('Output :', Solution().longestPalindrome(word1, word2))


word1 = "ab"
word2 = "ab"
# Output: 3
# Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which is a palindrome.
print('Output :', Solution().longestPalindrome(word1, word2))



word1 = "aa"
word2 = "bb"
# Output: 0
# Explanation: You cannot construct a palindrome from the described method, so return 0.
print('Output :', Solution().longestPalindrome(word1, word2))


word1 = "d"
word2 = "ece"   
# Output: 0
# Explanation: You cannot construct a palindrome from the described method, so return 0.
print('Output :', Solution().longestPalindrome(word1, word2))


word1 = "ceebeddc"
word2 = "d"
# Output: 3
print('Output :', Solution().longestPalindrome(word1, word2))



word1 = "afaaadacb"
word2 = "ca"
# Output: 6
print('Output :', Solution().longestPalindrome(word1, word2))
