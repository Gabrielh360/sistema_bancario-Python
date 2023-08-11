menu = """

[1] Depositar 🏧
[2] Sacar 💳
[3] Extrato 📋
[4] Transferência 💸
[0] Sair 👋
 
=> """

saldo = 0
limite = 500
limite_transferencia = 10000000
extrato = ""
satatus = ""
conta = ""
transferir = saldo
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            print("""
                  ✅ depósito realizado com sucesso!""")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("""
                ⚠ Operação falhou! O valor informado é inválido.""")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("""
                  ⚠ Operação falhou! Você não tem saldo suficiente.""")

        elif excedeu_limite:
            print("""
                  ⚠ Operação falhou! O valor do saque excede o limite.""")

        elif excedeu_saques:
            print("""
                  ⚠ Operação falhou! Número máximo de saques excedido.""")

        elif valor > 0:
            print("""
                  ✅ Saque realizado com sucesso!""")
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("""
                  ⚠ Operação falhou! O valor informado é inválido.""")

    elif opcao == "3":
        print("\n----------------- 📋 EXTRATO 📋 -----------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------------------------")

    elif opcao == "4":
        valor = float(input("Informe o valor da transferência: "))
        conta = input("Informe pra quem ira traferir o valor: ")

        excedeu_saldo = valor > saldo

        excedeu_limite_transferencia = valor > limite

        if excedeu_saldo:
            print("""
                  ⚠ Operação falhou! Você não tem saldo suficiente.""")

        elif excedeu_limite_transferencia:
            print("""
                  ⚠ Operação falhou! O valor da transferência excede o limite.""")

        elif valor > 0:
            print("""
                  ✅ Transferência realizada com sucesso!""")
            saldo -= valor
            extrato += f"Transferência: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("""
                  ⚠ Operação falhou! O valor informado é inválido.""")
        
        
    elif opcao == "0":
        print("""
              Obrigado por usar nosso sistema bancário, volte sempre! 👋
              """)
        break

    else:
        print("""
              ❌ Operação inválida, por favor selecione novamente a operação desejada.""")
 