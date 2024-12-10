import pandas as pd
from ..enums.enum_tipo_aviao import EnumTipoAviao
from funcionalidades.arquivos.manipula_arquivos import ManipulaArquivos

CAMINHO_AVIOES = "base_dados/voo/avioes.json"
cabecalho = 'Avioes'
colunas = ["capacidade_maxima","velocidade_maxima","qtd_motores","modelo", "consumo", "peso_maximo", "numero_serie", "tipo"]

class Aviao():
    def __init__(self) -> None:
        self._capacidade_maxima = None
        self._velocidade_maxima = None
        self._qtd_motores = None
        self._modelo = None
        self._consumo = None
        self._peso_maximo = None
        self._numero_serie = None
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

    #--------------SET--------------

    @capacidade_maxima.setter
    def capacidade_maxima(self, valor):
        if valor.isdigit():  
            self._capacidade_maxima = valor
        else:
            raise ValueError("Capacidade inválida!")
        
    @velocidade_maxima.setter
    def velocidade_maxima(self, valor):
        if valor.isdigit():  
            self._velocidade_maxima = valor
        else:
            raise ValueError("Velocidade inválido!")
        
    @qtd_motores.setter
    def qtd_motores(self, valor):
        if valor.isdigit():  
            self._qtd_motores = valor
        else:
            raise ValueError("Número de motores inválido!")
        
    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @consumo.setter
    def consumo(self, valor):
        if valor.isdigit():  
            self._consumo = valor
        else:
            raise ValueError("Consumo inválido!")
    
    @peso_maximo.setter
    def peso_maximo(self, valor):
        if valor.isdigit():  
            self._peso_maximo = valor
        else:
            raise ValueError("Peso inválido!")
    
    @numero_serie.setter
    def numero_serie(self, valor):
        if valor.isdigit():  
            self._numero_serie = valor
        else:
            raise ValueError("Número de série inválido!")
        
    @tipo.setter
    def tipo(self, valor):
        if valor in (EnumTipoAviao.CARGA, EnumTipoAviao.PASSAGEIRO):  
            self._tipo = valor
        else:
            raise ValueError("Tipo de avião inválido!")
        
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
        

        df = Aviao.carregarListaAvioes()
        novo_aviao = pd.DataFrame([
            {
                "numero_serie": aviao.numero_serie,
                "modelo": aviao.modelo,
                "tipo": aviao.tipo,
                "capacidade_maxima": aviao.capacidade_maxima,
                "velocidade_maxima": aviao.velocidade_maxima,
                "qtd_motores": aviao.qtd_motores,
                "consumo": aviao.consumo,
                "peso_maximo": aviao.velocidade_maxima,
            }
        ])

        df = pd.concat([df, novo_aviao], ignore_index=True)
        ManipulaArquivos.salvar_informacoes(df, CAMINHO_AVIOES, cabecalho)
    
    def carregarListaAvioes():
        lista_avioes = ManipulaArquivos.carregar_informacoes(CAMINHO_AVIOES, cabecalho, colunas)
        return lista_avioes
    
