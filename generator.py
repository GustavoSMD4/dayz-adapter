import base64
import json

from repo.repo import Repo

class BaseGenerator:
    def __init__(self):
        self.__tentBaseFile = "tent.json"
        
    def generator(self, coordinates: list[float, float, float], type: str):
        typesGenerateRaw = Repo().consultarFilesNames()
        typesGenerate = [t.get("descricao") for t in typesGenerateRaw]

        if type not in typesGenerate:
            raise Exception("invalid type")
        
        file = Repo().consultarFileByName(type)
        fileBase64 = file.get("file")

        json_bytes = base64.b64decode(fileBase64)
        json_str = json_bytes.decode("utf-8")
        data = json.loads(json_str)

        min_x = min_z = float('inf')
        max_x = max_z = float('-inf')
        min_y = float('inf')

        for obj in data.get("Objects", []):
            if 'pos' in obj:
                x, y, z = obj['pos']
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_z = min(min_z, z)
                max_z = max(max_z, z)
                min_y = min(min_y, y)

        if min_x == float('inf'):
            raise Exception("Nenhum objeto com posição encontrada.")

        # Centro do bounding box em X e Z, e menor Y
        originalCoordinates = [
            (min_x + max_x) / 2,  # centro em X
            min_y,                # ponto mais baixo em Y
            (min_z + max_z) / 2   # centro em Z
        ]

        for obj in data.get("Objects", []):
            if 'pos' in obj:
                diffX = obj['pos'][0] - originalCoordinates[0]
                diffY = obj['pos'][2] - originalCoordinates[2]
                diffZ = obj['pos'][1] - originalCoordinates[1]

                obj['pos'][0] = coordinates[0] + diffX
                obj['pos'][1] = coordinates[2] + diffZ
                obj['pos'][2] = coordinates[1] + diffY

        jsonStr = json.dumps(data, ensure_ascii=False)
        jsonBytes = jsonStr.encode('utf-8')
        newBase64 = base64.b64encode(jsonBytes).decode()

        return newBase64
