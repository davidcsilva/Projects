import math


class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        return self.num1 / self.num2

    def potencia(self):
        return self.num1 ** self.num2

    def raiz_quadrada(self):
        return self.num1 ** (1/2)

    def raiz_cubica(self):
        return self.num1 ** (1/3)

    def seno(self):
        return math.sin(self.num1)

    def cosseno(self):
        return math.cos(self.num1)

    def tangente(self):
        return math.tan(self.num1)

    def logaritmo(self):
        return math.log(self.num1)

    def logaritmo_natural(self):
        return math.log10(self.num1)

    def logaritmo_neperiano(self):
        return math.log(self.num1, math.e)

    def logaritmo_base_10(self):
        return math.log10(self.num1)

    def logaritmo_base_e(self):
        return math.log(self.num1, math.e)

    def logaritmo_base_2(self):
        return math.log2(self.num1)

    def logaritmo_base_3(self):
        return math.log(self.num1, 3)

    def logaritmo_base_4(self):
        return math.log(self.num1, 4)

    def logaritmo_base_5(self):
        return math.log(self.num1, 5)

    def logaritmo_base_6(self):
        return math.log(self.num1, 6)

    def logaritmo_base_7(self):
        return math.log(self.num1, 7)

    def logaritmo_base_8(self):
        return math.log(self.num1, 8)

    def logaritmo_base_9(self):
        return math.log(self.num1, 9)

    def logaritmo_base_10(self):
        return math.log10(self.num1)


def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    calculadora = Calculadora(num1, num2)
    print("Soma: ", calculadora.soma())
    print("Subtração: ", calculadora.subtracao())
    print("Multiplicação: ", calculadora.multiplicacao())
    print("Divisão: ", calculadora.divisao())
    print("Potência: ", calculadora.potencia())
    print("Raiz quadrada: ", calculadora.raiz_quadrada())
    print("Raiz cúbica: ", calculadora.raiz_cubica())
    print("Seno: ", calculadora.seno())
    print("Cosseno: ", calculadora.cosseno())
    print("Tangente: ", calculadora.tangente())
    print("Logaritmo: ", calculadora.logaritmo())
    print("Logaritmo natural: ", calculadora.logaritmo_natural())
    print("Logaritmo neperiano: ", calculadora.logaritmo_neperiano())
    print("Logaritmo base 10: ", calculadora.logaritmo_base_10())
    print("Logaritmo base e: ", calculadora.logaritmo_base_e())
    print("Logaritmo base 2: ", calculadora.logaritmo_base_2())
    print("Logaritmo base 3: ", calculadora.logaritmo_base_3())
    print("Logaritmo base 4: ", calculadora.logaritmo_base_4())
    print("Logaritmo base 5: ", calculadora.logaritmo_base_5())
    print("Logaritmo base 6: ", calculadora.logaritmo_base_6())
    print("Logaritmo base 7: ", calculadora.logaritmo_base_7())
    print("Logaritmo base 8: ", calculadora.logaritmo_base_8())
    print("Logaritmo base 9: ", calculadora.logaritmo_base_9())
    print("Logaritmo base 10: ", calculadora.logaritmo_base_10())


if __name__ == "__main__":
    main()
