#람다함수
#익명의 함수 == 람다 표현식

def plus_one(x):
    return x+1

print(plus_one(1))

#람다함수로 변환하기
#람다함수를 호출하려면 변수에 할당을 해줘야한다.

plus_two=lambda y: y+2
print(plus_two(1))
#람다함수는 주로 내장함수에 인자로 사용할때 유용하다

a=[1,2,3]
print(list(map(plus_one, a)))
#map은 인자값이 두개인데 map(함수, 인자값)
#a라는 리스트값들이 함수 영향을 받는다.
#[2, 3, 4]

print(list(map(lambda x: x+1, a)))
#lambda를 써서 출력한다.
#[2, 3, 4]




