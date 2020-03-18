
n = input()
a = input().split()
s = list()
d = list()
for i in a:
  if i in s:
    s.remove(i)
  else:
    s.append(i)  
print(*s,sep = ' ')
