class Carga():
    def __init__(self, remetente, cpf_remetente, destino, destinatario, descricao) -> None:
        self.__remetente = remetente
        self.__cpf_remetente = cpf_remetente
        self.__destino = destino
        self.__destinatario = destinatario
        self.__descricao = descricao

    #--------------GET--------------

    @property
    def remetente(self):
        return self.__remetente

    @property
    def cpf_remetente(self):
        return self.__cpf_remetente

    @property
    def destino(self):
        return self.__destino

    @property
    def destinatario(self):
        return self.__destinatario

    @property
    def descricao(self):
        return self.__descricao

    #--------------SET--------------

    @remetente.setter
    def remetente(self, valor):
        if valor and valor.strip():
            self.__remetente = valor
        else:
            raise ValueError("O remetente não pode ser vazio.")

    @cpf_remetente.setter
    def cpf_remetente(self, valor):
        if valor.isdigit() and len(valor) == 11:  # Exemplo para CPF brasileiro
            self.__cpf_remetente = valor
        else:
            raise ValueError("CPF do remetente inválido.")

    @destino.setter
    def destino(self, valor):
        if valor and valor.strip():
            self.__destino = valor
        else:
            raise ValueError("O destino não pode ser vazio.")

    @destinatario.setter
    def destinatario(self, valor):
        if valor and valor.strip():
            self.__destinatario = valor
        else:
            raise ValueError("O destinatário não pode ser vazio.")

    @descricao.setter
    def descricao(self, valor):
        if valor and valor.strip():
            self.__descricao = valor
        else:
            raise ValueError("A descrição não pode ser vazia.")
