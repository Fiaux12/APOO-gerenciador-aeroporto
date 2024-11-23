from pessoa import Pessoa

class ComissarioDeVoo(Pessoa):
    def __init__(self, nome, cpf) -> None:
        super().__init__(nome, cpf)