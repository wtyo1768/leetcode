
class Solution:
    def combinationSum2(self, candidates, target: int):
        ans = []
        tail = len(candidates)
        candidates.sort()

        def dfs(eles, target, start):
            if target<0:
                return
            if target==0:
                ans.append(eles)
                return

            for i in range(start, tail):
                ## 一直錯!
                # if i>0 and candidates[i-1]==candidates[i]:
                if i>start and candidates[i-1]==candidates[i]:  
                    continue
                remain = target - candidates[i]
                if remain<0: break
                dfs(eles+[candidates[i]], remain, i+1)

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
