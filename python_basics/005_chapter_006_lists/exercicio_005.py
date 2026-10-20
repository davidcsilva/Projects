'''
Altere o programa abaixo de forma a poder trabalhar com
vários comandos digitados de uma só vez. Atualmente, apenas um comando pode
ser inserido por vez. Altere-o de forma a considerar operação como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos
e, finalmente, a saída do programa. 

último = 10
fila = list(range(1,último+1))
while True:
print("\nExistem %d clientes na fila" % len(fila))
print("Fila atual:", fila)
print("Digite F para adicionar um cliente ao fim da fila,")
print("ou A para realizar o atendimento. S para sair.")
operação = input("Operação (F, A ou S):")
if operação == "A":
		if(len(fila))>0:
			atendido = fila.pop(0)
			print("Cliente %d atendido" % atendido)
		else:
			print("Fila vazia! Ninguém para atender.")
elif operação == "F":
		
último+=1 # Incrementa o ticket do novo cliente
		fila.append(último)
elif operação == "S":
		break
else:
		print("Operação inválida! Digite apenas F, A ou S!")

'''

último = 10
fila = list(range(1, último + 1))

while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")

    operações = input("Operação (ex: FFFAAAS): ").upper()

    sair = False
    for operação in operações:
        if operação == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação == "F":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
            print("Cliente %d adicionado à fila" % último)
        elif operação == "S":
            sair = True
            break
        else:
            print("Operação '%s' inválida! Digite apenas F, A ou S!" % operação)

    if sair:
        print("Saindo do programa...")
        break
