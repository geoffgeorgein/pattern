
n= int(input("Enter no of rows "))

k=int((2*n-2)/2)
for i in range(0,n):
  for j in range (0,k):
    print(end=" ")

  k=k-1
  for l in range(0,i+1):
      print("*",end=" ")
  print("\r")
