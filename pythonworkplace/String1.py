x = 4  # 숫자타입
y = "4"  # 문자열 타입

# 다른타입으로 연산을 할 수 없다.

# print(x + y)

print(str(x) + y)

# x를 문자열타입으로 케스팅 해주면 된다.

print(x + int(y))

# y를 숫자타입으로 케스팅 해준다.