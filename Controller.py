from Models import *
from DAO import *
from datetime import datetime


class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria salva com sucesso!')
        else:
            print('Categoria já cadastrada.')


    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) == 0:
            print('Categoria não existe.')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')
            # TODO: Colocar sem categoria no estoque

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()
        produto = DaoProdutos.ler()
        fornecedor = DaoFornecedor.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, Categoria('Sem categoria')), x.quantidade)
                           if (x.produto.categoria.categoria == categoriaRemover) else (x), estoque))
        
        produto = list(map(lambda x: Produtos(x.nome, x.preco, Categoria('Sem categoria'))
                           if (x.categoria.categoria == categoriaRemover) else (x), produto))
        
        fornecedor = list(map(lambda x: Fornecedor(x.nome, x.cnpj, x.telefone, Categoria('Sem categoria'))
                              if (x.categoria.categoria == categoriaRemover) else(x), fornecedor))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + 
                               i.produto.categoria.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

        with open('produtos.txt', 'w') as arq:
            for i in produto:
                arq.writelines(i.nome + '|' + i.preco + '|' + 
                               i.categoria.categoria)
                arq.writelines('\n')

        with open('fornecedor.txt', 'w') as arq:
            for i in fornecedor:
                arq.writelines(i.nome + '|' + i.cnpj + '|' +
                               i.telefone + '|' + i.categoria.categoria)
                arq.writelines('\n')


    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('Categoria alterada com sucesso!')
                #TODO: Alterar categoria do estoquer e produto
            else:
                print('A categoria para qual deseja alterar já existe.')

        else:
            print('A categoria que deseja alterar não existe.')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

        estoque = DaoEstoque.ler()
        produto = DaoProdutos.ler()
        fornecedor = DaoFornecedor.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, Categoria(categoriaAlterada)), x.quantidade)
                           if (x.produto.categoria.categoria == categoriaAlterar) else (x), estoque))
        
        produto = list(map(lambda x: Produtos(x.nome, x.preco, Categoria(categoriaAlterada))
                           if (x.categoria.categoria == categoriaAlterar) else (x), produto))
        
        fornecedor = list(map(lambda x: Fornecedor(x.nome, x.cnpj, x.telefone, Categoria(categoriaAlterada))
                              if (x.categoria.categoria == categoriaAlterar) else(x), fornecedor))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + 
                               i.produto.categoria.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

        with open('produtos.txt', 'w') as arq:
            for i in produto:
                arq.writelines(i.nome + '|' + i.preco + '|' + 
                               i.categoria.categoria)
                arq.writelines('\n')

        with open('fornecedor.txt', 'w') as arq:
            for i in fornecedor:
                arq.writelines(i.nome + '|' + i.cnpj + '|' +
                               i.telefone + '|' + i.categoria.categoria)
                arq.writelines('\n')


    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia!')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')


class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        ler_est = DaoEstoque.ler()
        ler_prod = DaoProdutos.ler()
        
        produto_existe = list(filter(lambda ler_prod: ler_prod.nome == nome, ler_prod))
        estoque_existe = list(filter(lambda ler_est: ler_est.produto.nome == nome, ler_est))
    
        if len(estoque_existe) > 0:
            print('O produto já está cadastrado no estoque.')

        else:
            if len(produto_existe) > 0:
                DaoEstoque.salvar(Estoque(Produtos(nome, preco, Categoria(categoria)), quantidade))
                print('Produto salvo em estoque.')

            else:
                DaoProdutos.salvar(Produtos(nome, preco, Categoria(categoria)))
                DaoEstoque.salvar(Estoque(Produtos(nome, preco, Categoria(categoria)), quantidade))
                print('Produto cadastrado, e salvo em estoque.')


    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break

            print('O produto foi removido com sucesso!')

        else:
            print('O produto não existe')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + 
                               i.produto.categoria.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')


    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        lerEstoq = DaoEstoque.ler()
        lerProd = DaoProdutos.ler()
        lerCat = DaoCategoria.ler()

        confirmCat = list(filter(lambda x: x.categoria == novaCategoria, lerCat))
        confirmProd = list(filter(lambda x: x.nome == nomeAlterar, lerProd))
        validProd = list(filter (lambda x: x.nome == novoNome, lerProd))
        validPrec = list(filter (lambda x: x.nome == novoNome and x.preco != novoPreco, lerProd))


        if len(confirmCat) > 0:
            if len(confirmProd) > 0:
                if len(validProd) == 0:
                    # Alteração de produto
                    x = list(map(lambda x: Produtos(novoNome, novoPreco, Categoria(novaCategoria)) if (x.nome == nomeAlterar) else (x), lerProd))
                    y = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, Categoria(novaCategoria)), novaQuantidade) if (x.produto.nome == nomeAlterar) else (x), lerEstoq))

                    with open('produtos.txt', 'w') as arq:
                        for i in x:
                            arq.writelines(i.nome + '|' + i.preco + '|' + 
                                           i.categoria.categoria)
                            arq.writelines('\n')

                    with open('estoque.txt', 'w') as arq:
                        for i in y:
                            arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + 
                                           i.produto.categoria.categoria + '|' + str(i.quantidade))
                            arq.writelines('\n')

                    
                    print('Produto alterado com sucesso!')

                else:
                    if len(validPrec) > 0:
                        # Alteração de valor
                        x = list(map(lambda x: Produtos(novoNome, novoPreco, Categoria(novaCategoria)) if (x.nome == novoNome) else (x), lerProd))
                        y = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, Categoria(novaCategoria)), novaQuantidade) if (x.produto.nome == nomeAlterar) else (x), lerEstoq))

                        with open('produtos.txt', 'w') as arq:
                            for i in x:
                                arq.writelines(i.nome + '|' + i.preco + '|' + 
                                            i.categoria.categoria)
                                arq.writelines('\n')
                        
                        with open('estoque.txt', 'w') as arq:
                            for i in y:
                                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + 
                                            i.produto.categoria.categoria + '|' + str(i.quantidade))
                                arq.writelines('\n')
                        print('Valor alterado com sucesso!')

                    else:
                        print('O novo produto já está cadastrado.')
                                      
            else:
                print('Produto que deseja alterar não está cadastrado.')

        else:
            print('A categoria informada não existe.')


    def adicionarProduto(self, nome, quantidade):
        lerEstoq = DaoEstoque.ler()
        temp = []
        
        for i in lerEstoq:
            if i.produto.nome == nome:
                i.quantidade = int(i.quantidade) + int(quantidade)

            temp.append([Produtos(i.produto.nome, i.produto.preco, Categoria(i.produto.categoria.categoria)), i.quantidade])

            arq = open('estoque.txt', 'w')
            arq.write('')
            
        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome + '|' + i[0].preco + '|' + i[0].categoria.categoria + '|' + str(i[1]))
                arq.writelines('\n')


    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio.')

        else:
            print('========== Produtos ==========')
            for i in estoque:
                print(f'Nome: {i.produto.nome}')
                print(f'Preço: {i.produto.preco}')
                print(f'Categoria: {i.produto.categoria.categoria}')
                print(f'Quantidade: {i.quantidade}')
                print('----------------')


class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        '''
        return 1: Produto não existe em estoque
        return 2: Quantidade insuficiente em estoque
        return 3: venda efetuada com sucesso.
        '''

        lerEstoq = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in lerEstoq:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if int(i.quantidade) >= int(quantidadeVendida):
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, Categoria(i.produto.categoria.categoria)),
                                        quantidadeVendida, Funcionario(vendedor, None, None, None, None, None), 
                                        Cliente(comprador, None, None, None, None, None))
                        
                        valorCompra = int(quantidadeVendida) * float(i.produto.preco)

                        DaoVendas.salvar(vendido)
                        print('Venda efetuada com sucesso!')
                        

            temp.append([Produtos(i.produto.nome, i.produto.preco, Categoria(i.produto.categoria.categoria)), i.quantidade])
                    
        arq = open('estoque.txt', 'w')
        arq.write('')

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome + '|' + i[0].preco + '|' + i[0].categoria.categoria + '|' + str(i[1]))
                arq.writelines('\n')

            
        if existe == False:
            print('O produto não existe.')
            return 1

        elif not quantidade:
            print('A quantidade não contém em estoque.')
            return 2

        else:
            return 3, print(valorCompra)


    def relatorioVendas(self):
        vendas = DaoVendas.ler()
        produtos = []

        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade = int(i.quantidadeVendida)
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))

            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': x['quantidade'] + quantidade} 
                                    if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})
        
            ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse = True)

        a = 1
        for i in ordenado:
            print(f'----- Produto {a} -----\n'
                  f"Nome de produto: {i['produto']}\n"
                  f"Quantidade vendida: {i['quantidade']}\n")
            a+=1


    def mostrarVendas(self, dataInicio, dataFinal):
        lerVendas = DaoVendas.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataFinal1 = datetime.strptime(dataFinal, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1
                                         and datetime.strptime(x.data, '%d/%m/%Y') <= dataFinal1, lerVendas))

        cont = 1
        total = 0

        for i in vendasSelecionadas:
            print(f'----- Venda {cont} -----\n'
                  f'Nome: {i.itensVendidos.nome}\n'
                  f'Categoria: {i.itensVendidos.categoria.categoria}\n'
                  f'Data: {i.data}\n'
                  f'Quantidade: {i.quantidadeVendida}\n'
                  f'Cliente: {i.comprador.fidelidade}\n'
                  f'Vendedor: {i.vendedor.clt}\n')
            
            total = float(i.itensVendidos.preco) * int(i.quantidadeVendida)
            cont += 1
            print(f'Total: {total}\n'
                  f'---------------\n')


class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        lerForn = DaoFornecedor.ler()
        lerCat = DaoCategoria.ler()

        validForn = list(filter(lambda x: x.cnpj == cnpj, lerForn))
        validCat = list(filter(lambda x: x.categoria == categoria, lerCat))
        validTel = list(filter(lambda x: x.telefone == telefone, lerForn))
        
        if len(validCat) > 0:
            if len(validForn) == 0:
                if len(validTel) == 0:
                    DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, Categoria(categoria)))
                    print('Fornecedor salvo com sucesso!')
                else:
                    print('Outro fornecedor já utiliza esse telefone')
            else:
                print('CNPJ já cadastrado')
        else:
            print('Categoria do fornecedor não existe')


    def removerFornecedor(self, cnpj):
        lerForn = DaoFornecedor.ler()

        validForn = list(filter(lambda x: x.cnpj == cnpj, lerForn))

        if len(validForn) > 0:
            for i in range(len(lerForn)):
                if lerForn[i].cnpj == cnpj:
                    del lerForn[i]
                    print('Fornecedor removido com sucesso!')
        else:
            print('Fornecedor não existe')


        with open('fornecedor.txt', 'w') as arq:
            for i in lerForn:
                arq.writelines(i.nome + '|' + i.cnpj + '|' +
                               i.telefone + '|' + i.categoria.categoria)
                arq.writelines('\n')


    def alterarFornecedor(self, cnpj, novoNome, novoTelefone, novaCategoria):
        lerForn = DaoFornecedor.ler()
        lerCat = DaoCategoria.ler()

        confirmcnpj = list(filter(lambda x: x.cnpj == cnpj, lerForn))
        confirmCat = list(filter(lambda x: x.categoria == novaCategoria, lerCat))
        validNome = list(filter(lambda x: x.nome == novoNome, lerForn))
        validTel = list(filter(lambda x: x.telefone == novoTelefone, lerForn))
        validCat = list(filter(lambda x: x.categoria.categoria == novaCategoria, lerForn))

        if len(confirmCat) > 0:
            if len(confirmcnpj) > 0:
                if len(validNome) == 0:
                    x = list(map(lambda x: Fornecedor(novoNome, cnpj, novoTelefone, Categoria(novaCategoria)) if(x.cnpj == cnpj) else (x), lerForn))

                    with open('fornecedor.txt', 'w') as arq:
                        for i in x:
                            arq.writelines(i.nome + '|' + i.cnpj + '|' +
                                           i.telefone + '|' + i.categoria.categoria)
                            arq.writelines('\n')
                    
                    print('Fornecedor alterado com sucesso.')

                else:
                    if len(validTel) == 0:
                        x = list(map(lambda x: Fornecedor(novoNome, cnpj, novoTelefone, Categoria(novaCategoria)) if(x.cnpj == cnpj) else (x), lerForn))

                        with open('fornecedor.txt', 'w') as arq:
                            for i in x:
                                arq.writelines(i.nome + '|' + i.cnpj + '|' +
                                            i.telefone + '|' + i.categoria.categoria)
                                arq.writelines('\n')
                        
                        print('Telefone do fornecedor alterado com sucesso.')

                    else:
                        print('alterações não identificadas.')
            else:
                print('CNPJ não cadastrado.')
        else:
            print('Nova vategoria não existe.')

    def mostrarFornecedor(self):
        lerForn = DaoFornecedor.ler()

        cont = 1
        for i in lerForn:
            print(f'----- Fornecedor {cont} -----\n'
                  f'CNPJ: {i.cnpj}\n'
                  f'Nome: {i.nome}\n'
                  f'Telefone: {i.telefone}\n'
                  f'Categoria: {i.categoria.categoria}\n')
            cont += 1


class ControllerFuncionario:
    def cadastraFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        lerFunc = DaoFuncionario.ler()

        validClt = list(filter(lambda x: x.clt == clt, lerFunc))
        validCpf = list(filter(lambda x: x.cpf == cpf, lerFunc))
        validEmail = list(filter(lambda x: x.email == email, lerFunc))
        validTel = list(filter(lambda x: x.telefone == telefone, lerFunc))

        if len(validClt) == 0:
            if len(validCpf) == 0:
                if len(validEmail) == 0:
                    if len(validTel) == 0:
                        DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                        print('Funcionário cadastrado com sucesso!')
                    else:
                        print('Telefone já cadastrado no sistema.')
                else:
                    print('Email já cadastrado no sistema')
            else:
                print('CPF já cadastrado no sistema.')
        else:
            print('CLT já cadastrada no sistema.')


    def removerFuncionario(self, cltRemover):
        lerFunc = DaoFuncionario.ler()

        confirmFunc = list(filter(lambda x: x.clt == cltRemover, lerFunc))

        if len(confirmFunc) == 0:
            print('Funcionário não está cadastrado.')
        else:
            for i in range(len(lerFunc)):
                if lerFunc[i].clt == cltRemover:
                    del lerFunc[i]
                    print('Funcionário removido com sucesso!')
                    break

            with open('funcionarios.txt', 'w') as arq:
                for i in lerFunc:
                    arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' +
                                   i.cpf + '|' + i.email + '|' + i.endereco)
                    arq.writelines('\n')


    def alterarFuncionario(self, clt, telefoneAlterar, emailAlterar, enderecoAlterar):
        lerFunc = DaoFuncionario.ler()

        confirmClt = list(filter(lambda x: x.clt == clt, lerFunc))
        existeTelefone = list(filter(lambda x: x.telefone == telefoneAlterar, lerFunc))
        existeEmail = list(filter(lambda x: x.email == emailAlterar, lerFunc))
        confirmEnd = list(filter(lambda x: x.clt == clt and x.endereco != enderecoAlterar, lerFunc))
        
        def atualizacao():
            x = list(map(lambda x: Funcionario(clt, x.nome, telefoneAlterar, x.cpf, emailAlterar, enderecoAlterar)
                 if (x.clt == clt) else (x), lerFunc))
                    
            with open('funcionarios.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.clt + '|' + i.nome + '|' + 
                                   i.telefone + '|' + i.cpf + '|' +
                                   i.email + '|' + i.endereco)
                    arq.writelines('\n')

                print('Alterações efetuadas com sucesso!')


        if len(confirmClt) > 0:
            if len(existeTelefone) == 0 or len(existeEmail) == 0 or len(confirmEnd) > 0:
                atualizacao()
            else:
                print('Alterações não identificadas.')
        else:
            print('Funcionário não cadastrado.')
        

    def mostrarFuncionario(self):
        lerFunc = DaoFuncionario.ler()

        cont = 1
        for i in lerFunc:
            print(f'----- Funcionário {cont} -----\n'
                  f'CLT: {i.clt}\n'
                  f'Nome: {i.nome}\n'
                  f'Telefone: {i.telefone}\n'
                  f'CPF: {i.cpf}\n'
                  f'Email: {i.email}\n'
                  f'Endereço: {i.endereco}\n')
            cont += 1


class ControllerCliente:
    def cadastrarCliente(self, fidelidade, nome, telefone, cpf, email, endereco):
        lerCli = DaoCliente.ler()

        validFidel = list(filter(lambda x: x.fidelidade == fidelidade, lerCli))
        validCpf = list(filter(lambda x: x.cpf == cpf, lerCli))
        validEmail = list(filter(lambda x: x.email == email, lerCli))
        validTel = list(filter(lambda x: x.telefone == telefone, lerCli))

        if len(validFidel) == 0:
            if len(validCpf) == 0 and len(validEmail) == 0 and len(validTel) == 0:
                DaoCliente.salvar(Cliente(fidelidade, nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso.')
            else:
                if len(validCpf) > 0:
                    print('CPF já cadastrado.')
                else:
                    pass
                if len(validEmail) > 0:
                    print('Email já cadastrado.')
                else:
                    pass
                if len(validTel) > 0:
                    print('Telefone em uso.')
                else:
                    pass
        else:
            print('Código fidelidade em uso.')


    def removerCliente(self, fidelRemover):
        lerCli = DaoCliente.ler()

        validFidel = list(filter(lambda x: x.fidelidade == fidelRemover, lerCli))

        if len(validFidel) == 0:
            print('Código fidelidade não cadastrado.')
        else:
            for i in range(len(lerCli)):
                if lerCli[i].fidelidade == fidelRemover:
                    del lerCli[i]
                    print('Cliente removido com sucesso.')
                    break

            with open('clientes.txt', 'w') as arq:
                for i in lerCli:
                    arq.writelines(i.fidelidade + '|' + i.nome + '|' + 
                                   i.telefone + '|' + i.cpf + '|' +
                                   i.email + '|' + i.endereco)
                    arq.writelines('\n')


    def alterarCliente(self, fidelidade, telefoneAlterar, emailAlterar, enderecoAlterar):
        lerCli = DaoCliente.ler()

        validFidel = list(filter(lambda x: x.fidelidade == fidelidade, lerCli))
        validTel = list(filter(lambda x: x.telefone == telefoneAlterar, lerCli))
        validEmail = list(filter(lambda x: x.email == emailAlterar, lerCli))
        validEnd = list(filter(lambda x: x.fidelidade == fidelidade and x.endereco != enderecoAlterar, lerCli))

        def atualizacao():
            x = list(map(lambda x: Cliente(fidelidade, x.nome, telefoneAlterar, x.cpf, emailAlterar, enderecoAlterar )
                 if (x.fidelidade == fidelidade) else (x), lerCli))
                    
            with open('clientes.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.fidelidade + '|' + i.nome + '|' + 
                                   i.telefone + '|' + i.cpf + '|' +
                                   i.email + '|' + i.endereco)
                    arq.writelines('\n')

                print('Alterações efetuadas com sucesso!')

        if len(validFidel) > 0:
            if len(validTel) == 0 or len(validEmail) == 0 or len(validEnd) > 0:
                atualizacao()
            else:
                print('Alterações não identificadas.')
        else:
            print('Código fidelidade não localizado.')


    def mostrarCliente(self):
        lerCli = DaoCliente.ler()
        cont = 1

        for i in lerCli:
            print(f'----- Cliente {cont} -----\n'
                  f'Fidelidade: {i.fidelidade} \n'
                  f'Nome: {i.nome} \n'
                  f'Telefone: {i.telefone}\n'
                  f'CPF: {i.cpf}\n'
                  f'Email: {i.email}\n'
                  f'Endereço: {i.endereco}\n')
            cont += 1




