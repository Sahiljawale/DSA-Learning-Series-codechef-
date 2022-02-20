for _ in range(int(input())):
  n,k=map(int,input().split())
  l=list(map(int,input().split()))
  ans=0
  for i in range(n):
    if l[i]>k:
      continue
    if k%l[i]==0:
      ans=max(ans,l[i])
  if ans==0:
    print("-1")
  else:
    print(ans)
