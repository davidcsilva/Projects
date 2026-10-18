'''
Altere o programa anterior para exibir os resultados no mesmo for-
mato de uma tabuada: 2x1 = 2, 2x2=4, ...
'''

x = 1
while x <= 20:
    if x % 2 == 0:
        print(f"2 x {x//2} = {x}")
    x = x + 1
