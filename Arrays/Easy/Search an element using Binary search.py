def searchInSorted(self,arr, N, K):
    #Your code here
    h = N
    l = 0
    while l <= h:
        m = (l+h)//2
        if arr[m] > K:
            h = m-1
        elif arr[m] < K:
            l = m + 1
        elif arr[m] == K:
            return 1
    else:
        return -1
