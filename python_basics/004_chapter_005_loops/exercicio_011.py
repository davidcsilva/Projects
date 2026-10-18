'''
Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.
'''

# Leitura dos dados de entrada
deposito_inicial = float(input("Digite o valor do depósito inicial (R$): "))
taxa_juros = float(
    input("Digite a taxa de juros mensal (ex: 0.5 para 0.5%): "))

# Conversão da taxa de porcentagem para valor decimal
taxa_decimal = taxa_juros / 100

saldo = deposito_inicial
mes = 1

print("\n--- EVOLUÇÃO DO SALDO MÊS A MÊS ---")

while mes <= 24:
    juros_mes = saldo * taxa_decimal
    saldo += juros_mes
    print(f"Mês {mes:2d}: R$ {saldo:10.2f} (Juros do mês: R$ {juros_mes:7.2f})")
    mes += 1

# Cálculo do total ganho com juros no período de 24 meses
total_juros = saldo - deposito_inicial

print("-" * 45)
print(f"Valor inicial investido: R$ {deposito_inicial:.2f}")
print(f"Valor final acumulado:   R$ {saldo:.2f}")
print(f"Total ganho em juros:    R$ {total_juros:.2f}")
