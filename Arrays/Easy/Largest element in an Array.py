def largest( arr, n):
    max=arr[0]
    for i in arr:
        if max < i:
            max = i
            
    return max
