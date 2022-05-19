#함수만들기

#두개 숫자를 받아서 더한값을 출력해주는 함수
# def add(a, b):
#     c = a+b
#     print(c)

# add(3, 2)
# add(5, 7)

def add(a, b):
    c=a+b
    return c
#리턴은 종료하는방법이기도하고 add(3, 2)가 리턴값으로 변하는 역할도 한다.

x = add(3, 2)
print(x)

#여러개의 값을 리턴할 수 있다.
def add(a, b):
    c = a + b
    d = a - b
    return c, d
print(add(3, 2))




#소수만 출력하는 프로그램을 만드시오

def 소수(x):
    #2부터 자기자신까지 돌아라
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a = [12, 13, 7, 9, 19]

for x in a:
    if 소수(x):
        print(x, end=' ')