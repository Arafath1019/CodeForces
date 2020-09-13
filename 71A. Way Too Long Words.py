
# --------------------Solution 01-----------------------------#
# Not Accepted
n = input()
n = int(n)
inputArray = []


if 1<=n<=100:
  for i in range(n):
    a = input()
    inputArray.append(a)

  for i in range(n):

    if 1 <= len(inputArray[i]) <= 100:

      if len(inputArray[i]) < 10:
        print(inputArray[i])

      else:
        a = inputArray[i][0]
        b = inputArray[i][len(inputArray[i])-1]
        middle = str(len(inputArray[i])-2)
        print(a + middle + b)


# ------------------------Solution 02--------------------------#
# Accepted

for i in range(int(input())): 
  s=input() 
  print(s[0]+str(len(s)-2)+s[len(s)-1] if (len(s)>10) else s)