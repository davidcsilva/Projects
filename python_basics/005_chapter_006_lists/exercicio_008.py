'''
Modifique o primeiro exemplo abaixo de forma a realizar
a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de
saída do while.

x=0
while x<len(L):
if L[x]==p:
		achou=True ❷
		break ❸
x+=1
if achou: ❹
print("%d achado na posição %d" % (p,x))
else:
print("%d não encontrado" % p)

'''
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = 3

x = 0
while x < len(L):
    if L[x] == p:
        break
    x += 1

if x < len(L):
    print("%d achado na posição %d" % (p, x))
else:
    print("%d não encontrado" % p)
