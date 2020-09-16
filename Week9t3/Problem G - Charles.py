
field = [1 for i in range(100)]
num = int(input())

def cutrow(n):
  for i in range(10):
    field[(n-1)*10+i] = 1

def cutcol(n):
  for i in range(10):
    field[i*10+n-1] = 1

for i in range(num):
  field = [x+1 for x in field]
  lines = input().split()
  for r in range(3):
    cutrow(int(lines[r]))
  for c in range(3,6):
    cutcol(int(lines[c]))

print()
for r in range(10):
  print(field[r*10],field[r*10+1],field[r*10+2],field[r*10+3],field[r*10+4],field[r*10+5],field[r*10+6],field[r*10+7],field[r*10+8],field[r*10+9])
