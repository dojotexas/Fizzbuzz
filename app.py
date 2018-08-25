def fizzbuzz(numero):
    if numero % 3 ==0 and numero % 5 == 0:
        retorno = 'fizzbuzz'
    elif numero % 3 == 0:
        retorno = 'fizz'
    elif numero % 5 == 0:
        retorno = 'buzz'
    else:
        retorno = numero
    return retorno
    
