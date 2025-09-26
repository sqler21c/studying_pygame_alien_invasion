def func(*args):
    return args

print(type(func(5)))


def start(func, *args, **kwargs):
    print("start function")
    return func(*args, **kwargs)

def sum_a_b(a, b):
    return a + b

result = start(sum_a_b, 3, 5)
print(result)