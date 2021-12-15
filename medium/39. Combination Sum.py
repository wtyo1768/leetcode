

class Solution:
    def combinationSum(self, candidates, target: int):
        ans = []
        tail = len(candidates)
        # candidates.sort()

        def dfs(eles, target, i):
            print(candidates[i:])
            if target==0:
                ans.append(eles)
                return
            # if target<0: return
            for e in range(i, tail):
                if target>0:
                    dfs(eles+[candidates[e]], target-candidates[e], e)

        dfs([], target, 0)
        return ans


candidates = [7,3,6, 2]
target = 7
print("Output :", Solution().combinationSum(candidates, target))
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.


candidates = [5,2,3]
target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
print("Output :", Solution().combinationSum(candidates, target))


candidates = [2]
target = 1
# Output: []
print("Output :", Solution().combinationSum(candidates, target))


candidates = [1]
target = 1
# Output: [[1]]
print("Output :", Solution().combinationSum(candidates, target))


candidates = [1]
target = 2
# Output: [[1,1]]
print("Output :", Solution().combinationSum(candidates, target))
