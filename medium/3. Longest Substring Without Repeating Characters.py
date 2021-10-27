
# Straightforward solution  
class Solution:   
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l==0: return 0

        ans, record = 1, {s[0]}
        count = 1
        for i in range(0, l):
            ans = max(ans, count)
            record = {s[i]}
            count = 1
            while(i+1<l): 
                if s[i+1] in record: break
                else:
                    count+=1
                    record.add(s[i+1])
                i+=1

        return max(ans, count)




s = "abcabcbb"
print('Output :', Solution().lengthOfLongestSubstring(s))
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


s = "bbbbb"
print('Output :', Solution().lengthOfLongestSubstring(s))
# Output: 1
# Explanation: The answer is "b", with the length of 1.


s = "pwwkew"
print('Output :', Solution().lengthOfLongestSubstring(s))
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


s = "au"
print('Output :', Solution().lengthOfLongestSubstring(s))
# Output: 3
