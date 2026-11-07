'''
O que acontece quando a lista já está ordenada? Rastreie o programa
abaixo, mas com a lista L=[1,2,3,4,5].

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

fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
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
