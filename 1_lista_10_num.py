#Lê um número n vezes e os adiciona a uma lista
def lista_1(n):
    lista=[]
    for i in range(n):
        lista.append(int(input()))
    return lista

#Soma todos os números
def soma_lista(lista):
    return sum(lista)

#Multiplica todos os números
def multiplica_lista(lista):
    produto=1
    for i in range (len(lista)):
        produto*= lista[i]
    return produto

def main():
    lista = lista_1(10)
    soma = soma_lista(lista)
    multi = multiplica_lista(lista)
    #Saída de Dados
    print(lista,soma,multi, sep="\n")
    
if __name__=="__main__":
    main()
