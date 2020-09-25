from sys import stdin, stdout
points,roads = stdin.readline().split()
streets = []
dots = [str(x) for x in range(1,int(points)+1)]
for x in range(int(roads)):
  road = stdin.readline().split()
  streets.append(tuple(road))

def count(iterable,obj):
  c = 0
  for x in iterable:
    if obj in x:
      c += 1
  return c

def search():
  dead = {}
  end = [x for x in dots if count(streets,x)==1]
  while len(end):
    for x in end:
      dots.remove(x)
      for path in streets:
        if x in path:
          streets.remove(path)
          dead[x] = path
    end = [x for x in dots if count(streets,x)==1]
  return dead

def order(dead):
  out = []
  for x in dead:
    entrance = [i for i in dead[x] if i!=x][0]
    if entrance in dead:
      continue
    if count(streets,entrance) == 0:
      out.append([x,entrance])
    else:
      out.append([entrance,x])
  out.sort(key=lambda x:x[0])
  last = [None]
  while out != last:
    last = out.copy()
    for x in range(len(out)-1):
      if out[x][0]==out[x+1][0] and out[x][1]>out[x+1][1]:
        out[x],out[x+1] = out[x+1],out[x]
  return out

dead = search()
deadend = order(dead)

stdout.write(str(len(deadend))+"\n")
for x in deadend:
  stdout.write(" ".join(x)+"\n")
