def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet("Alice")
