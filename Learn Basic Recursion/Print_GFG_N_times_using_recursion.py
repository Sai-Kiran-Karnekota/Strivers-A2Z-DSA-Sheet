def printGfg(self, n):
    # Code here
    def p(i):
        if i == 0:
            return
        print("GFG", end = ' ')
        return p(i - 1)
    p(n)
