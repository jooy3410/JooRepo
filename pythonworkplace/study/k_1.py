n, k = map(int, input().split())
#문자를 스트링으로 받는데, int로 정수화 시킨다.
#그리고 map 으로 n kf로 하나씩 메핑한다.
#개수를 새야하는까
cnt=0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
#for에서 중간에 브레이크 걸리지 않으면, else구문이 돌아가지 않지만
#정상적으로 돌면 else를 실행한다.
else:
    print(-1)
