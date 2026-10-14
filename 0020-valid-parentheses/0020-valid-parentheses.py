class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:

            if bracket not in brackets:
                stack.append(bracket)

            else:
                if len(stack) == 0:
                    return False

                if stack[-1] != brackets[bracket]:
                    return False

                stack.pop()

        return len(stack) == 0