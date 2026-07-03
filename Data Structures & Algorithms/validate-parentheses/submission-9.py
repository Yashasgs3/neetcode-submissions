class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in match:          # Closing bracket
                if not stack or stack.pop() != match[ch]:
                    return False
            else:                    # Opening bracket
                stack.append(ch)

        return not stack