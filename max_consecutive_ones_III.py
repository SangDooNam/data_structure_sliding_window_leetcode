class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        left, zeros_count, max_lenght = 0, 0, 0
        
        for right in range(len(nums)):
            
            if nums[right] == 0:
                zeros_count += 1
            
            
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            max_lenght = max(max_lenght, right - left + 1)
        
        return max_lenght
                


sol = Solution()

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3 

print(nums[:4])
# print(sol.longestOnes(nums, k))