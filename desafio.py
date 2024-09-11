import os
menu = """
    *****Banco Isa*****
      Operação
        [d] Depósito
        [s] Sacar
        [e] Extrato
        [q] Sair
        => """ 

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3




while True:

    opcao = input(menu)

    if opcao == "d":
        os.system('cls')
        print ("Opção escolhida: Depósito")
        deposito = float( input ("Informe o valor a ser depositado: "))
        saldo+= deposito
        extrato.append(f"Operação: D + R$ {deposito} | Saldo: R$ {saldo}")
        print (f"Foi depositado {deposito} a sua conta e o valor do saldo atual é de {saldo} ")

    elif opcao == "s":
        os.system('cls')
        print("Opção escolhida: Saque")
        if numero_saques < LIMITE_SAQUES:
            print(f"Seu saldo em conta é de {saldo}")
            valor_saque = float(input("Informe o valor para saque: "))
            if (valor_saque <= saldo) and (valor_saque <= limite):
                saldo-= valor_saque
                numero_saques+= 1
                extrato.append(f"Operação: S - R$ {valor_saque} | Saldo: R$ {saldo}")
                print(f"Saque realizado com sucesso seu saldo atual é {saldo} ")
            elif valor_saque > saldo:
                print("Não tem saldo suficiente para essa operação.")
            elif valor_saque >= limite:
                print("Não é possível realizar a operação valor limite de saque  excedido.")
        else:
            print("Não é mais possível realizar essa operação, pois foi excedido o limite de saque do dia")        
                    


    elif opcao == "e":
        os.system('cls')
        print("Opção escolhida: Extrato")
        if not extrato:
            print("Não foram realizadas movimentações")  
        else:
           for operacao in extrato:
               print(operacao)      

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")