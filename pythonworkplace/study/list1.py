import random as r

#리스트 :하나의 변수를 일렬로 순서를 정해 묶어 놓은것

#리스트 만드는 방법
a=[]
print(a)

c=[1, 2, 3, 4, 5]
print(c)
print(c[0])

#range를 이용하여 리슽 만들기
b=list(range(1, 11))
print(b)

#리스트 끼리 더할 수도있다.
d = c+b
print(d)

#리스트에 요소 값 추가하기
print(a)
a.append(6)
print(a)

#특정 인덱스 값에 요소 넣기
a.insert(0, 7)
print(a)

#리스트에서 맨뒤에 값 삭제하기
a.pop()
print(a)

#리스트에서 위치값을 넣어주면 그자리의 요소값이 사라진다.
a.pop(0)
print(a)

#리스트의 특정값 지우기(4라는 값을 찾아서 지우기)
print(c)
c.remove(4)
print(c)

#리스트에서 요소값이 몇번 인덱스에 있는지 알려주기
print(c.index(5))

l = list(range(1,11))
print(l)

#l이라는 리스트 요소들의 합 출력하기
print(sum(l))

#l라는 리스트 값들중 가장 큰값 찾아주기
print(max(l))

#l라는 리스트에서 가장 작을값 출력해주기
print(min(l))

#l라는 리스트에서 인자 값들중에서 최소값 찾아주기
print(min(7, 5))

#l이라는 리스트의 값들을 무작위로 섞어라
r.shuffle(l)
print(l)

#l이라는 리스트를 오름차순으로 정리하기
l.sort()
print(l)

#l이라는 리스트를 내림차순하기
l.sort(reverse=True)
print(l)

#l이라는 리스트 값들을 없애기 -->빈리스트만들기
l.clear()
print(l)
