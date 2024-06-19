# Função do menu
def menu():
    menu_text = """
    • MENU •

    [1] Nova conta
    [2] Listar contas
    [3] Novo usuário
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [7] Sair

    Escolha -> """
    return input(menu_text)

# Função Listar contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta["agencia"]}
            Numero D'Contas: {conta["numero_conta"]}
            Cliente: {conta["usuarios"]["nome"]}
        """
        print(linha)

# Função criar conta
def criar_conta(agencia, usuarios, numero_conta, contas):
    cpf = input("\n    Informe seu CPF novamente: ")
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print("\n     --- Conta criada com sucesso! ---")
            conta = {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuario}
            contas.append(conta)
            return contas
    print("\n    ! O usuario não foi encontrado\n    por favor verifique se suas informações estão corretas!  ")
    return contas

# Função Criar Usuario
def novoUsuario(usuarios):
    cpf = input("\n    Qual seu CPF? ")
    usuario = filtro_usuario(cpf, usuarios)
    if usuario:
        print("\n    ! Usuario Ja existente!")
        return usuarios

    nome = input("\n    Qual seu nome? ")
    data = input("\n    Qual sua data de nascimento?  dd/mm/aaaa: ")
    endereco = input("\n    Qual seu endereço?  Ex: (logradouro - numero da casa - bairro - cidade/sigla estado)  ")
    usuarios.append({"nome": nome, "data": data, "cpf": cpf, "endereco": endereco})
    return usuarios

# Função para filtrar usuarios
def filtro_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False

# Função do deposito
def deposito(saldo, extrato,/,):
    deposito_valor = int(input("\n   Qual valor você que depositar? "))
    if deposito_valor > 0:
        print("\n     -- Deposito feito com sucesso! --")
        saldo += deposito_valor
        extrato += f"\n    Depositado: {deposito_valor}\n"
    else:
        print("Ops, algo deu errado, tente novamente!")
    return saldo, extrato

# Função de saque
def saque(*,saldo, extrato, limite, numero_saques, limite_saques,):
    saque_valor = int(input("\n   Qual valor você quer Sacar? "))
    excedeu_saldo = saque_valor > saldo
    excedeu_limite = saque_valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("\n    ! Voce não tem saldo o suficiente :(!")
    elif excedeu_limite:
        print(f"\n    ! Voce excedeu o limite de R$ {limite} por saque")
    elif excedeu_saques:
        print(f"\n    ! Você excedeu o seu limite de saques diarios {numero_saques}/{limite_saques}")
    elif saque_valor > 0:
        print("\n     -- Saque feito com sucesso!--")
        saldo -= saque_valor
        extrato += f"\n    Sacado: {saque_valor}\n"
        numero_saques += 1
    else:
        print("Ops, algo deu errado, tente novamente!")
    return saldo, extrato, numero_saques

# Função exibir o extrato
def exibir_extrato(saldo,/,*, extrato):
    rooftop = f"\n    ------ Extrato-----\n     total: {saldo}           \n     -------------------\n"
    print(rooftop + extrato)

# Função dos codigos
def codigos():
    
    saldo = 0
    limite = 500
    extrato = ""
    contas = []
    numero_saques = 0
    usuarios = []
    numero_conta = 0
    limite_saques = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()
        
        if opcao == "1":
            numero_conta = len(contas) + 1
            contas = criar_conta(AGENCIA, usuarios, numero_conta, contas)
            
        elif opcao == "2":
            listar_contas(contas)
            
        elif opcao == "3":
            usuarios = novoUsuario(usuarios)
            
        elif opcao == "4":
            saldo, extrato = deposito(saldo, extrato)
            
        elif opcao == "5":
            saldo, extrato, numero_saques = saque(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
            
        elif opcao == "6":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "7":
            break
            
        else:
            print("\n   ! Descupe não entendi, pode repetir?")

codigos()

# Codigo feito por Luiz Hilário : ) 
