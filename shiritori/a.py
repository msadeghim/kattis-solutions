a = int(input())
s = set()
pre = input()
s.add(pre)
for k in range(a-1):
    ss = input()
    if ss in s or ss[0] != pre[len(pre)-1]:
        if k % 2 == 0:
            print('Player 2 lost')
            exit()
        else:
            print('Player 1 lost')
            exit()
    pre = ss
    s.add(ss)
print('Fair Game')
