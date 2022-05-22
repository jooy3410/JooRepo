#k번째 약수
n, k =map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
#for else 구문 
#for 문이 정상적으로 끝나면 else 문이 동작