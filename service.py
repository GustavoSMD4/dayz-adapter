from adapter import Adapter


class Service:
    def __init__(self):
        self.__adapter = Adapter()
    
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
        