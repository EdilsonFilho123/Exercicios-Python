# Nome: Edilson Claudio Silvestrini Filho
# R.A.: 0017/09-1
# Sala: 4º TADS

def menorf(num):
    result = list(str(num))
    result.sort()
    st = "".join(result)
    valor = int(st)
    return valor

def maiorf(num):
    result = list(str(num))
    result.sort(reverse=True)
    st = "".join(result)
    valor = int(st)
    if(valor < 10):
        valor *= 10
    if(valor < 100):
        valor *= 10
    if(valor < 1000):
        valor *= 10
    return valor


limite = int(input('Digite o limite: '))

for i in range(1, (limite+1)):
    passos, sub = 0, i

    while(sub != 6174):
        menor = menorf(sub)
        maior = maiorf(sub)

        if maior == menor:
            break

        sub = maior - menor
        print(sub)
        passos += 1
    
    if passos == 0:
        print(i,": Error: Não Funciona para digitos iguais!!")
    else:
        print(i,": Para chegar no 6174 foram usados", passos, "termos")

