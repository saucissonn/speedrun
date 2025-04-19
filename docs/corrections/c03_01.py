def fibonacci(n):
    if n < 2 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#utilisation de la prog dynamique (ascendante)
def fibonaccib(n):
    t = [0]*(n+1)
    t[1] = 1
    for i in range(2, n+1):
        t[i] = t[i-1] + t[i-2]
    return t[n]