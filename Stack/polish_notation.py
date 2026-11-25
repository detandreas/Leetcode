class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []
        operators = ("+", "-", "*", "/")
        for token in tokens:
            if token in operators:
                b, a = int(stack.pop()), int(stack.pop())
                match token:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a/b))
            else:
                stack.append(token)
        return int(stack.pop())


s = Solution()
token = ["2", "1", "+", "3", "*"]
print(s.evalRPN(token))
