

numeros = []  # Inicializa o array vazio
i = 0
soma = 0


while i < 2:
    num = int(input('Digite um número: '))  # Solicita a entrada do número e converte para inteiro
    numeros.append(num)  # Adiciona o número ao array
    i += 1  # Incrementa o valor de i
    soma=soma + num
   
print('Os números digitados são:', numeros)
print('A soma:', soma)

# maior(numeros)
def maior(numeros):
    return numeros[0] > numeros[1]  # Retorna True se o primeiro número for maior, senão False

# Exemplo de uso
resultado = maior(numeros)

if resultado:
    print('O primeiro número é maior que o segundo.')
else:
    print('O segundo número é maior que primeiro.')






