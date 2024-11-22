from pessoa import Pessoa

class ComissarioDeVoo(Pessoa):
    def __init__(self, nome, cpf, genero) -> None:
        super().__init__(nome, cpf, genero)