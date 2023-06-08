class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '{', '[']
        #close_bracket = [')', '}', '[']
        for letter in s:
            print(stack)
            if letter in open_brackets:
                stack.insert(0, letter)
            else:
                if (len(stack) == 0):
                    return False
                elif (stack[0] == self.opposite_bracket(letter)):
                    print(stack[0])
                    print(self.opposite_bracket(letter))
                    stack.pop(0)
                else:
                    return False
        if (len(stack) == 0):
            return False
        return True

    def opposite_bracket(self, s: str) -> str:
        if s == ')':
            return '('
        elif s == '}':
            return '{'
        else:
            return '['
                    


if __name__ == '__main__':
    s = "()"
    sol = Solution()
    print(sol.isValid(s))