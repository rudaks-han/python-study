def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 함수 실행 전
        result = func(*args, **kwargs)
        # 함수 실행 후
        return result

    return wrapper


def simple_decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")

    return wrapper


@simple_decorator
def say_hello():
    print("Hello, World!")


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result

    return wrapper


@logging_decorator
def add(a, b):
    return a + b


if __name__ == "__main__":
    # say_hello()
    print(add(1, 2))
