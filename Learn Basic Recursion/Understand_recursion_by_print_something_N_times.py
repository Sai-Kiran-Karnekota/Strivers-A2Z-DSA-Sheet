def printNos(self,N):
    #Your code here
    def pNos(n): # Recursive function
        if n == N: # Checks whether n == N if True terminates the recursion by returning None
            print(n, end=' ')
            return 
        print(n, end=' ') # if n != N then prints n with space
        return pNos(n+1) # Recursive return with function pNos while increasing the n value by 1
    pNos(1) # Since printing number starts from 1 we send 1 as it's parameter
