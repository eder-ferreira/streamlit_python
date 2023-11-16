import Services.data_base as db

def cadastrar(cliente):  # vem do models
        db.cursor.execute("""INSERT INTO tb_usuario(nome_usuario,email_usuario,senha_usuario,ocupacao)
        VALUES(?,?,?,?)""",(cliente.nome_usuario, cliente.email_usuario, cliente.senha_usuario, cliente.ocupacao))
        db.con.commit()