
n = str(input())
s = list(n)
l = ["a","e","i","o","u","A","E","I","O","U"]
co = 0
v = 0
for i in s:
  if i in l:
    v += 1
  if i not in l:
    co += 1
print(v , co , sep = " ")      
