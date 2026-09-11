class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmin, curmax= 0, 0
        globalmin, globalmax = nums[0], nums[0]
        total = 0

        for num in nums:
            curmin = min(curmin + num, num)
            curmax = max(curmax + num, num)
            total += num
            globalmin = min(curmin, globalmin)
            globalmax = max(curmax, globalmax)
        
        if globalmax > 0:
            return max(globalmax, total - globalmin)
        else:
            return globalmax