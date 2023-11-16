
Como criar um CRUD WEB em python | Streamlit #1
https://www.youtube.com/watch?v=9mnNSMCu3dI&t=52s

Conectando ao banco de dados com python | Streamlit #2
https://www.youtube.com/watch?v=lOyCICREgy8





from datetime import date
import sqlite3
con = sqlite3.connect('db_academia.db')  # CRIA CONEXÃO
cursor = con.cursor()                    # CRIA CURSOR
# con.close()                              # FECHA O BANCO

# CRIA TABELA
# def create_table():
#     cursor.execute("CREATE TABLE IF NOT EXISTS'tb_usuario'(Id INTEGER,nome_usuario TEXT,email_usuario TEXT,senha_usuario TEXT,data_cadastro TEXT)")
#     con.commit()
#     print("Tabela db_usuario criada com sucesso!")
#     con.close()
# CADASTRA
# CRUD

# def cadastrar_usuario():
#     print("\n<<<<<= CADASTRAR USUARIO =>>>>>")
#     nome_usuario = input("Nome completo do usuario: ")
#     email_usuario = input("Informe o e-mail: ")
#     senha_usuario = input("Cadastre uma senha: ")
#     data_cadastro = date.today()
#     cursor.execute(f"INSERT INTO db_usuario VALUES(NULL,'{nome_usuario}','{email_usuario}',"
#                f"'{senha_usuario}','{data_cadastro}')")

# SALVA AS ALTERAÇÕES
# con.commit()

#FECHA A CONEXÃO
# con.close()
# print("Dados cadastrados com sucesso!")
#
# # RECUPERA
# # for row in cursor.execute('SELECT * FROM db_usuario ORDER BY nome_usuario'):
# for row in cursor.execute('SELECT * FROM db_usuario'):
#     print(row)

# ATUALIZA
# id = input("Insira o Id a ser atualizado => ")
# novo_usuario = input("Insira o novo valor para o campo nome => ")
# cursor.execute("UPDATE db_usuario SET nome_usuario = ? WHERE Id = ?",
#                (novo_usuario, id))
# con.commit()
# print(f"Id: {id} atualizado no campo nome para: {novo_usuario}!\n")
# for row in cursor.execute('SELECT * FROM db_usuario'):
#     print(row)

# APAGA
# id = input("Insira o Id a ser apagado => ")
# cursor.execute("DELETE FROM db_usuario WHERE Id=?",(id,))
# con.commit()
# print(f"Id: {id} apagado da tabela usuario!\n")
#
# print("Tabela Atualizada")
# cursor.execute("SELECT * from db_usuario")
# for row in cursor:
#     print(row)
# cursor.close()

# def check_login(self):
#
#     for row in cursor.execute('SELECT * FROM tb_usuario ORDER BY nome_usuario'):
#         print(row)

# RECUPERA
# usuario = input("Insira o usuario => ")
# senha = input("Insira a senha => ")
# usuario = 'root'
# senha = 'root'
# for row in cursor.execute("SELECT * FROM tb_usuario WHERE nome_usuario=? and senha_usuario=?",
#                           (usuario, senha)):
#     print(row)

# usuario = 'root'
# senha = 'root'
# user = cursor.execute("SELECT nome_usuario FROM tb_usuario WHERE id=13")
# for row in user:
#     print(row)


usuario = 'eder ferreira'
senha = 'eder'
user = cursor.execute("SELECT nome_usuario FROM tb_usuario WHERE nome_usuario =?", (usuario,))
for row in user:
    print(f"Usuario: {row}")

senha = cursor.execute("SELECT senha_usuario FROM tb_usuario WHERE senha_usuario =?", (senha,))
for row in senha:
    print(f"Senha: {row}")

if user == usuario and senha == senha:
    print("Login bem-sucedido!")

    print("Ok logado!!")
else:
    print("Login ou senha incorretos!!")