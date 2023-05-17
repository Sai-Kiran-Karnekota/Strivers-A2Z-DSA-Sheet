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


# Another approach

Arr = [1,2,3,4,5]
a = len(Arr)
b = a//2 if a%2==0 else a//2 + 1
def rev(c):
    if c >= b:
        d = Arr[c]
        Arr[c] = Arr[a-c-1]
        Arr[a-c-1] = d
        c -= 1
        return rev(c)
    return Arr
print(rev(a-1))
