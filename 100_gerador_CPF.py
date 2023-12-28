import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador_regressivo = 10 

resultado_digito_1 = 0
for digitos in nove_digitos:
    resultado_digito_1 += int(digitos) * contador_regressivo
    contador_regressivo -= 1

resultado_digito_1 = ((resultado_digito_1 * 10) % 11)
resultado_digito_1 = resultado_digito_1 if resultado_digito_1 <= 9 else 0

#Primeira parte do problema acabou aqui.

#Segunda parte do problema : 
dez_digitos = nove_digitos + str(resultado_digito_1)

contador_regressivo_2 = 11
resultado_digito_2 = 0

for digitos_dos_dez in dez_digitos:
    resultado_digito_2 += int(digitos_dos_dez) * contador_regressivo_2
    contador_regressivo_2 -= 1

resultado_digito_2 = ((resultado_digito_2 * 10) % 11)
resultado_digito_2 = resultado_digito_2 if resultado_digito_2 <= 9 else 0

cpf_gerado = str(dez_digitos) + str(resultado_digito_2)

print(f'\n 1° Digito: {resultado_digito_1}\n 2° Digito: {resultado_digito_2}\n CPF gerado: {cpf_gerado}\n')
print('Quantidade de numeros do cpf: ', len(cpf_gerado))
