a = set()
b = int(input())
for i in range(b):
    a.add(input().lower().replace('-', ' '))

print(len(a))
