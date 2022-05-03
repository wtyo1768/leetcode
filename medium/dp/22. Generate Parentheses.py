

class Solution:
    def generateParenthesis(self, n: int):
        ans=[]

        def helper(l, r, out):
            if l==0:
                ans.append(out + ')'*r)
                return    
            helper(l-1, r, out+'(')
            if r>l: helper(l, r-1, out+')')
        helper(n, n, '')
        return ans

n = 3
print('Output :', Solution().generateParenthesis(n))
# Output: ["((()))","(()())","(())()","()(())","()()()"]


n = 1
print('Output :', Solution().generateParenthesis(n))
# Output: ["()"]

 

