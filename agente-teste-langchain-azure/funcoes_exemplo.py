# funcoes_exemplo.py

# A função soma dois números.
def soma(a, b):
    return a + b

# A função subtrai dois números.
def subtrair(a, b):
    return a - b

# A função multiplica dois números, com tratamento de erro.
def multiplicar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("A entrada deve ser um número inteiro ou de ponto flutuante.")
    return a * b

# A função divide dois números, com tratamento de erro.
def dividir(a, b):
    # Trata a divisão por zero.
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b