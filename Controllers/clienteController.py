import Services.conection as db
import Models.cliente as cliente
import Models.produto as produto


def cadastrar(cliente):  # vem do models
    count = db.cursor.execute("""
    INSERT INTO tb_usuario(nome_usuario,email_usuario,senha_usuario,ocupacao,dt_cadastro)
    VALUES(?,?,?,?,?)""",
        (cliente.nome_usuario, cliente.email_usuario, cliente.senha_usuario, cliente.ocupacao, cliente.dt_cadastro))
    db.con.commit()


def listar():
    count = db.cursor.execute("""SELECT * FROM tb_usuario""").rowcount
    list = []

    for row in db.cursor.fetchall():
        list.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4], row[5]))
    return list


def excluir(id):
    count = db.cursor.execute("""
    DELETE FROM tb_usuario WHERE id = ?""",
                              (id,)).rowcount
    db.con.commit()


def editar(id):
    count = db.cursor.execute("""
    SELECT FROM tb_usuario WHERE id = ?""",
                              (id,)).rowcount
    db.cursor.commit()


def carregar_dados():
    count = db.cursor.execute('''
    SELECT * FROM tb_produto''').rowcount
    list = []

    for row in db.cursor.fetchall():
        list.append(produto.Produto(row[0], row[1], row[2], row[3], row[4]))
    return list

def carregar_dados_grafico():
    count = db.cursor.execute('''
    SELECT * FROM tb_produto''').rowcount
    descricao =[]
    quantidade = []

    for row in db.cursor.fetchall():
        descricao.append(produto.Produto(row[1]))
        quantidade.append(produto.Produto(row[2]))
    return descricao,quantidade