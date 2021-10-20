from itertools import combinations


class Solution(object):

    def all_comb(self, nums):
        n = len(nums)
        sums = []
        for n in range(len(nums)+1):
            comb = list(combinations(nums,n))
            for subl in comb:
                sums += [sum(subl)]
                # output = min(output, abs(sum(subl)-goal))
        return set(sums)


    def bfs(self, nums, goal):
        head, tail = 0, len(nums)
        while(True):
            n = (tail-head) // 2
            n = head + n
            if nums[n-1]<= goal and nums[n]>=goal:
                return n
            elif nums[0]>goal:
                return 0
            elif nums[-1]<goal:
                return tail-1

            if nums[n] < goal:
                head = n
            else:
                tail = n


    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        pos_sum = neg_sum = 0
        for e in nums:
            if e >0:pos_sum+=e
            else: neg_sum+=e

        if goal>0 and goal>=pos_sum:
            return goal-pos_sum
        elif goal<0 and goal<=neg_sum:
            return abs(goal-neg_sum)

        output =  10e9
        x = nums[:len(nums)//2]
        y = nums[len(nums)//2:]

        x_comb = self.all_comb(x)
        y_all_comb = self.all_comb(y)
        y_all_comb = sorted(y_all_comb)
        for x in x_comb:
            target = goal - x
            y_comb = y_all_comb
            n = self.bfs(y_comb, target)
            # print(y_comb, target, n)

            if n<=len(y_comb)-1:
                output = min(output, abs(target-y_comb[n]))
            if not n==0:
                output = min(output, abs(target-y_comb[n-1]))
            if output==0:break
        return output



nums = [5,-7,3,5]
goal = 6
## 0
nums = [7,-9,15,-2]
goal = -5 
## 1

nums = [1,2,3] 
goal = -7
Output: 7


nums = [9152249,8464156,-2493402,8990685,-7257152,-1050240,2243737,-82901,8939692]
goal = 26915229
Output: 8405



o = Solution().minAbsDifference(nums, goal)
print('output: ', o)
