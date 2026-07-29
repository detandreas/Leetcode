from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """O(n) time and O(n) space."""

        quota = len(nums) // 2

        hashmap = defaultdict(int)
        for num in nums:

            hashmap[num] += 1

            if hashmap[num] > quota:
                return num
            
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Boyer-Moore Majority Voting Algorithm.
        O(n) runtime and O(1) space.

        Intuition:
        Majority element should appear more than N // 2 times,
        while all the other elements should appear in total less
        than N // 2 times.
        """

        candidate = None
        count = 0
        for num in nums:

            if count == 0:
                candidate = num
                count += 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1
        
        return candidate
    
        # Original algorithm requires to verify that candidate is actually a majority element by traversing the array one more time
        # and verifying that count > N // 2.
        # In our case problem description states that a majority element always exists.




nums = [3,2,3,3,2]
s = Solution()
print(s.majorityElement(nums))