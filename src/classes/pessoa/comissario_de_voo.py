from pessoa import Pessoa

class ComissarioDeVoo(Pessoa):
    def __init__(self, nome, cpf, linguas, numero_certificado) -> None:
        super().__init__(nome, cpf)
        self.__linguas = linguas
        self.__numero_certificado = numero_certificado