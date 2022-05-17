#리스트와 내장함수(2)
a = [23, 12, 6, 53, 19]

#0부터 3까지
print(a[:3])

#1부터 4까지
print(a[1:4])

#len(a) 리스트 a의 값이 몇개가 있느냐 를 확인하는 함수
print(len(a))

#리스트의 값에 하나하나 접근하는 방법(1)
for i in range(len(a)):
    print(a[i], end=' ')
print()

#리스트의 값에 하나하나 접근하는 방법(2)
for x in a:
    print(x, end=' ')
print()

# 홀수만 출력하시오
for x in a:
    if x%2 == 1:
        print(x, end=' ')
print()

# 인덱스 번호까지 접근하고 싶을때
for x in enumerate(a):
    #튜플
    print(x)


#리스트와 튜플의 차이
#튜플의 값은 절대 변경이 불가능하지만 리스트의 값은 변경이 가능하다.

b=(1, 2, 3, 4, 5)
print(b[0])

#요소값에 접근하기
for  x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

#all() 함수는 for문이 a라는 리스트에 접근할때 23,12,36,53,19 가 되는데 그것을
#60>x 를 비교하면서 모두 참이기에 참을 리턴하고
#하나라도 거짓이면 거짓을 리턴한다.
if all(60>x for x in a):
    print("yes")
else:
    print("no")

#any()함수는 조건중에 하나라도 참이면 참이다. 거짓은 모두 거짓일때 거짓을 리턴한다.
if any(15>x for x in a):
    print("yes")
else:
    print("no")
