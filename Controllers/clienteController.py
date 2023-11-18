import Services.conection as db
import Models.cliente as cliente


def cadastrar(cliente):  # vem do models
    db.cursor.execute("""INSERT INTO tb_usuario(nome_usuario,email_usuario,senha_usuario,ocupacao,dt_cadastro)
        VALUES(?,?,?,?,?)""", (
    cliente.nome_usuario, cliente.email_usuario, cliente.senha_usuario, cliente.ocupacao, cliente.dt_cadastro))
    db.con.commit()


def selecionar():
    db.cursor.execute('SELECT * FROM tb_usuario')
    userList = []

    for row in db.cursor.fetchall():
        userList.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4], row[5]))

    return userList
