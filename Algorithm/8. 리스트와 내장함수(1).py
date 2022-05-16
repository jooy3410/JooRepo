import random as random
#빈 리스트
a = []
print(a)
# list()함수
b = list()
print(b)

a = [1, 2, 3, 4, 5]
print(a)
#a의 0번째 값을 출력하라
print(a[0])
#b라는 변수에 list 함수를 써서 리스트를 만드는데 range함수를 사용하여 1부터10까지 저장하라
b= list(range(1, 11))
print(b)

#리스트합치기
c = a+b
print(c)

#리스트에 있는 함수들

#append()
a.append(6)
print(a)

#insert(인덱스번호, 들어갈 값)
a.insert(3, 7)
print(a)

#pop() 맨뒤에 있는값 꺼내기
a.pop()
print(a)
#a.pop(3) 특정인덱스 자리값 꺼내기

#remove(4) 4를 찾아서 삭제하라
a.remove(4)
print(a)

#index(5) 5라는 값이 인덱스 몇번째에 있는지 찾는 함수
print(a.index(5))

#a초기화
a=list(range(1,11))
print(a)

#a라는 리스트의 모든 값 합산
print(sum(a))

#a라는 리스트의 값중 가장 큰값
print(max(a))

#a라는 리스트의 값중 가장 작은값
print(min(a))

random.shuffle(a)
print(a)

#a를 오름차순으로 정렬
a.sort()
print(a)

#a를 내림차순으로 정렬
a.sort(reverse=True)
print(a)

#clear() 리스트 초기화 함수
a.clear()
print(a)



