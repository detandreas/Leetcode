class Solution:
    def simplifyPath(self, path: str) -> str:

        splitted, stack = path.split("/"), []
        for element in splitted:
            
            match element:
                case '':    # '/'
                    continue
                case '.':
                    continue
                case '..':
                    if stack:
                        stack.pop()
                    continue

            stack.append(element)

        return  '/' + '/'.join(stack)
            
s = Solution()
path = "/home//foo/"
print(s.simplifyPath(path))
