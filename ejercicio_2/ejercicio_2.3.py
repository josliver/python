def fibonacci(num):
    if num == 0 or num == 1 : 
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_range(num):
    fibo_numbers = []
    for i in range(num):
        fibo_numbers.append(fibonacci(i))
    return fibo_numbers

print(fibonacci_range(6))