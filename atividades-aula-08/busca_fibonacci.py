def busca_fibonacci(arr, valor):
    n = len(arr)
    
    fib_m2 = 0  
    fib_m1 = 1  
    fib_m = fib_m2 + fib_m1  

    
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if arr[i] < valor:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > valor:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i 

    
    if fib_m1 and offset + 1 < n and arr[offset + 1] == valor:
        return offset + 1

    return -1  

arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
valor = 80

resultado_fibonacci = busca_fibonacci(arr, valor)
print("Índice encontrado (Fibonacci Search):", resultado_fibonacci)
