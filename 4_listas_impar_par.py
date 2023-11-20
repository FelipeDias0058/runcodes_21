def f_par(valor):
    return valor % 2 == 0


def f_lista(n):
    lista=[]
    par=[]
    impar=[]
    for i in range(n):
        num = int(input())
        lista.append(num)
        if f_par(num) == True:
            par.append(num)
        else:
            impar.append(num)
    return lista,par,impar


def main():
    funcao, par, impar = f_lista(20)
    print(funcao, par, impar, sep='\n')
    

if __name__=="__main__":
    main()
