class Solution:
    def isValid(self, s: str) -> bool:
        asdfsdfa = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for char in s:
            if char in asdfsdfa:
                top = stack.pop() if stack else '#'
                
                if asdfsdfa[char] != top:
                    return False
            else:
                stack.append(char)
                
        return not stack