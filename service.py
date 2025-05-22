import base64
import json
from adapter import Adapter
from generator import BaseGenerator
from repo.repo import Repo


class Service:
    def __init__(self):
        self.__adapter = Adapter()
        self.__generator = BaseGenerator()
        self.__conn = Repo()
    
    @classmethod
    def newService(cls):
        return cls()
    
    def adapter(self, req: dict):
        file = req.get("file")
        originalCoordinates = req.get("originalCoordinates")
        newCoordinates = req.get("newCoordinates")
        
        if file is None:
            raise Exception("File is none")
        
        if originalCoordinates is None or len(originalCoordinates) != 3:
            raise Exception("originalCoordinates not valid")
        
        if newCoordinates is None or len(newCoordinates) != 3:
            raise Exception("newCoordinates not valid")
        
        return self.__adapter.convertJsonCoordinates(file, originalCoordinates, newCoordinates)
    
    def generateTent(self, req: dict):
        coordinates = req.get("coordinates")
        type = req.get("type")
        
        if coordinates is None or len(coordinates) != 3:
            raise Exception("coordinates not valid")
        
        if type is None:
            raise Exception("type invalid")
        
        return self.__generator.generator(coordinates, type)
    
    def getFilesNames(self):
        dadosRaw = self.__conn.consultarFilesNames()
        dados = []
        for dado in dadosRaw:
            dados.append(dado.get("descricao"))
            
        return dados
      
    def fileUpload(self, req: dict):
        name = req.get("descricao")
        file = req.get("file")
        
        try:
            decoded = base64.b64decode(file)
            json.loads(decoded.decode("utf-8"))
        except Exception as e:
            raise Exception("Arquivo inválido: o conteúdo não é um JSON válido.") from e

        self.__conn.createFile(name, file)
      
    def fileDelete(self, req: dict):
        fileName = req.get("descricao")
        
        if fileName is None:
            raise Exception("invalid file name")
        
        file = self.__conn.consultarFileByName(fileName)
        self.__conn.deleteFile(file.get("id"))  
      