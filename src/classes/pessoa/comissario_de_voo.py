import pandas as pd
from .pessoa import Pessoa
from modulos.manipula_arquivos import ManipulaArquivos

CAMINHO_COMISSARIOS = "base_dados/tripulacao/comissarios.json"
cabecalho = 'Comissarios'
colunas = ["nome","cpf","linguas","numero_certificado"]


class ComissarioDeVoo(Pessoa):
    def __init__(self, nome, cpf) -> None:
        super().__init__(nome, cpf)

        #Línguas faladas - Lista de str
        self.__linguas = []

        # Número do certificado - str
        self.__numero_certificado = None

    #--------------GET--------------

    @property
    def linguas(self):
        return self.__linguas
    
    @property
    def numero_certificado(self):
        return self.__numero_certificado

    #--------------SET--------------

    @linguas.setter
    def linguas(self, valor):
        lista_linguas = ['Português', 'Inglês', 'Alemão', 'Russo', 'Chinês', 'Japonês', 'Francês', 'Italiano']
        
        if not valor:  
            raise Exception("A lista de línguas não pode ser vazia!")
    
        for lingua in valor:
            if lingua not in lista_linguas:  
                raise Exception(f"Língua inválida!")
        self.__linguas = valor
    
    @numero_certificado.setter
    def numero_certificado(self, valor):
        if valor.isdigit():  
            self.__numero_certificado = valor
        else:
            raise Exception("Número do Certificado inválido!")

    #--------------PRIVATE--------------

    #--------------PUBLIC---------------

    def cadastrar(nome, cpf, linguas, numero_certificado):
        comisario = ComissarioDeVoo(nome, cpf)
        comisario.linguas = linguas
        comisario.numero_certificado = numero_certificado

        df = ComissarioDeVoo.carregarListaComissarios()
        novo_comissario = pd.DataFrame([
            {
                "nome": comisario.nome,
                "cpf": comisario.cpf,
                "linguas": comisario.linguas,
                "numero_certificado": comisario.numero_certificado
            }
        ])

        df = pd.concat([df, novo_comissario], ignore_index=True)
        ManipulaArquivos.salvar_informacoes(df, CAMINHO_COMISSARIOS, cabecalho)
    
    def carregarListaComissarios():
        lista_comissarios = ManipulaArquivos.carregar_informacoes(CAMINHO_COMISSARIOS, cabecalho, colunas)
        return lista_comissarios
    