from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, genero) -> None:
        self._nome = nome
        self._cpf = cpf
        self._genero = genero

