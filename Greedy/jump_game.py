class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """Optimized for early exit"""

        target = len(nums) - 1
        max_reach = 0
        for i in range(len(nums) - 1):

            if i > max_reach:
                return False
            
            reach = i + nums[i]
            if reach > max_reach:
                max_reach = reach
                if max_reach >= target:
                    return True
        
        return target <= max_reach

#s = Solution()
#nums = [3,2,1,0,4]
#nums = [2,3,1,1,4]
#nums = [1,1,1,1,4]
#print(s.canJump(nums))

class Solution:
    def canJump(self, nums: list[int]) -> bool:

        max_reach = 0
        for i in range(len(nums)):

            if i > max_reach:
                return False
            
            reach = i + nums[i]
            if reach > max_reach:
                max_reach = reach
        
        return True
    
s = Solution()
nums = [3,2,1,0,4]
#nums = [2,3,1,1,4]
#nums = [1,1,1,1,4]
print(s.canJump(nums))