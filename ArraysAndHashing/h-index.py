class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        Complexity: O(nlgn)

        Παρατήρησε ότι max(h) = len(citations)
        citations = [100, 100, 100], h = 3

        Λύση:
        Ταξινομούμε σε φθόνουσα σειρά τον πίνακα citations.
        Για να έχουμε h-index = n πρέπει το nοστό paper, δηλαδή το paper στην θέση n-1 του πίνακα,
        να έχει τουλάχιστον n citations, citations[n-1] >= n.
        Εφόσον ο πίνακας είναι ταξινομημένος η σχέση citations[i] >= n ισχύει και για i < n - 1.

        Εξετάζοντας τις πιθανές τιμές h-index απο την μεγαλύτερη στην μικρότερη εξασφαλίζουμε οτι η πρώτη που θα βρεθεί
        θα είναι και η μέγιστη εφικτή.
        """

        citations.sort(reverse=True)
        for n in range(len(citations), 0, -1):

            if citations[n-1] >= n:
                return n
            
        return 0

class Solution:
    def hIndex(self, citations: list[int]) -> int:
          
        citations.sort(reverse=True)
      
        # Alternative approach that's more intuitive
        h_index = 0
        for i, citation_count in enumerate(citations):
            # i+1 represents the number of papers we've seen so far
            # We can have an h-index of at most min(i+1, citation_count)
            h_index = max(h_index, min(i + 1, citation_count))
      
        return h_index
            

            
s = Solution()
#citations = [3,0,6,1,5]
#citations = [1,3,1]
#citations = [10]
#citations = [1,1,1,1]
#citations = [1,2,3,4,5]
#citations = [4999] * 4998
#citations.append(1)
#citations = [0,0,2]
citations = [0,0,0]
print(s.hIndex(citations))