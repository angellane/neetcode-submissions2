class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])

         
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if (c == '}' or c == ']' or c == ')') and (stack[-1] == '(' or stack[-1] == '[' or stack[-1] == '{'):
                    stack.pop()
            
        if not stack:
            return True
        return False


        