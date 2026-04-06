class Solution:
    def isValid(self, s: str) -> bool:
        characters = {')':'(',']':'[','}':'{'}
        stack = []
        for ch in s:
            if ch in characters:
                if not stack or stack[-1]!=characters[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack