T=int((input))
for t in range(t):
    n, s, e, k = map(int, iniput().split())
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t, a[k-1]))