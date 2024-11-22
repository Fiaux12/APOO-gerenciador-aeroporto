from pessoa import Pessoa

class Passageiro(Pessoa):
    def __init__(self, nome, cpf, genero, idVoo) -> None:
        super().__init__(nome, cpf, genero)
        self.__idVoo = idVoo