
"""
two conditions
1.back taller than front
2.price in increasing order

input
4 - number of item in each row
3 2 1 2 - price of back row
2 3 4 3 - height of back row
2 1 2 1 - price of front row
2 2 1 3 - height of front row

output
3 2 4 1 - order of back row
4 2 1 3 - order of front row
"""

class tile:   #create tile object
  def __init__(self,price,height,order):
    self.p = price
    self.h = height
    self.o = order

row1 = [] 
row2 = []
#put tiles in lists
n = int(input())
p1 = input().split()
h1 = input().split()
for x in range(n):
  obj = tile(p1[x],h1[x],str(x+1))
  row1.append(obj)

p2 = input().split()
h2 = input().split()
for x in range(n):
  obj = tile(p2[x],h2[x],str(x+1))
  row2.append(obj)


def sort_all_perm(old_row):
  change = True
  permutations = []
  row = old_row.copy()
  counter = 0
  while change:
    if counter % 2 == 0:
      last = row.copy()
    for x in range(n-1):
      if row[x+1].p < row[x].p:
        holder = row[x]
        row[x] = row[x+1]
        row[x+1] = holder
      elif row[x+1].p == row[x].p:
        new = row.copy()
        new1 = sorted(new,key=lambda t:t.p)
        if new1 not in permutations:
          permutations.append(new1)
        holder = row[x]
        row[x] = row[x+1]
        row[x+1] = holder
        new.sort(key=lambda t:t.p)
        if new not in permutations:
          permutations.append(new)
    if row == last:
      change = False
      if row not in permutations:
        permutations.append(row)
    counter += 1
  return permutations

back = sort_all_perm(row1)
front = sort_all_perm(row2)

print()
out = []
found = False
for b in back:
  for f in front:
    invalid = False
    for x in range(n):
      if b[x].h <= f[x].h:
        invalid = True
        break
    if invalid == False:
      found = True
      out.append([obj.o for obj in b])
      out.append([obj.o for obj in f])
      break
  if found:
    break

if bool(out):
  for line in out:
    print(" ".join(line))
else:
  print("impossible")
