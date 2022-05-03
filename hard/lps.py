
class Solution:
    def lps(self, s):
        j, i = 0, 1
        lps = [0] * len(s)

        while(i<len(s)):
            if s[i]==s[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j>0: j=lps[j-1]
                else:
                    i+=1   
                    j=0
        print(lps)  
        return lps[-1]


s = "acccbaaacccbaac"
print('Output', Solution().lps(s))

s = "ababab"
print('Output', Solution().lps(s))
