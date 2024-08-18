x = 10  # 전역 변수

def modify_global():
    global x  # 전역 변수 x를 참조
    x = 20    # 전역 변수 x를 수정

# modify_global()
# print(x)  # 20 출력

y = 1
def outer_function():
    y = 5  # 외부 함수 변수

    def inner_function():
        nonlocal y  # 바깥 함수의 y를 참조
        y = 10      # 바깥 함수의 y를 수정

    inner_function()
    print(y)  # 10 출력

print(y)  # 10 출력

outer_function()


