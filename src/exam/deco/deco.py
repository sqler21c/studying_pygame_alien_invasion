import time

def make_cal(op):
    if op == '+':
        return lambda x, y : x + y
    
    if op == '-':
        return lambda x, y : x - y
    if op == '*':
        return lambda x, y : x * y
    if op == '/':
        return lambda x, y : x / y

plus = make_cal('+')

# plus(3,2)
print(plus(3,2))


def big_number(n):
    return n ** n ** n

def make_func_alarm(func):
    def new_func(*args, **kwargs):
        print("start function")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print('실행 시간 : ', end_time - start_time)
        print("end funciton")
        return result
    
    return new_func

# new_fuc = make_func_alarm(big_number)
# new_fuc(6)


@make_func_alarm
def big_mumber1(n):
    return n ** n ** n

@make_func_alarm
def big_number2(n):
    return (n+1) ** (n+1) ** (n+1)

big_mumber1(3)
print("big 2")
big_number2(6)
