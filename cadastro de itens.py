# Cria uma lista vazia para armazenar os itens
itens = []

# Define uma função para cadastrar itens
def cadastrar_item():
    # Solicita ao usuário as informações do item a ser cadastrado
    nome = input("Digite o nome do item: ")
    descricao = input("Digite a descrição do item: ")
    preco = float(input("Digite o preço do item: "))

    # Cria um dicionário com as informações do item
    item = {"nome": nome, "descricao": descricao, "preco": preco}

    # Adiciona o item à lista de itens
    itens.append(item)

    # Imprime mensagem de confirmação
    print("Item cadastrado com sucesso!")

# Define uma função para listar os itens cadastrados
def listar_itens():
    # Verifica se há itens cadastrados
    if len(itens) == 0:
        print("Não há itens cadastrados.")
    else:
        # Imprime os itens cadastrados
        for i, item in enumerate(itens):
            print(f"{i+1}. {item['nome']}: {item['descricao']} - R${item['preco']:.2f}")

# Define uma função para excluir um item cadastrado
def excluir_item():
    # Solicita ao usuário o número do item a ser excluído
    num_item = int(input("Digite o número do item a ser excluído: "))

    # Verifica se o número do item é válido
    if num_item <= 0 or num_item > len(itens):
        print("Número inválido.")
    else:
        # Remove o item da lista de itens
        item_removido = itens.pop(num_item-1)

        # Imprime mensagem de confirmação
        print(f"O item '{item_removido['nome']}' foi removido com sucesso!")

# Loop principal do programa
while True:
    # Imprime as opções de ação
    print("\nSelecione uma opção:")
    print("1. Cadastrar um novo item")
    print("2. Listar os itens cadastrados")
    print("3. Excluir um item cadastrado")
    print("4. Sair do programa")

    

    # Solicita ao usuário a opção desejada
    opcao = int(input("Opção selecionada: "))

    # Executa a ação correspondente à opção selecionada
    if opcao == 1:
        cadastrar_item()
    elif opcao == 2:
        listar_itens()
    elif opcao == 3:
        excluir_item()
    elif opcao == 4:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")
