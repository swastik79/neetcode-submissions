class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if len(nums) == 1:
            return 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                continue
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1
            else:
                min_jump = float("inf")
                for j in range(i + 1, i + nums[i] + 1):
                    if dp[j] != 0:
                        min_jump = min(min_jump, dp[j])
                dp[i] = 1 + min_jump
        
        return dp[0]
