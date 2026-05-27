class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        if len(s) == 1:
            return False
        elif len(s) == 0:
            return True

        res = []

        for b in s:
            if b in brackets:
                res.append(b)
            else:
                if not res:
                    return False

                if b == brackets[res[-1]]:
                    res.pop()
                else:
                    return False

        if res:
            return False

        return True