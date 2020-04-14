def retrocontador(e):
    if e > 0:
        print("{},".format(e), end="")
        retrocontador(e-1)
    elif e == 0:
        print("{}".format(e))
        retrocontador(e-1)
    else:
        return
   
retrocontador(10)



def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return n
    
print("El sumatorio es: {}".format(sumatorio(4)))



def factorial(n):
    if n > 0:
        return  n * factorial(n-1)
    else:
        return 1
    
print("El factorial es: {}".format(factorial(5)))




