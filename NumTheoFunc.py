from EuclidsAlgo import EuclidAlgo2

def Tao(n):
  count = 0
  for i in range(1, n+1):
    if n%i == 0:
      count += 1
  return count

def listSum(list):
  sum=0 
  for i in list:
    sum += i
  return sum

def sigmaK(n, k, ask):
  list = []
  for i in range(1, n+1):
    if n%i == 0:
      list.append(i**k)
  if ask == "list":
    return list
  elif ask == "sum":
    return listSum(list)

def coPrime(a, b):
    if EuclidAlgo2(a, b) == 1:
        return True
    else:
        return False

def eulerPi(n, ask):
  count = 0
  listofcoprime = []
  for i in range(1, n+1):
    if coPrime(i, n):
      count += 1
      listofcoprime.append(i)
  if ask == "list":
    return listofcoprime
  elif ask == "count":
    return count

