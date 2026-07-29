class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """O(n^2) because of .pop() operation requires shifting."""

        i = 0
        length = len(nums)
        count = 1
        while i + 1 < length:

            if nums[i] == nums[i + 1]:
                count += 1
            else:
                count = 1
            
            if count > 2:
                nums.pop(i + 1)
                length -= 1
                continue
            
            l += 1
        
        return length


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """O(n) complexity"""

        if len(nums) <= 2:
            return len(nums)
        
        write = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        
        return write
    
    
s = Solution()
input = [0]
#input = [1,1,1,2,2,3]
print(s.removeDuplicates(input))
