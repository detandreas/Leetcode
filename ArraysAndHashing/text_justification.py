class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:

        length, line = 0, []
        res = []

        for word in words:
            if length + len(line) + len(word) > maxWidth:

                n_gaps = len(line) - 1
                extra_space = maxWidth - length
                distribution = extra_space // max(1, n_gaps)
                remainder = extra_space % max(1, n_gaps)

                for i in range(max(1, len(line) - 1)):
                    line[i] += " " * distribution

                    if remainder:
                        line[i] += " "
                        remainder -= 1

                res.append("".join(line))
                length, line = 0, []


            length += len(word)
            line.append(word)

        last_line = " ".join(line)
        trailling_space = maxWidth - len(last_line)
        res.append(last_line + " " * trailling_space)
        return res




s = Solution()
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(s.fullJustify(words, maxWidth))
