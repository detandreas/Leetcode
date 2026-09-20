class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        solutions = []
        targets = set()
        n = len(nums)

        for i, target in enumerate(nums):

            if target in targets:
                continue
            targets.add(target)

            if target > 0: break


            lo, hi = i+1, n - 1
            while lo < hi:
                localsum = nums[lo] + nums[hi]

                if localsum == - target:
                    solutions.append([target, nums[lo], nums[hi]])
                    lo += 1

                    while lo < hi and nums[lo] == nums[lo -1]:
                        lo += 1

                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi += 1

                elif localsum >  - target:
                    hi -= 1
                else:
                    lo += 1

        return solutions

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))