import math
import itertools

def archheight(x1,x2):
  r = (x2 - x1) / 2
  center_x = (x2 + x1) / 2
  center_y = h - r
  for x in range(x1,x2+1):
    y = math.sqrt(r**2-(x-center_x)**2)+center_y
    arch_h[x] = y

groundheight = {}
detail = input().split()
h = int(detail[1])
alpha = int(detail[2])
beta = int(detail[3])
for i in range(int(detail[0])):
  ground = input().split()
  groundheight[int(ground[0])] = int(ground[1])

length = int(ground[0])
#all combinations of pillar placement
combinations = []
pos = [x for x in groundheight if x not in (0,length)]
for pnum in range(len(pos)+1):
  for subset in itertools.combinations(pos, pnum):
    c = list(subset)
    c.append(0)
    c.append(length)
    c.sort()
    combinations.append(c)


#calculate arch lengths and pillar heights
archlength = []
pillarheight = []
for c in combinations:
  illegal = False
  arch_h = {}
  for x in range(len(c)-1):
    archheight(c[x],c[x+1])
  for x in groundheight:
    if groundheight[x] > arch_h[x]:
      illegal = True
      break
  if illegal:
    continue
  
  archlength.append([c[i+1]-c[i] for i in range(len(c)-1)])
  pillarheight.append([h-groundheight[c[i]] for i in range(len(c))])

costs = []
for a,p in zip(archlength,pillarheight):
  arch = sum([x**2 for x in a]) * beta
  pillar = sum(p) * alpha
  total = arch + pillar
  costs.append(total)

if bool(costs):
  print(min(costs))
else:
  print("impossible")
