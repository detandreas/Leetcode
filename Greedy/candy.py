class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        O(n) time complexity.
        O(n) space complexity.
        """
        
        n = len(ratings)
        left_to_right = [1] * n
        right_to_left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_to_right[i] = left_to_right[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right_to_left[i] = right_to_left[i+1] + 1

        candies = sum(max(left, right)
                      for left, right in zip(left_to_right, right_to_left))

        return candies


s = Solution()
#ratings = [1,0,2]
ratings = [1,2,3,4,3,2,1]
print(s.candy(ratings))