class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        O(n) time complexity
        O(n) space complexity
        """

        starting_points, hash_set = [], set(nums)

        for element in hash_set:
            if (element - 1) not in hash_set:
                starting_points.append(element)

        print(starting_points)

        max_seq = 0
        for start in starting_points:
            curr_seq_len = 1
            while start + 1 in hash_set:
                curr_seq_len += 1
                start += 1

            max_seq = max(max_seq, curr_seq_len)

        print(max_seq)
        return max_seq

class Optimized:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        O(n) time complexity
        O(n) space complexity
        """

        max_seq, hash_set = 0, set(nums)
        for element in hash_set:
            if (element - 1) not in hash_set:
                curr_seq = 1
                while element + 1 in hash_set:
                    curr_seq += 1
                    element += 1
                max_seq = max(max_seq, curr_seq)

        return max_seq

s = Solution()
nums = [100,4,200,1,3,2]
s.longestConsecutive(nums)