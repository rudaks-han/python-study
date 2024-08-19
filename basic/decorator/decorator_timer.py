import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@timer_decorator
def slow_function():
    time.sleep(2)
    print("Finished slow function")


if __name__ == "__main__":
    slow_function()
