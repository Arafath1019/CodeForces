import math
n, m, a = input().split()
n = int(n)
m = int(m)
a = int(a)
if (1<=a<=10**9) and (1<=m<=10**9) and (1<=n<=10**9):
  flagstones = math.ceil(m/a) * math.ceil(n/a)
  print(flagstones)