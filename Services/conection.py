import sqlite3
con = sqlite3.connect('academia.db')        # CRIA CONEXÃO
cursor = con.cursor()                       # CRIA CURSOR
# con.close()                                # FECHA O BANCO