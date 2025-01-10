
class Coordenadas():
    def __init__(self) -> None:
        # Latitude - float
        self.__latitude = None

        # Longitude - float
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
        if not (-90.0 <= valor <= 90.0):
            raise ValueError("Latitude deve estar no intervalo de -90 a 90.")
        self.__latitude = valor
        
    
    @longitude.setter
    def longitude(self, valor):
        if not (-180.0 <= valor <= 180.0):
            raise ValueError("Longitude deve estar no intervalo de -180 a 180.")
        self.__longitude = valor
        
        
        