class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l, zero_count, max_lenth = 0, 0, 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            
            max_lenth = max(max_lenth, r - l)
            
        return max_lenth

sol = Solution()

nums = [0,1,1,1,0,1,1,0,1] 
# nums = [1,1,0,1] 
# nums = [1,1,1]

print(sol.longestSubarray(nums))