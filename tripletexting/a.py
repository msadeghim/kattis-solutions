a = input()
l = len(a) // 3
if a[0:l] == a[l:l+l]:
    print(a[0:l])
elif a[0:l] == a[l+l:]:
    print(a[0:l])
else:
    print(a[l:l+l])
