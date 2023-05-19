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

            
# another & best approach
from collections import Counter
def frequencyCount(self, arr, N, P):
    d = Counter(arr)
    for i in range(arr):
        arr[i] = d[i+1]
