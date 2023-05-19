def largest( arr, n):
    m = arr[0]
    for i in arr:
        if m < i:
            m = i
            
    return m

# Another approach

def largest( arr, n):
    m = float("-inf")
    for i in arr:
        if max < i:
            m = i
            
    return m
