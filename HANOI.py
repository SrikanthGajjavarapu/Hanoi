#1 TOWER OF HANOI PROBLEM
def TOH(n,source,dest,mid):
  if n==1:
    print("move disk {} from {} to {}".format(n,source,dest))
    return
  TOH(n-1,source,mid,dest)
  print("move disk {} from {} to {}".format(n,source,dest))
  TOH(n-1,mid,dest,source)
n=int(input("enter your number"))
TOH(n,'A','C','B')