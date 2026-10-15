class Solution:
    def isValid(self, s: str) -> bool:

        open_stack = []
        close_stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:

            if bracket in "([{":
                open_stack.append(bracket)

            else:
                close_stack.append(bracket)

                if len(open_stack) == 0:
                    return False

                open_bracket = open_stack.pop()
                close_bracket = close_stack.pop()

                if open_bracket != pairs[close_bracket]:
                    return False

        return len(open_stack) == 0 and len(close_stack) == 0