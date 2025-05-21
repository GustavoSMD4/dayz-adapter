import base64
import json
from typing import Literal

class BaseGenerator:
    def __init__(self):
        self.__tentBaseFile = "tent.json"
        
    def generator(self, coordinates: list[float, float, float], type: Literal["tent"]):
        data = ""
        
        if type == "tent":
            with open(self.__tentBaseFile, 'r', encoding='utf-8') as f:
                data = json.load(f)
        
        else:
            raise Exception("invalid type")
        
        originalCoordinates = [6605, 9054, 359]

        for obj in data.get("Objects", []):
            if 'pos' in obj:
                diffX = obj['pos'][0] - originalCoordinates[0]
                diffY = obj['pos'][2] - originalCoordinates[1]
                diffZ = obj['pos'][1] - originalCoordinates[2]

                obj['pos'][0] = coordinates[0] + diffX
                obj['pos'][1] = coordinates[2] + diffZ
                obj['pos'][2] = coordinates[1] + diffY

        jsonStr = json.dumps(data, ensure_ascii=False)
        jsonBytes = jsonStr.encode('utf-8')
        newBase64 = base64.b64encode(jsonBytes).decode()

        return newBase64

