class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        O(n^2) because insert(0, item) requires shifting the whole list.
        """
        for _ in range(k):
            item = nums.pop()
            nums.insert(0, item)

#s = Solution()
#nums = [1,2,3,4,5,6,7]
#k = 7
#s.rotate(nums, k)
#print(nums)
    
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        O(n) time and O(1) space.
        """
        
        def reverse(lst: list, l: int, r: int):
            
            while l < r:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1

        n = len(nums)
        k = k % n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

from math import gcd

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        O(n) time and O(1) space.
        
        The permutation of every element of the list nums is described by the mapping:
        i -> (i + k) % n, where n = len(nums)

        In every nested iteration you find the final position of the element that the variable prev holds.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return

        cycles = gcd(n, k) # Προκύπτει απο σύνθετη θεωρία αριθμών γιατί δουλεύει αυτό.
        for start in range(cycles):
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                if current == start:
                    break
    


s = Solution()
nums = [1,2,3,4,5,6,7, 8, 9]
k = 5
s.rotate(nums, k)
print(nums)