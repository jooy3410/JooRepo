#함수 만들기
def add(a, b):
    c=a+b
    print(c)

#기능을 하는 코드를 메인스크립트에 작성한다면
#코드도 길어지고 유지보수하기도 힘들다
#그래서 함수를 쓴다.
#그리고 함수는 메인스크립트 위에다가 해야 인식을 한다.

#이때 main 스트립트가 main함수를 작동시켜라 작동이 된다.
#add(3,2)
#add(5,7)

def add2(a,b):
    c=a+b
    return c #반환해준다 == 결과값을 던져준다.
#return은  함수를 종료하는 역할도 한다.

print(add2(3, 2))

def add3(a, b):
    c=a+b
    d=a-b
    return c, d
    #파이썬은 정수값 두개를 리턴할 수있는데(여러개의 값을 튜플로 리턴된다.

print(add3(3, 2))


#소수만 출력하는 것을 만들어보자


def isPrime(y):
    #y가 소수이면 참을 리턴하고 아니면 거짓을 리턴한다.
    for i in range(2, y): #2부터 y전까지 돌리자
        if y%i==0:
            return  False
    return True #약수가 없으면 트루를 반환

x=[12, 13, 7, 9, 19]
for d in x:
    if isPrime(d): #d 가 y로 전달 된다.
        print(d, end=' ')




