

def quickSort( nums):
    def helper(head, tail):
        if head >= tail: return 
        l, r = head, tail
        m = (r + l) // 2
        pivot = nums[m]
        while r >= l:
            while r >= l and nums[l] < pivot: l += 1
            while r >= l and nums[r] > pivot: r -= 1
            if r >= l:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        print(head, m, tail, nums)
        helper(head, r)
        helper(l, tail)

    helper(0, len(nums)-1)
    return nums


arr = [10, 80, 30, 90, 40, 50, 70]
quickSort(arr)
print(arr)

arr = [12, 11, 13, 5, 6, 7]
quickSort(arr)
print(arr)