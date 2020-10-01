if 2 > 1:
    print("Hello")

if 1 > 2:
    print("Hello")  # 거짓이여서 프린트 안한다.

    # 거짓일때 출력하려면

if not 1 > 2:
    print("Hello")

    # 여러가지 조건을 붙일 수 있다.

if 1 > 0 and 2 > 1:
    print("Hi")

if 0 > 0 and 2 > 1:
    print("Hi")

# and는 한쪽만 참일 경우 거짓이다.
# 하지만 or은 한쪽만 참이여도 결과를 출력한다.

if 0 > 0 or 2 > 1:
    print("Hi")