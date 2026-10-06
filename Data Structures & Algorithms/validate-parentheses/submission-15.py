class Solution:
    def isValid(self, s: str) -> bool:
        #create hashmap mapping closing to opening 
        #fo every character in s, check if the character is in the stack. If it is then see if the top of the stack is = to the current element in s 
        #If it is, pop from the stack 
        #If it's not, return false 
        #then add the element to the stack if it isnt already in the stack 

        hashmap = {')' : '(', ']' : '[', '}' : '{'}
        stack  = []
        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                
            else:
                stack.append(c)
        return True if not stack else False
        