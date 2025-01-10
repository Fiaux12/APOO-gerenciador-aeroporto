import pandas as pd
from ..enums.enum_tipo_aviao import EnumTipoAviao
from modulos.manipula_arquivos import ManipulaArquivos

CAMINHO_AVIOES = "base_dados/voo/avioes.json"
cabecalho = 'Avioes'
colunas = ["capacidade_maxima","velocidade_maxima","qtd_motores","modelo", "consumo", "peso_maximo", "numero_serie", "tipo"]

class Aviao():
    def __init__(self) -> None:
        # Capacidade máxima do avião - str
        self._capacidade_maxima = None

        # Velocidade máxima do avião - str
        self._velocidade_maxima = None

        # Quantidade de motores da aeronave - str
        self._qtd_motores = None

        # Modelo da aeronave (ex: Boeing 737, Airbus A320) - str
        self._modelo = None

        # Consumo de combustível da aeronave - str
        self._consumo = None

        # Peso máximo da aeronave - str
        self._peso_maximo = None

        # Número de série único da aeronave - str
        self._numero_serie = None

        # Tipo de aeronave - EnumTipoAviao
        self._tipo = None

    #--------------GET--------------

    @property
    def capacidade_maxima(self):
        return self._capacidade_maxima
    
    @property
    def velocidade_maxima(self):
        return self._velocidade_maxima
           
    @property
    def qtd_motores(self):
        return self._qtd_motores
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def consumo(self):
        return self._consumo
    
    @property
    def peso_maximo(self):
        return self._peso_maximo
    
    @property
    def numero_serie(self):
        return self._numero_serie
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def str_tipo(self):
        return self._tipo.value

    #--------------SET--------------

    @capacidade_maxima.setter
    def capacidade_maxima(self, valor):
        if valor.isdigit():  
            self._capacidade_maxima = valor
        else:
            raise Exception("Capacidade inválida!")
        
    @velocidade_maxima.setter
    def velocidade_maxima(self, valor):
        if valor.isdigit():  
            self._velocidade_maxima = valor
        else:
            raise Exception("Velocidade inválido!")
        
    @qtd_motores.setter
    def qtd_motores(self, valor):
        if valor.isdigit():  
            self._qtd_motores = valor
        else:
            raise Exception("Número de motores inválido!")
        
    @modelo.setter
    def modelo(self, valor):
        if valor and valor.strip(): 
            self._modelo = valor
        else:
            raise Exception("Modelo inválido!")

    @consumo.setter
    def consumo(self, valor):
        if valor.isdigit():  
            self._consumo = valor
        else:
            raise Exception("Consumo inválido!")
    
    @peso_maximo.setter
    def peso_maximo(self, valor):
        if valor.isdigit():  
            self._peso_maximo = valor
        else:
            raise Exception("Peso inválido!")
    
    @numero_serie.setter
    def numero_serie(self, valor):
        if valor.isdigit():  
            self._numero_serie = valor
        else:
            raise Exception("Número de série inválido!")
        
    @tipo.setter
    def tipo(self, valor):
        if valor in (EnumTipoAviao.CARGA, EnumTipoAviao.PASSAGEIRO) and valor != None:  
            self._tipo = valor
        else:
            raise Exception("Tipo de avião inválido!")
        
    #--------------PRIVATE--------------

    #--------------PUBLIC---------------
   
    def cadastrar(capacidade_maxima, velocidade_maxima, qtd_motores, modelo, consumo , peso_maximo, numero_serie, tipo):
        aviao = Aviao()
        aviao.capacidade_maxima = capacidade_maxima
        aviao.velocidade_maxima = velocidade_maxima
        aviao.qtd_motores = qtd_motores
        aviao.modelo = modelo
        aviao.consumo = consumo
        aviao.peso_maximo = peso_maximo
        aviao.numero_serie = numero_serie
        aviao.tipo = tipo
        

        avioes = Aviao.carregarListaAvioes()

        for _, aviao_ in avioes.iterrows():
            if aviao_["numero_serie"] == numero_serie:
                raise Exception("Já existe um avião com esse numero de série!")
        

        novo_aviao = pd.DataFrame([
            {
                "numero_serie": aviao.numero_serie,
                "modelo": aviao.modelo,
                "tipo": aviao.str_tipo,
                "capacidade_maxima": aviao.capacidade_maxima,
                "velocidade_maxima": aviao.velocidade_maxima,
                "qtd_motores": aviao.qtd_motores,
                "consumo": aviao.consumo,
                "peso_maximo": aviao.velocidade_maxima,
            }
        ])

        avioes = pd.concat([avioes, novo_aviao], ignore_index=True)
        ManipulaArquivos.salvar_informacoes(avioes, CAMINHO_AVIOES, cabecalho)
    
    def carregarListaAvioes():
        lista_avioes = ManipulaArquivos.carregar_informacoes(CAMINHO_AVIOES, cabecalho, colunas)
        return lista_avioes
    
