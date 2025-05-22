import base64
import sqlite3

conn = sqlite3.connect("database/database.db", check_same_thread=False)
cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS FILES(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         DESCRICAO VARCHAR(100) NOT NULL UNIQUE,
#         FILE BLOB
#     )               
# """)

def adicionarArquivoTent():
    with open("tent.json", "rb") as f:
        file_data = f.read()
    
    file_base64 = base64.b64encode(file_data).decode('utf-8')
    
    descricao = "tent"

    cursor.execute("""
        INSERT INTO FILES (DESCRICAO, FILE)
        VALUES (?, ?)
    """, (descricao, file_base64))
    
    conn.commit()

adicionarArquivoTent()

cursor.close()
conn.close()

