def factorialNumbers(self, N):
      l = []
  def fact(c,n):
      if n>N:
          return l
      c += 1
      l.append(n)
      return fact(c, n*c)
  return fact(1,1)
