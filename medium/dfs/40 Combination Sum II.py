

class Solution:
    def combinationSum2(self, candidates, target: int):
        ans = []
        candidates.sort()

        def dfs(eles, target, i):
            if not target: 
                ans.append(eles)
                return  
            if target<0: return
                
            for e in range(i, len(candidates)):
                if e>i and candidates[e]==candidates[e-1]:
                    continue
                if target-candidates[e]<0:
                    break   
                dfs(eles+[candidates[e]], target-candidates[e], e+1)

        dfs([], target, 0)
        return ans


candidates =  [10,1,2,7,6,1,5]
target = 8
# Output: [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
print("Output :", Solution().combinationSum2(candidates, target))


candidates =  [2,5,2,1,2]
target = 5
# Output: [
# [1,2,2],
# [5]
# ]
print("Output :", Solution().combinationSum2(candidates, target))
