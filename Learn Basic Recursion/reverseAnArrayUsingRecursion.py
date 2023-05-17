Arr = [1,2,3,4,5]
# Arr is a list
L = []
a = len(Arr)
def rev(c):
    if c >= 0:
        L.append(Arr[c])
        c -= 1
        return rev(c)
    return L
print(rev(a-1))
