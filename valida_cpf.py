import os
soma_cpf = 0
multi = 10
print("Bem-vindo ao Validador de CPF!")

while True:
    cpf_input = input('Digite seu CPF em números: ')
    
    if not cpf_input.isnumeric():
        os.system('cls')
        print('Digite números, sem letras ou espaços vazios.')
        continue
    
    char_repeat = cpf_input == cpf_input[0] * len(cpf_input)
    if char_repeat:
        os.system('cls')
        print('Digite números distintos.')
        continue
    
    if len(cpf_input) != 11:
        os.system('cls')
        print('Digite os 11 números do CPF.')
        continue

    else:
        os.system('cls')
        cpf_v = cpf_input[:9]

        for digito in cpf_v:     
            soma_cpf += multi*(int(digito))
            multi -= 1

        mult_cpf = soma_cpf * 10
        ver1_cpf = mult_cpf % 11
        ver1_cpf = 0 if ver1_cpf > 9 else ver1_cpf
            
        soma_cpf = 0
        multi = 11
        cpf_v = cpf_v + str(ver1_cpf)

        for digito in cpf_v:
            soma_cpf += multi*(int(digito))
            multi -= 1

        mult_cpf = soma_cpf * 10
        ver2_cpf = mult_cpf % 11
        ver2_cpf = 0 if ver2_cpf > 9 else ver2_cpf
            
        cpf_calculo = cpf_v + str(ver2_cpf)

        if cpf_input == cpf_calculo:
            print(f'O CPF {cpf_input} é um CPF válido!')
        else:
            print(f'Este CPF não é válido.')

        saida = input('Digite 0 para sair. \
Qualquer outro caractere dará continuidade. \
Ao sair desta tela, seu CPF será apagado do terminal. ')
    
    if saida == '0':
        print('Saindo...')
        break
    else:
        os.system('cls')
