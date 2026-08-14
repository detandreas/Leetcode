"""
Υπολογίζεις το παγιδευμένο νερό σε κάθε θέση του πίνακα,το οποίο προκύπτει ως εξής:
για κάποια θέση i trapped_water = min(max_left, max_right) - height[i]
βλ. σχήμα Το πόσο νερό παγιδεύεται σε μια θέση ορίζεται απο το μικρότερο όριο (bound) ανάμεσα στο αριστερό και δεξί όριο
ώστε να μην ξεχυλίζει το νερό.
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        """O(n) time complexity and O(n) space complexity."""
        n = len(height)
        max_left = [0] * n
        curr_max = height[0]
        for i in range(1, n):
            max_left[i] = curr_max
            curr_max = max(curr_max, height[i])
        
        max_right = [0] * n
        curr_max = height[-1]
        for i in range(n-2, -1, -1):
            max_right[i] = curr_max
            curr_max = max(curr_max, height[i])

        total = 0
        for i in range(n):
            trapped_water = min(max_left[i], max_right[i]) - height[i]
            if trapped_water > 0:
                total += trapped_water
        
        return total

class Solution:
    def trap(self, height: list[int]) -> int:
        """
        O(n) time complexity and O(1) space complexity.
        two-pointers approach.
        Δεν είναι ανάγκη να ξέρεις τα πραγματικά max_left, max_right γιατί για παράδειγμα αν 
        max_left <= curr_max_right (αυτού που έχεις εως τώρα υπολογίσει, όχι του πραγματικού),
        τότε σίγουρα max_left <= max_right(του πραγματικού) αφού max_left <= curr_max_right <= max_right.
        π.χ για height = [0,1,0,2,1,0,1,3,2,1,2,1] l = 0, r = 11
        max_left = 0, max_right = 1
        max_left <= max_right => l = 1
        Τώρα πρέπει να βρώ το ελάχιστο boundary ώστε να διαφυλαχτεί το νερό δηλαδή το min(max_left, max_right)
        Το πραγματικό max_right είναι 3 αλλά δεν χρειάζεται να το βρώ αφου max_left = 0 < max_right = 1
        Κάνω τον υπολογισμό max_left = 0, height[l] = 1: max_left - height[l] = -1, άρα δεν αποθηκεύεται νερό στην θέση l=1.
        """
        n = len(height)
        l, r = 0, n-1
        max_left, max_right = height[0], height[-1]
        total = 0
        while l < r:
            if max_left <= max_right:
                l += 1
                trapped_water = max_left - height[l]
                max_left = max(max_left, height[l])
            else:
                r -= 1
                trapped_water = max_right - height[r]
                max_right = max(max_right, height[r])

            if trapped_water > 0:
                total += trapped_water
        
        return total
            


        
s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(s.trap(height))


