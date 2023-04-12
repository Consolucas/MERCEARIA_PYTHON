import Controller
import os.path


def criarArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')


criarArquivos('categoria.txt', 'clientes.txt', 'estoque.txt',
              'fornecedor.txt', 'funcionarios.txt', 'produtos.txt',
              'vendas.txt')


if __name__ == '__main__':
    while True:
        local = int(input('Digite 1 para acessar *CATEGORIAS*\n'
                          'Digite 2 para acessar *ESTOQUE*\n'
                          'Digite 3 para acessar *FORNECEDOR*\n'
                          'Digite 4 para acessar *FUNCIONÁRIO*\n'
                          'Digite 5 para acessar *CLIENTE*\n'
                          'Digite 6 para acessar *VENDAS*\n'
                          'Digite 7 para ver os produtos mais vendidos **\n'
                          'Digite 8 para acessar SAIR\n'))

        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input('\nDigite 1 para cadastrar uma categoria\n'
                                    'Digite 2 para remover uma categoria\n'
                                    'Digite 3 para alterar uma categoria\n'
                                    'Digite 4 para mostrar as categorias cadastradas\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    categoria = input('\nDigite a categoria que deseja cadastrar: ')
                    cat.cadastraCategoria(categoria)

                elif decidir == 2:
                    categoria = input('\nDigite a categoria que deseja remover: ')
                    cat.removerCategoria(categoria)

                elif decidir == 3:
                    categoria = input('\nDigite a categoria que deseja alterar: ')
                    novaCategoria = input('Digite a categoria para qual deseja alterar: ')
                    cat.alterarCategoria(categoria, novaCategoria)

                elif decidir == 4:
                    print('\n')
                    cat.mostrarCategoria()

                elif decidir == 5:
                    break

                else:
                    print('\ndigite um número válido.')

        elif local == 2:
            est = Controller.ControllerEstoque()
            while True:
                decidir = int(input('\nDigite 1 para cadastrar um produto\n'
                                    'Digite 2 para remover um produto\n'
                                    'Digite 3 para alterar um produto\n'
                                    'Digite 4 para adicionar quantidade de um produto\n'
                                    'Digite 5 para ver produtos em estoque\n'
                                    'Digite 6 para sair\n'))

                if decidir == 1:
                    nome = input('\nNome do produto: ')
                    preco = input('Preço do produto: ')
                    categoria = input('Categoria do produto: ')
                    quantidade = input('Unidades: ')
                    est.cadastrarProduto(nome, preco, categoria, quantidade)

                elif decidir == 2:
                    nome = input('\nNome do produto que eseja remover: ')
                    est.removerProduto(nome)

                elif decidir == 3:
                    nomeAnti = input('\nNome do produto que deseja alterar: ')
                    nomeNovo = input('Novo nome: ')
                    preco = input('Novo preço: ')
                    categoria = input('Nova categoria: ')
                    quantidade = input('Nova quantidade: ')
                    est.alterarProduto(nomeAnti, nomeNovo, preco, categoria, quantidade)

                elif decidir == 4:
                    nome = input('\nNome do produto: ')
                    quantidade = input('Quantidade adicionada: ')
                    est.adicionarProduto(nome, quantidade)

                elif decidir == 5:
                    print('\n')
                    est.mostrarEstoque()

                elif decidir == 6:
                    break

                else:
                    print('\nDigite um número válido.')

        elif local == 3:
            forn = Controller.ControllerFornecedor()
            while True:
                decidir = int(input('\nDigite 1 para cadastrar fornecedor\n'
                              'Digite 2 para remover fornecedor\n'
                              'Digite 3 para alterar fornecedor\n'
                              'Digite 4 para ver fornecedores\n'
                              'Digite 5 para sair\n'))
                
                if decidir == 1:
                    nome = input('\nNome do fornecedor: ')
                    cnpj = input('CNPJ do fornecedor: ')
                    telefone = input('Telefone do fornecedor: ')
                    categoria = input('Tipo de produto entregue: ')
                    forn.cadastrarFornecedor(nome, cnpj, telefone, categoria)

                elif decidir == 2:
                    cnpj = input('\nCNPJ do fornecedor que deseja remover: ')
                    forn.removerFornecedor(cnpj)

                elif decidir == 3:
                    cnpj = input('\nCNPJ do fornecedor: ')
                    nomeNovo = input('Novo nome do Fornecedor: ')
                    telNovo = input('Novo número de telefone: ')
                    catNovo = input('Nova categoria de produtos: ')
                    forn.alterarFornecedor(cnpj, nomeNovo, telNovo, catNovo)

                elif decidir == 4:
                    print('\n')
                    forn.mostrarFornecedor()

                elif decidir == 5:
                    break

                else:
                    print('\nDigite um número válido.')
                
        elif local == 4:
            func = Controller.ControllerFuncionario()
            while True:
                decidir = int(input('\nDigite 1 para cadastrar um funcionário\n'
                                    'Digite 2 para remover um funcionário\n'
                                    'Digite 3 para alterar um funcionário\n'
                                    'Digite 4 para ver funcionários\n'
                                    'Digite 5 para sair\n'))
                
                if decidir == 1:
                    clt = input('\nNúmero da carteira de trabalho: ')
                    nome = input('Nome do funcionário: ')
                    telefone = input('telefone do funcionário: ')
                    cpf = input('CPF do funcionário: ')
                    email = input('E-mail do funcionário: ')
                    endereco = input('Endereço do funcionário: ')
                    func.cadastraFuncionario(clt, nome, telefone, cpf, email, endereco)

                elif decidir == 2:
                    clt = input('\nCLT do funcionário que deseja remover: ')
                    func.removerFuncionario(clt)
                
                elif decidir == 3:
                    clt = input('\nCLT do Funcionário que deseja alterar: ')
                    telNovo = input('Novo telefone: ')
                    emailNovo = input('Novo e-mail: ')
                    endNovo = input('Novo endereço: ')
                    func.alterarFuncionario(clt, telNovo, emailNovo, endNovo)

                elif decidir == 4:
                    print('\n')
                    func.mostrarFuncionario()

                elif decidir == 5:
                    break

                else:
                    print('\nDigite um número válido.')

        elif local == 5:
            cli = Controller.ControllerCliente()
            while True:
                decidir = int(input('\nDigite 1 para cadastrar um cliente\n'
                                    'Digite 2 para remover um cliente\n'
                                    'Digite 3 para alterar um cliente\n'
                                    'Digite 4 para ver clientes\n'
                                    'Digite 5 para sair\n'))
                
                if decidir == 1:
                    fidelidade = input('\nCódigo do cliente: ')
                    nome = input('Nome do cliente: ')
                    telefone = input('Telefone do cliente: ')
                    cpf = input('CPF do cliente: ')
                    email = input('E-mail do cliente: ')
                    endereco = input('Endereço do cliente: ')
                    cli.cadastrarCliente(fidelidade, nome, telefone, cpf, email, endereco)

                elif decidir == 2:
                    fidelRemover = input('\nCódigo fielidade do cliente que deseja remover: ')
                    cli.removerCliente(fidelRemover)

                elif decidir == 3:
                    fidelidade = input('\nCódigo fidelidade do cliente que deseja alterar: ')
                    telNovo = input('Novo telefone: ')
                    emailNovo = input('E-mail novo: ')
                    endNovo = input('Novo endereço: ')
                    cli.alterarCliente(fidelidade, telNovo, emailNovo, endNovo)

                elif decidir == 4:
                    print('\n')
                    cli.mostrarCliente()

                elif decidir == 5:
                    break

                else:
                    print('\nDigite um número válido.')

        elif local == 6:
            vend = Controller.ControllerVenda()
            while True:
                decidir = int(input('\nDigite 1 para cadastrar venda\n'
                                    'Digite 2 para ver vendas\n'
                                    'Digite 3 para sair\n'))
                
                if decidir == 1:
                    nomeProd = input('\nProduto vendido: ')
                    vendedor = input('Código do funcionário: ')
                    comprador = input('Código do cliente: ')
                    quantidade = input('Quantidade do produto: \n')
                    vend.cadastrarVenda(nomeProd, vendedor, comprador, quantidade)

                elif decidir == 2:
                    dtInicio = input('\nData de início da análise: ')
                    dtFinal = input('Data final da anáise: \n')
                    vend.mostrarVendas(dtInicio, dtFinal)

                elif decidir == 3:
                    break

                else:
                    print('\nDigite um número válido.\n')

        elif local == 7:
            vend = Controller.ControllerVenda()
            vend.relatorioVendas()

        elif local == 8:
            break

        else:
            print('\nDigite um número válido.\n')















