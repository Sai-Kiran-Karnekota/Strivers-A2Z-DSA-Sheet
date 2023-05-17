def sumOfCubes(N):
    if N == 0:
        return 0
    return N**3 + sumOfCubes(N-1)
print(sumOfCubes(10))
