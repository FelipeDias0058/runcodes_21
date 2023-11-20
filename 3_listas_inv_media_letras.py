def f_ListaInversa(n):
    lista=[]
    if n==0:
        return lista
    else:
        for i in range(n):
            lista.append(float(input()))
        lista.reverse()
        lista2=[round(i,4)for i in lista]
        return lista2
def f_Média(n):
    média=[]
    média2=0
    if n==0:
        return média,"SEM NOTAS"
    else:
        for i in range(n):
            média.append(float(input()))
        média2=sum(média)/n
        média3=[round(i,1)for i in média]
        média4=(round(média2,1))
        return média3,média4
def f_Letras(n):
    contador=0
    letras=[]
    for i in range(n):
        adicional=input()[0]
        if adicional in ('A','E','I','O','U','a','e','i','o','u'):
            contador+=1
        elif adicional in ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','W','Y','Z','b','c','d','f','g','h','j','k','l','m','n','p',
                           'q','r','s','t','v','x','w','y','z'):
            letras.append(adicional)
    return contador,letras
        
def main():
    num = int(input())
    n1 = f_ListaInversa(num)
    n2, n3 = f_Média(num)
    n4, n5 = f_Letras(num)
    print(n1,n2,n3,n4,n5, sep='\n')

if __name__=="__main__":
    main()
