from model.Produto import Produto


class ProdutoDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarProdutos(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM produto ORDER BY id'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            produto = Produto()
            produto.id = item[0]
            produto.nome = item[1]
            produto.departamento = item[2]
            produto.codbar = item[3]

            lista.append(produto)

        return lista

    def selecionarProduto(self, id) -> Produto:
        c = self.connection.cursor()
        c.execute(f"SELECT * FROM produto WHERE id = {id}")
        recset = c.fetchone()
        c.close()

        print(recset)

        produto = Produto()
        produto.id = recset[0]
        produto.nome = recset[1]
        produto.departamento = recset[2]
        produto.codbar = recset[3]

        return produto

    def inserirProduto(self, produto: Produto) -> Produto:
        c = self.connection.cursor()
        c.execute("""
            insert into produto(id, nome, departamento, codbar)
            values({}, '{}', '{}', '{}')
        """.format(produto.id, produto.nome, produto.departamento, produto.codbar))

        self.connection.commit()

    def alterarProduto(self, produto: Produto) -> Produto:
        c = self.connection.cursor()
        c.execute("""
            update produto
            SET nome = '{}', departamento = '{}', codbar = '{}'
            WHERE id = '{}';
        """.format(produto.nome, produto.departamento, produto.codbar, produto.id))

        self.connection.commit()

    def excluirProduto(self, produto: Produto) -> Produto:
        c = self.connection.cursor()
        c.execute("""
            delete from produto
            where id = '{}'
        """.format(produto.id))
        self.connection.commit()
