# class Solution:
    # def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # """O(nlgn)"""
#
        # if len(numbers) == 2:
            # return [1, 2]
#
        # for i, candidate in enumerate(numbers):
            # complement = target - candidate
            # j = self.binary_search(numbers, complement, lo = i + 1)
            # if j != -1 :
                # return [i + 1, j + 1]
#
        # return [-1, -1]
#
    # def binary_search(self, arr: list[int], target: int, lo: int | None = None, hi: int | None = None) -> int:
        # """
        # lo, hi is inclusive,
        # """
#
        # if lo is None:
            # lo = 0
        # if hi is None:
            # hi = len(arr) - 1
#
        # while lo <= hi:
            # mid = lo + (hi - lo) // 2
#
            # if arr[mid] == target:
                # return mid
            # elif arr[mid] > target:
                # hi = mid -1
            # else:
                # lo = mid + 1
#
        # return  -1

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """O(n)"""

        if len(numbers) == 2:
            return [1, 2]

        lo, hi = 0, len(numbers) - 1

        while lo <= hi:

            local_sum = numbers[lo] + numbers[hi]

            if local_sum == target:
                return [lo + 1, hi + 1]
            elif local_sum > target:
                hi -= 1
            else:
                lo += 1

        return [-1, -1]


numbers = [1, 2, 3]
target = 10
s = Solution()
print(s.twoSum(numbers, target))