from collections import defaultdict, Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        """
        m = len(s)
        k = len(words[0])
        O(m * k) time complexity.

        n = len(words)
        O(n * k) space complexity
        """
        word_count = Counter(words)

        string_length = len(s)
        num_words = len(words)
        word_length = len(words[0])

        res = []

        for starting_position in range(word_length):

            hash_map: dict[str, int] = defaultdict(int)
            l = r = starting_position

            while l + word_length <= string_length:

                curr_word = s[r: r+word_length]
                r += word_length

                if word_count == 0:
                    l = r
                    hash_map.clear()
                    continue

                hash_map[curr_word] += 1

                while hash_map[curr_word] > word_count[curr_word]:
                    removed_word = s[l: l+word_length]
                    l += word_length
                    hash_map[removed_word] -= 1

                if r - l == num_words * word_length:
                    res.append(l)

        return res

s = "barfoothefoobarman"
words = ["foo","bar"]
sol = Solution()
print(sol.findSubstring(s, words))