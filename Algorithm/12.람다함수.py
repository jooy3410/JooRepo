def plus_one(x):
    return x+1

print(plus_one(1))

#람다함수
#x는 매개변수
plus_tow=lambda x: x+2
print(plus_tow(1))

#람다함수는 어떤 내장함수에 인자로 쓸때 편리하다
a=[1, 2, 3]
print(list(map(plus_one, a)))

#자료들을 인트화 시켜라
#map(int, 자료형 )
#map(함수명, 자료)

#이럴때 람다함수가 유용하다.
print(list(map(lambda x: x+1, a)))
