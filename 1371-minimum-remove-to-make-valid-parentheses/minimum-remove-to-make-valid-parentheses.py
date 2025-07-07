class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        hashmap = {')': '('}
        stack = []
        final_list = []
        complement = 0

        for char in s:
            if char == '(':
                stack.append(char)
                complement += 1
            if char in hashmap:
                complement -= 1
                if stack:
                    stack.pop()
                else:
                    continue
                
            final_list.append(char)

        reversed_list = final_list[::-1]

        while len(stack) > 0:
            reversed_list.remove(stack[-1])
            stack.pop()
            
        return "".join(reversed_list[::-1])