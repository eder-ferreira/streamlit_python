import sqlite3
# con = sqlite3.connect('academia.db')        # CRIA CONEXÃO
con = sqlite3.connect('academia.db', check_same_thread=False)
cursor = con.cursor()                       # CRIA CURSOR
# con.close()                                # FECHA O BANCO

