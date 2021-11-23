#슬라이스
a = [23, 12, 36, 53, 19]
#0부터 3번째 까지
print(a[:3])
#[23, 12, 36]
print(a[1:4])
#[12, 36, 53]

#길이
print(len(a))
#5

#for문으로 접근하는 방법1
for i in range(len(a)):
    print(a[i], end=' ')

print()

#for문으로 리스트 원소에 접근하는 방법2
for x in a:
    print(x, end=' ')

print()

for x in a:
    if x%2==1: #2를 나눠 서 1이 남으면 홀수이다.
        print(x, end=' ')
print()

#인덱스번호랑 값을 출력하고 싶을때
for x in enumerate(a):
    print(x)
#enumerate()함수 -> (인덱스번호 , 벨류값) 튜플
# (0, 23)
# (1, 12)
# (2, 36)
# (3, 53)
# (4, 19)

#튜플
b=(1, 2, 3, 4, 5)
print(b[0])
#튜플과 리스트의 차이점은 안에 있는값을 바꿀수 있는냐 없느냐이다
#튜플은 값을 바꿀 수 없다.

for x in enumerate(a):
    print(x[0], x[1])
print()

#인덱스와 리스트 요소값에 접근할 수있는게 enumerate이다.
for index, value in enumerate(a):
    print(index, value)
print()

#all이라는 함수는  60>x라는 조건이 모두 참이면 true를 리턴하고
#아니면 거짓을 리턴한다.
if all(60 > x for x in a):
    print("yes")
else:
    print("no")

print()

#any라는 함수는 5개중에서 한번만 참이면 전체적으로 참이고
#모두 거짓일때에만 거짓을 반환한다.
if any(11 > x for x in a):
    print("yes")
else:
    print("no")





