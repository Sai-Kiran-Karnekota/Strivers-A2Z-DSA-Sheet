def frequencyCount(self, arr, N, P):
    # code here
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in range(len(arr)):
        if (i+1) in d:
            arr[i] = d[i+1]
        else:
            arr[i] = 0
