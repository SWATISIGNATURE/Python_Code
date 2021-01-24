def Factorial(n):
    if n <= 1:
        return 1
    else:
        print(n)
        return n * Factorial(n-1)

if __name__=="__main__":
    print(Factorial(5)) 