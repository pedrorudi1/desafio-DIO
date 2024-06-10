menu = '''
MENU

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

Digite a opção desejada: 
'''

saldo = 0
limite = 500
extrato = ""

numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    
    if (opcao == "d"):
        print("DEPÓSITO")
        valor = float(input('Digite o valor a depositar: R$ '))
        if (valor <= 0):
            print('Valor depositado é inválido.')
        else:
            print('Depósito realizado com sucesso.')
            saldo += valor
            extrato += f'Depósito R$ {valor:.2f}\n'
        
    elif (opcao == "s"):
        print("SAQUE")
        saque = float(input('Digite o valor que deseja sacar: R$ '))
        if (limite_saques == 0):
            print('Você atingiu o limite de saques diários.')
        elif (saque > limite):
            print('O limite desta operação é de R$ 500,00.')
        elif (saldo < saque):
            print('Você não tem limite disponível para esta operação.')
        else:
            print('Saque realizado com sucesso.')
            limite_saques -= 1
            saldo -= saque
            extrato += f'Saque - R$ {saque:.2f}\n'

    elif (opcao == "e"):
        print("EXTRATO")
        print(f'{extrato}\nSaldo disponível: R$ {saldo:.2f}')
            
    elif (opcao == "q"):
        break
    
    else:
        print("Opção inválida, selecione novamente qual operação deseja: ")