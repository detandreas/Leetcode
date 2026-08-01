class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """O(n^2) time complexity."""
        n = len(gas)
        for i, g in enumerate(gas):

            if g < cost[i]:
                continue

            tank = g
            j = (i + 1) % n
            while j != i:
                tank = tank - cost[j-1] + gas[j]

                if tank < cost[j]:
                    break

                j = (j + 1) % n
            
            if j == i:
                return i
        
        return -1

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        O(n) time complexity

        1st run to find the starting gas station,
        2nd run to verify that the path is valid.
        """

        n = len(gas)
        start = None
        tank = 0
        location = 0
        while location < 2 * n:

            if start is None:
                start = location
            
            tank += gas[location % n] - cost[location % n]

            if tank < 0:
                start = None
                tank = 0
            
            location += 1

            if start is not None and location - start == n:
                return location % n
        
        return -1

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        O(n) time complexity.

        Χωρίς 2n loop wrap around pass.
        το start που μένει στο τέλος του single pass είναι εγγυημένα το global minimum σημείο του prefix sum.
        """
        n = len(gas)
        total_tank = 0
        tank = 0
        start = 0

        for i in range(n):
            diff = gas[i] - cost[i]
            total_tank += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_tank >= 0 else -1
        


            

s = Solution()
#gas = [1,2,3,4,5]
#cost = [3,4,5,1,2]
gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))