book = input().split()
pages = input().split()
num = int(book[1])
notebooks = 1
for page in pages:
  if int(page) > num:
    notebooks += 1
    num = 100 - int(page)
  else:
    num -= int(page)

print(notebooks)
