numeros = []  # Inicializa o array para armazenar os números
soma = 0
continuar = 'S'  # Inicializa a variável para controle do loop

while continuar.upper() == 'S':  # Continua enquanto a resposta for 'S' ou 's'
    num = int(input('Digite um número: '))  # Solicita a entrada do número e converte para inteiro
    numeros.append(num)  # Adiciona o número ao array
    soma += num  # Soma o número digitado
    continuar = input('Deseja continuar? [S/N]: ')  # Pergunta se deseja continuar

print('Os números digitados são:', numeros)
print('A soma dos números é:', soma)


