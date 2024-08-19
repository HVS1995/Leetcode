class Solution:
    def __init__(self):
        self.t = [[-1 for _ in range(1001)] for _ in range(1001)]

    def solve(self, currCountA, pasteCountA, n):
        if currCountA == n:
            return 0

        if currCountA > n:
            return 1000

        if self.t[currCountA][pasteCountA] != -1:
            return self.t[currCountA][pasteCountA]

        copyPaste = 1 + 1 + self.solve(currCountA + currCountA, currCountA, n)
        paste = 1 + self.solve(currCountA + pasteCountA, pasteCountA, n)

        self.t[currCountA][pasteCountA] = min(copyPaste, paste)
        return self.t[currCountA][pasteCountA]

    def minSteps(self, n):
        if n == 1:
            return 0  # We already have 1 A

        self.t = [[-1 for _ in range(1001)] for _ in range(1001)]

        # We have to start with a copy, hence 1 +
        return 1 + self.solve(1, 1, n)
        