def print2largest(self,arr, n):
    # code here
    m1 = 0
    m2 = 0
    for i in arr:
        if m1 < i:
            m2 = m1
            m1 = i
        elif m2 < i and i < m1:
            m2 = i
    return m2 if m2 != 0 else -1
