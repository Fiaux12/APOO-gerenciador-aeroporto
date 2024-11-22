from pessoa import Pessoa

class Piloto(Pessoa):
    def __init__(self, nome, cpf, genero, tipoAviao) -> None:
        super().__init__(nome, cpf, genero)
        self.__tipoAviao = tipoAviao