from pessoa import Pessoa

class Passageiro(Pessoa):
    def __init__(self, nome, cpf, idVoo) -> None:
        super().__init__(nome, cpf)
        self.__idVoo = idVoo