#cadastro de medicamentos


medicamentos = []

n_medicamentos = 1

def menu() :
    option = int(input('''
[1] - Cadastrar medicamento
[2] - Consultar medicamento
[3] - Editar itens do medicamento
[4] - Sair do programa



'''))

    return option

def cadastra_medicamento() :
    medicamento_nome = input('Digite o nome do medicamento: ')
    medicamento_id = input('Digite o id do medicamento: ')
    medicamento_lote = input('Digite o lote do medicamento: ')
    medicamentos_dados = (medicamento_nome,medicamento_id,medicamento_lote)
    medicamentos.append(medicamentos_dados)
    print(medicamentos)
    print('medicamento adicionado')

def mostrar_medicamento() :
    for medicamento in medicamentos:
      print(f'''
      Nome: {medicamento_nome}
      id: {medicamento_id}
      lote: {medicamento_lote}''')


def programa() :

    while True:
        option = menu()

        if option == 1 :
            cadastra_medicamento()
        if option == 2 :
            mostrar_medicamento()
        if option == 4 :
          break

programa()