'''
Modifique o programa abaixo para ordenar a lista em
ordem decrescente. L=[1,2,3,4,5] deve ser ordenada como L=[5,4,3,2,1].

L=[7,4,3,12,8]
fim=5 ❶
while fim > 1: ❷
trocou=False ❸
x=0 ❹
while x<(fim-1): ❺
		if L[x] > L[x+1]: ❻
			trocou=True ❼
			temp=L[x] ❽
			L[x]=L[x+1]
			L[x+1]=temp
		x+=1
if not trocou: ❾
		break
fim-=1 ❿
for e in L:
print(e)

'''
L = [1, 2, 3, 4, 5]

fim = len(L)
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] < L[x + 1]:  # Operador alterado de > para <
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1

for e in L:
    print(e)
