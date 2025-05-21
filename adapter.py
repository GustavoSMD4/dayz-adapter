import json
import base64

class Adapter:
    def __init__(self):
        pass
    
    def convertJsonCoordinates(self, file, originalCoordinates, newCoordinates):
        with open(file, 'r') as f:
            dados = json.load(f)

        for obj in dados.get("Objects", []):
            if 'pos' in obj:
                diffX = obj['pos'][0] - originalCoordinates[0]
                diffY = obj['pos'][2] - originalCoordinates[1] 
                diffZ = obj['pos'][1] - originalCoordinates[2] 

                obj['pos'][0] = newCoordinates[0] + diffX 
                obj['pos'][1] = newCoordinates[2] + diffZ  
                obj['pos'][2] = newCoordinates[1] + diffY 

        return self.salvarBase64(dados)

    @staticmethod
    def salvarBase64(dados):
        jsonStr = json.dumps(dados, indent=4)
        jsonBytes = jsonStr.encode('utf-8')
        base64Bytes = base64.b64encode(jsonBytes)
        return base64Bytes.decode('utf-8')

    @staticmethod
    def criarArquivoBase64(arquivoBase64, arquivoOriginal):
        with open(arquivoBase64, 'r') as f:
            base64Str = f.read()

        base64Bytes = base64Str.encode('utf-8')
        jsonBytes = base64.b64decode(base64Bytes)
        
        with open(arquivoOriginal, 'wb') as f:
            f.write(jsonBytes)
