a,b,c=map(int,input().split())
if a+b+c==180 and (a+b>c or a+c>b or c+b>a) and (a>0 and b>0 and c>0):
  print("YES")
else:
  print("NO")
