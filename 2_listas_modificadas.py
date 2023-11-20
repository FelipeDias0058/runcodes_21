#O 'for' é usado nessas funções para adicionar elementos às listas
def lista_zeros(n):
    lista=[]
    for i in range(n):
        lista.append(0)
    return lista

def lista_1n(lista):
    crescente=lista[:]
    for i in range (len(lista)):
        crescente[i]=i+1
    return crescente

def lista_2(lista):
    lista_digitada = lista[:]
    for i in range(len(lista)):
        lista_digitada[i]=(int(input()))
    return lista_digitada

def lista_inversa(lista):
    lista_inversa = lista[:]
    for i in range(len(lista)):
        lista_inversa[i] = (int(input()))
    lista_inversa.reverse()
    return lista_inversa
        

def main():
    #Digita o tamanho das listas
    número=int(input())

    zeros= lista_zeros(número)
    ordem_crescente = lista_1n(zeros)
    lista_digitada = lista_2(zeros)
    inversa = lista_inversa(zeros)

    #Saída de Dados
    print(zeros,ordem_crescente, lista_digitada, inversa, sep='\n')
    
if __name__=="__main__":
    main()
