from time import sleep

def remover_casas_decimais(numero, casas_decimais):
    multiplicador = 10 ** casas_decimais
    numero_sem_casas = int(numero * multiplicador) / multiplicador
    return numero_sem_casas


num = input("Digite uma dízima para saber a sua fração geratriz: ")

if "," in num:
    num.replace(",", ".")

inteiro, decimal = num.split(".")
quantidade = len(decimal)


num2 = float(num)


i = 0
j = 0
fracao = 0
while i <= 10000:
    i += 1
    j = 0
    if fracao == num2:
        break
    
    while j <= 1000:
        j += 1
        valor = i/j
        
        fracao = remover_casas_decimais(valor, quantidade)
        
        if fracao == num2:
            numerador = i
            denominador = j
            break


print(numerador, "/",denominador)

sleep(0.5)

input("Pressione qualquer tecla para sair...")