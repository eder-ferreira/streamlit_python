from datetime import date
import sqlite3
con = sqlite3.connect('db_academia.db')  # CRIA CONEXÃO
cursor = con.cursor()                    # CRIA CURSOR
# con.close()                              # FECHA O BANCO