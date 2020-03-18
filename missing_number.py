n = input().split()
l = []
for i in n:
  l.append(int(i))
d = []
for i in range(1,101):
  if i not in l:
    d.append(i)
print(*d,sep = " ")    
