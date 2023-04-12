from Models import *


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))        
        return cat


class DaoProdutos:
    @classmethod
    def salvar(cls, produtos:Produtos):
    # sempre quando for salvar algum dado, sempre lembrar de referenciar o tipo do dado,
    # nesse caso, sempre temos que fazer DaoProdutos.salvar(Produtos(*infos*))
        with open('produtos.txt', 'a') as arq:
            arq.writelines(produtos.nome + '|' + produtos.preco + '|' + 
                           produtos.categoria.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arq:
            cls.produtos = arq.readlines()

        cls.produtos = list(map(lambda x: x.replace('\n', ''), cls.produtos))
        cls.produtos = list(map(lambda x: x.split('|'), cls.produtos))

        prod = []
        for i in cls.produtos:
            prod.append(Produtos(i[0], i[1], Categoria(i[2])))
        return prod


class DaoEstoque:
    @classmethod
    def salvar(cls, estoque: Estoque):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(estoque.produto.nome + '|' + estoque.produto.preco + '|' + 
                           estoque.produto.categoria.categoria + '|' + str(estoque.quantidade))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open ('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        for i in cls.estoque:
            est.append(Estoque(Produtos(i[0], i[1], Categoria(i[2])), i[3]))
        return est


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' +
                           fornecedor.telefone + '|' + fornecedor.categoria.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''),cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], Categoria(i[3])))
        return forn


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoa.txt', 'a') as arq:
            arq.writelines(pessoa.nome + '|' + pessoa.telefone + '|' + 
                           pessoa.cpf + '|' + pessoa.email + '|' + 
                           pessoa.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('pessoa.txt', 'r') as arq:
            cls.pessoa = arq.readlines()

        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
        cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))

        pess = []
        for i in cls.pessoa:
            pess.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return pess


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + '|' + funcionario.nome + '|' + 
                           funcionario.telefone + '|' + funcionario.cpf + '|' +
                           funcionario.email + '|' + funcionario.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))

        func = []
        for i in cls.funcionario:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return func
    

class DaoCliente:
    @classmethod
    def salvar(cls, cliente: Cliente):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(cliente.fidelidade + '|' + cliente.nome + '|' + 
                           cliente.telefone + '|' + cliente.cpf + '|' +
                           cliente.email + '|' + cliente.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.cliente = arq.readlines()

        cls.cliente = list(map(lambda x: x.replace('\n', ''), cls.cliente))
        cls.cliente = list(map(lambda x: x.split('|'), cls.cliente))

        cli = []
        for i in cls.cliente:
            cli.append(Cliente(i[0], i[1], i[2], i[3], i[4], i[5]))
        return cli


class DaoVendas:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + '|' + venda.itensVendidos.preco + '|' +
                           venda.itensVendidos.categoria.categoria + '|' + venda.quantidadeVendida + '|' + 
                           venda.vendedor.clt + '|' + venda.comprador.fidelidade + '|' + 
                           venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], Categoria(i[2])), i[3], Funcionario(i[4], None, None, None, None, None),
                        Cliente(i[5], None, None, None, None, None), i[6]))
        return vend





