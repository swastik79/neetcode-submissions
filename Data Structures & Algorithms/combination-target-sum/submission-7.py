class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if sum(subset) > target or i >= len(nums):
                return
            else:
                subset.append(nums[i])
                backtrack(i, subset)
                subset.pop()
                backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res    
        