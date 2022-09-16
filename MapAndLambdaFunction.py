cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers    
    lim=n
    lista = [0,1]
    
    for i in range(2,lim):
        lista.append(lista[i-2] + lista[i-1])
        
    return(lista[0:lim])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
