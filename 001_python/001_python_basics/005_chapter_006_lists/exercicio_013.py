'''
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior
temperatura, assim como a temperatura média.
'''
T = [-10, -8, 0, 1, 2, 5, -2, -4]

# Utilizando as funções nativas do Python
menor_temp = min(T)
maior_temp = max(T)
media_temp = sum(T) / len(T)

print(f"Menor temperatura: {menor_temp}°C")
print(f"Maior temperatura: {maior_temp}°C")
print(f"Temperatura média: {media_temp:.2f}°C")
