
import sqlite3

from configs import Configs


class Repo:
    def __init__(self):
        self.__conn = sqlite3.connect(Configs().dbPath, check_same_thread=False)
        self.__cursor = self.__conn.cursor()
        
    def consultarFiles(self):
        self.__cursor.execute("SELECT * FROM FILES;")
        return self.__formatar()
    
    def consultarFilesNames(self):
        self.__cursor.execute("SELECT DESCRICAO FROM FILES;")
        return self.__formatar()
    
    def consultarFileByName(self, name):
        self.__cursor.execute("SELECT * FROM FILES WHERE DESCRICAO = ?;", (name, ))
        file = self.__formatar()
        return file[0]
        
    def createFile(self, descricao, file):
        self.__cursor.execute("INSERT INTO FILES (DESCRICAO, FILE) VALUES (?, ?)", (descricao, file))
        self.__conn.commit()
        
    def deleteFile(self, id):
        self.__cursor.execute("DELETE FROM FILES WHERE ID = ?", (id, ))
        self.__conn.commit()
        
    def __formatar(self):
        headers = [desc[0].lower() for desc in self.__cursor.description]
        dadosFormatados = [dict(zip(headers, data)) for data in self.__cursor.fetchall()]
        return dadosFormatados
    

