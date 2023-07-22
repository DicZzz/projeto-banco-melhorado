def menu(): 
    menu =  """
==========MENU==========
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Criar Conta
  [5] Listar Contas
  [6] Novo Usuario
  [0] Sair
  =>"""
    return input(menu)  



def depositar(saldo, valor, extrato, /):
    valor = float(input("Informe o valor do deposito: R$ "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
 valor = float(input("Informe o valor do saque:R$ "))
 excedeu_saldo = valor >saldo
 excedeu_limite = valor > limite
 excedeu_saques = numero_saques >= limite_saques

 if excedeu_saldo:
          print("Operação falhou!Você naõ tem saldo suficiente!")

 elif excedeu_limite:
             print("Operação falhou! O valor do saque excede o limite.")

 elif excedeu_saques:
             print("Operação falhou! Número maximo de saques excedido.")

 elif valor > 0:
             saldo -= valor
             extrato += f"Saque: R$ {valor:.2f}\n"
             numero_saques += 1
             print("\n=== Saque realiado com Sucesso!===" )

 else:
             print("Operação falhou! O valor informado é invàlido.")

def exibir_extrato(saldo, /,*,extrato):
     print ("\n================ EXTRATO ================")
     print("Não foram realizadas movimentações."if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("============================================")
     
def criar_usuario(usuarios):
      cpf = input("Informe o CPF (somente números):")
      usuario = filtrar_usuario(cpf, usuario)

      if usuario:
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return
      
      nome = input("Informe o nome completo: ")
      data_nascimento = input("Informe a data de nascimneto (dd-mm-aaaa): ")
      endereco = input("Informe o endereço (logradouro, N - Bairro - Cidade/Estado): ")
      usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
      print("=== Usuario criado com Sucesso! ===")

def filtrar_usuario(cpf, usuarios):
      usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]== cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
      cpf = input("Informe o CPF do usuario: ")
      usuario = filtrar_usuario(cpf, usuarios)
      if usuario:
            print("\n=== Conta criada com sucesso! ===")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
      
      print("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
      for conta in contas:
            linha = f"""\
            Agência:\t{conta['agencia']}
            C/C?\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("Informe o valor do depósito:R$ "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque:R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if contas:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação invalida, por favor selecione novamente a operação desejada")
