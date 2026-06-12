class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        lookup={
            '}':'{',
            ')':'(',
            ']':'['
        }
        for i in s:
            if i in lookup.values(): # if its a opening bracket
                stack.append(i)
            elif not stack or stack[-1] != lookup[i]:
                return False 
            else:
                stack.pop()

        return not stack # if stack is empty after push and pop operation
        # its a valid paranthesis 