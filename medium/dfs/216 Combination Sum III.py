
class Solution:
    def combinationSum3(self, k: int, n: int):
        cand = list(range(1, 10))
        ans = []

        def dfs(eles, n, start):
            if n==0 and len(eles)==k:
                ans.append(eles)
                return
            if len(eles)>=k or n<0: return

            for i in range(start, 9):
                s = n - cand[i]
                if s<0:break
                dfs(eles+[cand[i]], s, i+1)

        dfs([], n, 0)
        return ans


class Solution:
    def combinationSum3(self, k: int, n: int):
        cand = list(range(1, 10))
        tail = 9
        ans = []

        def dfs(eles, n, start):
            if n==0 and len(eles)==k:
                ans.append(eles)

            if n<0 or len(eles)>=k:
                return

            for i in range(start, tail):
                remain = n - cand[i]
                if remain<0: break
                dfs(eles+[cand[i]], remain, i+1) 


        dfs([], n, 0)
        return ans


k = 3
n = 7
print('Output', Solution().combinationSum3(k, n))
# Output: [[1,2,4]]
# 1 + 2 + 4 = 7
# There are no other valid combinations.

k = 3
n = 9
print('Output', Solution().combinationSum3(k, n))
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.

k = 4
n = 1
print('Output', Solution().combinationSum3(k, n))
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
