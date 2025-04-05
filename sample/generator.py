# Generator (제너레이터):
# 여러 개의 값을 필요할 때 하나씩 반환하는 특별한 함수입니다.
# 일반 함수와 달리 한 번에 모든 값을 반환하지 않고, 한 번에 하나씩 값을 생성(yield) 하고 중단됩니다.

# yield 키워드:
# Generator 함수 내에서 사용되는 특수한 키워드로, 값을 반환하면서 함수의 실행을 잠시 멈추는 역할을 합니다.
# yield가 있으면 그 함수는 자동으로 제너레이터가 됩니다.

# 요약:
# Generator는 값을 한 번에 하나씩 생성하는 함수이고,
# yield 는 그 Generator를 가능하게 하는 파이썬의 키워드

def generator_function():
    print("첫번째")
    yield 1
    print("두번째")
    yield 2
    print("세번째")
    yield 3
    print("마지막은 yield 없음")


gen = generator_function()

print(next(gen))  # 첫번째 값 생성
print(next(gen))  # 두번째 값 생성
print(next(gen))  # 세번째 값 생성
print(next(gen))  # 마지막 값 생성, StopIteration Exception 발생

