a = int(input())
pre = 1
for i in range(a):
    b = int(input())
    k = pre
    while k < b:
        print(k)
        k += 1
    pre = b + 1
if b == a:
    print('good job')
