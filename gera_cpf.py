import os
import random
print('Bem-vindo ao Gerador de CPF!')

while True:
    cpf_input = ''
    soma_cpf = 0
    multi = 10
    
    for i in range(9):
        cpf_input += str(random.randint(0, 9))    

    for digito in cpf_input:     
        soma_cpf += multi*(int(digito))
        multi -= 1

    mult_cpf = soma_cpf * 10
    ver1_cpf = mult_cpf % 11
    ver1_cpf = 0 if ver1_cpf > 9 else ver1_cpf
            
    soma_cpf = 0
    multi = 11
    cpf_input = cpf_input + str(ver1_cpf)

    for digito in cpf_input:
        soma_cpf += multi*(int(digito))
        multi -= 1

    mult_cpf = soma_cpf * 10
    ver2_cpf = mult_cpf % 11
    ver2_cpf = 0 if ver2_cpf > 9 else ver2_cpf
            
    cpf_input = cpf_input + str(ver2_cpf)

    print(f'O CPF gerado é {cpf_input}.')
    
    saida = input('Digite 0 para sair. \
Qualquer outro caractere dará continuidade. \
Ao sair desta tela, seu CPF será apagado do terminal. ')
    
    if saida == '0':
        print('Saindo...')
        break
    else:
        os.system('cls')
