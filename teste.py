final_arquivo = False
string_vazia = ''
lista=[]

meu_arquivo = open('times.txt', 'r')

print('Times que participarão deste campeonato:')

while not final_arquivo:
    linha = meu_arquivo.readline()
    if linha == string_vazia:
        final_arquivo = True
    else:
        time = linha.rstrip()
        lista.append(time)
        

meu_arquivo.close()
lista.sort()

print(lista)

