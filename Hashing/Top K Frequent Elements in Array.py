def topK(self, nums, k):
    #Code here

    d = {}
    max, min = 1,1
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return sorted(d, key=lambda i:(d[i],i),reverse=True)[:k]
