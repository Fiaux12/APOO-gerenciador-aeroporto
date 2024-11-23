from pessoa import Pessoa

class Piloto(Pessoa):
    def __init__(self, nome, cpf, tipo_aviao, licenca) -> None:
        super().__init__(nome, cpf)
        self.__tipo_aviao = tipo_aviao
        self.__licenca = licenca