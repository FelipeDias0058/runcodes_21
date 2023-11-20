
def f_lista_1(n):
    lista_1 = []
    for i in range(n):
        lista_1.append(int(input()))
    return lista_1

def f_lista_2(n):
    lista_2 = []
    for i in range(n):
        lista_2.append(int(input()))
    return lista_2

def f_lista_3(n,lista_1,lista_2):
    lista_3=[]
    for i in range(n):
        lista_3.append(lista_1[i])
        lista_3.append(lista_2[i])
    return lista_3
        
    
def main():
    A = f_lista_1(25)
    B = f_lista_2(25)
    C = f_lista_3(25, A, B)

    print(A)
    print(B)
    print(C)
    
if __name__== '__main__':
    main()
