class Solution:
    def jump(self, nums: list[int]) -> int:
        """Greedy algorithm O(n) time O(1) space"""
        
        target = len(nums) - 1
        if target == 0:
            return 0
        
        current_end = 0
        max_reach = 0
        jumps = 0
        for i in range(len(nums) - 1):
            
            max_reach = max(max_reach, i + nums[i])

            if i == current_end:
                current_end = max_reach
                jumps += 1

                if current_end >= target:
                    return jumps
            
s = Solution()
nums = [2,3,1,1,4]
#nums = [2,3,0,1,4]
#nums = [2,0,2,1,4]
#nums = [1,1,1,1]
#nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]

print(s.jump(nums))

#from collections import defaultdict, deque
#import sys
#
#class Solution:
#    """
#    Jump game modeled II as a graph.
#
#    O(n^2) time.
#    """
#    def create_graph(self, nums: list[int]) -> dict[int, list[int]]:
#        g = defaultdict(list)
#        for i in range(len(nums) - 1):
#            v = nums[i]
#            for j in range(1 + i, min(i + v + 1, len(nums))):
#                g[(v, i)].append((nums[j], j))
#        
#        return g
#
#    def jump(self, nums: list[int]) -> int:
#        
#        n = len(nums)
#        if n == 1:
#            return 0
#        
#        q = deque()
#        g = self.create_graph(nums)
#        print(g)
#        target = (nums[n - 1], n-1)
#        dist = defaultdict(lambda: sys.maxsize)
#        visited = defaultdict(bool)
#
#        q.appendleft((nums[0], 0))
#        dist[(nums[0], 0)] = 0
#        while q:
#            curr, i = q.pop()
#            visited[(curr, i)] = True
#            print(f"Visiting {(curr, i)}")
#            for adj, j in g[(curr, i)]:
#                
#                print(f"Adjacent {(adj, j)}")
#                if not visited[(adj, j)]:
#                    q.appendleft((adj, j))
#
#                if dist[(adj, j)] > dist[(curr, i)] + 1:
#                    dist[(adj, j)] = dist[(curr, i)] + 1
#                
#                if (adj, j) == target:
#                    return dist[(adj, j)]
#

#s = Solution()
#nums = [2,3,1,1,4]
#nums = [2,3,0,1,4]
#nums = [2,0,2,1,4]x
#print(s.jump(nums))


class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Dynamic programming.

        O(n^2) time O(n) space
        """
        n = len(nums)
        if n == 1:
            return 0
        
        INF = float('inf')
        dp = [INF] * n
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == INF:
                continue
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)
        
        return dp[n - 1]