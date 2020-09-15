
line1 = input().split()
num = int(line1[0])
height = int(line1[1])
speed = int(line1[2])
disc_width = int(line1[3])
length = 200000

def check(x1,y1,x2,y2):  #check if acid touch disk
  if y2 == y1 and x2 in x1:
    return True
  else:
    return False

pos = []

for x in range(num):  #put acid pos into list
  acid = input().split()
  x = int(acid[0])
  y = int(acid[1])
  pos.append([x,y])


for dh in range(height):#try all height to throw the disk
  disk = [-x-1 for x in range(disc_width)]
  t = 0
  while disk[-1] != length:
    for x in range(disc_width):
      disk[x] += 1
    t += 1
    for p in pos:
      if t == 1:
        test = check(disk,dh,p[0],p[1])
      else:
        test = check(disk,dh,p[0],y+speed-1)
      if test:
        break
      for v in range(speed):
        y = ((p[1]+t*speed) % height)-v
        if y < 0:
          y = height + y
        test = check(disk,dh,p[0],y)
        if test:
          break
      if test:
        break
    if test:
      break
  if disk[-1] == length:
    break

if test:
  print("GAME OVER")
else:
  print("VICTORY")
