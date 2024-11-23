from pessoa import Pessoa

class Piloto(Pessoa):
    def __init__(self, nome, cpf, tipo_aviao, numero_licenca) -> None:
        super().__init__(nome, cpf)
        self.__tipo_aviao = tipo_aviao
        self.__numero_licenca = numero_licenca