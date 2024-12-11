
class Coordenadas():
    def __init__(self, latitude:int, longitude: int) -> None:
        self.__latitude = None
        self.__longitude = None

   #--------------GET--------------

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude


    #--------------SET--------------

    @latitude.setter
    def latitude(self, valor):
        if not (-90 <= valor.latitude <= 90):
            raise ValueError("Latitude deve estar no intervalo de -90 a 90.")
        self.__latitude = valor
        
    
    @longitude.setter
    def longitude(self, valor):
        if not (-180 <= valor.longitude <= 180):
            raise ValueError("Longitude deve estar no intervalo de -180 a 180.")
        self.__longitude = valor
        
        
        