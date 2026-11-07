'''
Modifique o programa para trabalhar com duas filas. Para facilitar
seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendi-
mento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.
'''

último_1 = 10
último_2 = 10

fila_1 = list(range(1, último_1 + 1))
fila_2 = list(range(1, último_2 + 1))

while True:
    print("\n" + "=" * 40)
    print("Fila 1 (%d clientes): %s" % (len(fila_1), fila_1))
    print("Fila 2 (%d clientes): %s" % (len(fila_2), fila_2))
    print("=" * 40)
    print("Comandos: F (chegada Fila 1), G (chegada Fila 2)")
    print("          A (atender Fila 1), B (atender Fila 2)")
    print("          S (sair)")

    operações = input("Operações (ex: FFGAABB S): ").upper()

    sair = False
    for operação in operações:
        if operação == "F":
            último_1 += 1
            fila_1.append(último_1)
            print("Cliente %d adicionado à Fila 1" % último_1)

        elif operação == "G":
            último_2 += 1
            fila_2.append(último_2)
            print("Cliente %d adicionado à Fila 2" % último_2)

        elif operação == "A":
            if len(fila_1) > 0:
                atendido = fila_1.pop(0)
                print("Cliente %d atendido da Fila 1" % atendido)
            else:
                print("Fila 1 vazia! Ninguém para atender.")

        elif operação == "B":
            if len(fila_2) > 0:
                atendido = fila_2.pop(0)
                print("Cliente %d atendido da Fila 2" % atendido)
            else:
                print("Fila 2 vazia! Ninguém para atender.")

        elif operação == "S":
            sair = True
            break

        else:
            print("Operação '%s' inválida!" % operação)

    if sair:
        print("Saindo do programa...")
        break
