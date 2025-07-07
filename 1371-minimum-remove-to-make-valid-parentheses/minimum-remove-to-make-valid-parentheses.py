class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ''
        balanced = []
        st = 0
        op = []
        string = list(s)

        for i, ch in enumerate(string):
            if ch == ')':
                if st==0:
                    ch = '_'
                else:
                    st -= 1
            if ch == '(':
                op.append(['(', i])
                st += 1
            balanced.append(ch)

        for ch, i in reversed(op):
            if st == 0:
                break
            balanced[i] = '_'
            st -= 1

        for ch in balanced:
            if ch != '_':
                res += ch
        return res
