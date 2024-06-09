menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        
        deposito = float((input("Digite o valor do deposito: ")))

        if deposito > 0:
            saldo+= deposito   
            extrato+= f'Deposito: R$ {deposito:.2f}\n'  

        else:
            print("A operação falhou! Digite um valor positivo! ")
            
            
    elif opcao == "s":
       
        saque = float(input("Digite o valor do saque: "))

        passou_do_saldo = saque > saldo     

        passou_do_limite = saque > limite

        passou_limite_saques = numero_saques >= LIMITE_SAQUES

        if passou_do_saldo:
            print("Sem saldo!")

            pergunta = input("Você deseja fazer um empréstimo? Sim(s),Não(n)")
            novo_saldo=float(input("Digite o valor do empréstimo: "))
            if pergunta == "s":
                saldo+=novo_saldo
                emprestimo = saldo
                extrato+= f'Empréstimo: R$ {emprestimo:.2f}\n'  

        elif passou_do_limite:
            print("Saque passou do limite!")
            pergunta = input("Você deseja aumentar seu limite? Sim(s),Não(n)")
            limite_novo=float(input("Digite novo limite: "))
            if pergunta == "s":
                limite+=limite_novo

        elif passou_limite_saques:
            print("O número de saque excedeu!")

        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            numero_saques += 1 
        
        else:
            print("Operação inválida,por favor selecione a operação desejada.")
                
       
    elif opcao == "e":
        print("\n************** EXTRATO BANCARIO ******************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("****************************************************")

    elif opcao == "q":
        break

    else:
        print("Operação inválida,por favor selecione a operação desejada.")
     


 




