class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        prefix_sum = [1] * n 
        suffix_sum = [1] * n

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] * nums[i-1]
        
        print(f"{prefix_sum=}")

        for i in range(n-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] * nums[i+1]

        print(f"{suffix_sum=}")
        
        answer = []
        for i in range(n):
            product = prefix_sum[i] * suffix_sum[i]
            answer.append(product)
        
        return answer
    
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Για κάθε θέση `i` χωρίζουμε το γινόμενο σε 2 μέρη.
        1. Το γινόμενο όλων των αριθμών αριστερά του i.
        2. Το γινόμενο όλων των αριθμών δεξιά του i.

        Ιδιαίτερο είναι επίσης οτι κατασκευάζουμε τον πίνακα answer σε 2 pass.
        n = len(nums).
        Στο 1ο pass υπολογίζουμε το γινόμενο nums[0] * nums[1] * nums[i-1]
        Στο 2ο pass υπολογίζουμε το γινόμενο nums[i+1] * nums[i+2] * nums[n-1]

        Complexity:
        Time complexity O(n).
        Space complexity O(1).
        """

        n = len(nums)   
        answer = [1] * n
        prefix_prod = 1
        for i in range(n):

            answer[i] *= prefix_prod
            prefix_prod *= nums[i]

        suffix_prod = 1
        for i in range(n - 1, -1, -1):

            answer[i] *= suffix_prod
            suffix_prod *= nums[i]
            
        return answer


s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))
