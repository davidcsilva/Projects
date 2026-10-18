'''
Escreva um programa que pergunte o valor inicial de uma dívida e
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
de meses para que a dívida seja paga, o total pago e o total de juros pago.
'''

# Leitura dos dados de entrada
divida_inicial = float(input("Digite o valor inicial da dívida (R$): "))
taxa_juros = float(input("Digite o juro mensal (%): "))
pagamento_mensal = float(input("Digite o valor do pagamento mensal (R$): "))

taxa_decimal = taxa_juros / 100
juros_primeiro_mes = divida_inicial * taxa_decimal

# Verificação se o pagamento cobre ao menos os juros
if pagamento_mensal <= juros_primeiro_mes:
    print("\nErro: O pagamento mensal é menor ou igual aos juros gerados por mês.")
    print("Com esse valor, a dívida nunca será paga!")
else:
    saldo = divida_inicial
    meses = 0
    total_pago = 0.0
    total_juros = 0.0

    while saldo > 0:
        juros_mes = saldo * taxa_decimal

        # No último mês, o pagamento ajusta-se para não ultrapassar o saldo restante
        if saldo + juros_mes < pagamento_mensal:
            pagamento_efetivo = saldo + juros_mes
        else:
            pagamento_efetivo = pagamento_mensal

        total_juros += juros_mes
        saldo = (saldo + juros_mes) - pagamento_efetivo
        total_pago += pagamento_efetivo
        meses += 1

    print("\n--- RESULTADO DA QUITAÇÃO DA DÍVIDA ---")
    print(f"Número de meses necessários: {meses}")
    print(f"Total pago:                  R$ {total_pago:.2f}")
    print(f"Total de juros pago:         R$ {total_juros:.2f}")
