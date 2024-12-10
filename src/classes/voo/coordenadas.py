
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
        if valor.isdigit():  
            self.__latitude = valor
        else:
            raise ValueError("Latitude inválida!")
    
    @longitude.setter
    def longitude(self, valor):
        if valor.isdigit():  
            self.__longitude = valor
        else:
            raise ValueError("Longitude inválida!")
        