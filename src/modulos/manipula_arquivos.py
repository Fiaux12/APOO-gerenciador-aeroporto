import pandas as pd
import json
import os

SETTINGS_DATA_FILE = "../assets/settings/settings.json"

class ManipulaArquivos():
    def __init__(self) -> None:
        pass
        

    # TODO: Função para carregar os dados de um arquivo JSON em um DataFrame


    # Função para carregar os dados de um arquivo JSON em um DataFrame
    def carregar_informacoes(caminho, cabecalho, colunas):
        if os.path.exists(caminho):
            with open(caminho, "r") as arquivo:
                dados = json.load(arquivo)
            return pd.DataFrame(dados[cabecalho])
        return pd.DataFrame(columns=colunas)

    # Função para salvar os dados do DataFrame no arquivo JSON
    def salvar_informacoes(df, caminho, cabecalho):
        dados_json = {cabecalho: df.to_dict(orient="records")}
        with open(caminho, "w") as arquivo:
            json.dump(dados_json, arquivo, indent=4)


    # TODO:Função para atualizar dados
