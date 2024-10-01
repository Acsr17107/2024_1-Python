def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    print('{}! = {}'.format(n, a))

factorial(5)
factorial(10)
factorial(20)