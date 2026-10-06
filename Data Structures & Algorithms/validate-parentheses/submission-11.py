class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])

         
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if (stack[-1] == '(' and c == ')') or (stack[-1] == '[' and c == ']') or (stack[-1] == '{' and c == '}'):
                    if stack and stack[-1]:
                        stack.pop()
            
        if not stack:
            return True
        return False


        