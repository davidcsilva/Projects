'''
Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada mês, e você
deve considerá-lo para o cálculo de juros do mês seguinte.
'''

# Leitura dos dados de entrada
deposito_inicial = float(input("Digite o valor do depósito inicial (R$): "))
deposito_mensal = float(input("Digite o valor do depósito mensal (R$): "))
taxa_juros = float(
    input("Digite a taxa de juros mensal (ex: 0.5 para 0.5%): "))

# Conversão da taxa de porcentagem para valor decimal
taxa_decimal = taxa_juros / 100

saldo = deposito_inicial
total_depositado = deposito_inicial
mes = 1

print("\n--- EVOLUÇÃO DO SALDO MÊS A MÊS ---")

while mes <= 24:
    # No primeiro mês utiliza apenas o depósito inicial;
    # nos meses seguintes (mês 2 em diante), adiciona o depósito mensal no início do mês.
    if mes > 1:
        saldo += deposito_mensal
        total_depositado += deposito_mensal

    # Cálculo dos juros do mês sobre o saldo atualizado
    juros_mes = saldo * taxa_decimal
    saldo += juros_mes

    print(f"Mês {mes:2d}: R$ {saldo:10.2f} (Juros do mês: R$ {juros_mes:7.2f})")
    mes += 1

# Cálculo do total ganho apenas com juros
total_juros = saldo - total_depositado

print("-" * 50)
print(f"Total investido pelo cliente: R$ {total_depositado:.2f}")
print(f"Valor final acumulado:        R$ {saldo:.2f}")
print(f"Total ganho em juros:         R$ {total_juros:.2f}")
