class Solution:
    """
    Given a string containing just the characters
    '(', ')', '{', '}', '[' and ']', determine if
    the input string is valid. The brackets must
    close in the correct order, "()" and "()[]{}"
    are all valid but "(]" and "([)]" are not.
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in dic.keys():
                stack.append(char)
            elif char in dic.values():
                if stack == [] or char != dic[stack[-1]]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return stack == []

    def bracket_match(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack == []:
                    cnt += 1
                elif stack[-1] == '(':
                    stack.pop()

        cnt += len(stack)

        return cnt

    def bracket_match2(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif stack == []:
                stack.append(char)
            elif stack[-1] == '(':
                stack.pop()

        return len(stack)

    def match(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            stack.append(char)
            if char in dic.values() and len(stack) > 1:
                if stack[-2] in dic.keys() and char == dic[stack[-2]]:
                    stack.pop()
                    stack.pop()

        return len(stack)

    def match2(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        # Traverse the input parentheses string
        for char in s:
            # If the current one is left parenthesis push to stack
            if char in dic.keys():
                stack.append(char)

            # Else if the current one is a right parenthesis
            elif char in dic.values():
                # If the stack is empty or the top on is a right parenthesis
                if stack == [] or stack[-1] in dic.values():
                    # Push the current right parenthesis
                    stack.append(char)
                # Else if the stack top is a left parenthesis
                elif stack[-1] in dic.keys():
                    # If the current right parenthesis does not match the top
                    # Push the current right parenthesis
                    if char != dic[stack[-1]]:
                        stack.append(char)
                    # Else if pop the top stack parenthesis
                    elif char == dic[stack[-1]]:
                        stack.pop()

        # Return the length of the remaining stack
        return len(stack)


if __name__ == "__main__":
    test1 = "(()())"  # Expected result 0
    test2 = "((())"  # Expected result 1
    test3 = "())"  # Expected result 1
    test4 = "((()"  # Expected result 2
    test5 = ")("  # Expected result 2
    test6 = ")((("  # Expected result 4
    test7 = "{[(()][}"  # Expected result 6
    test8 = "}[([])}]"  # Expected result 4
    test9 = "{[()]}"  # Expected result 0
    test10 = "][({})]"  # Expected result 1
    sol = Solution()
    print(sol.bracket_match2(test1))
    print(sol.bracket_match2(test2))
    print(sol.bracket_match2(test3))
    print(sol.bracket_match2(test4))
    print(sol.bracket_match2(test5))
    print(sol.bracket_match2(test6))
    print(sol.match2(test7))
    print(sol.match2(test8))
    print(sol.match2(test9))
    print(sol.match2(test10))
