class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(window_sum, max_sum)
        
        return max_sum / k





sol = Solution()

# nums = [1,12,-5,-6,50,3]
# k = 4
nums = [5]
k = 1 
# nums = [0,1,1,3,3]
# k = 4

print(sol.findMaxAverage(nums, k))