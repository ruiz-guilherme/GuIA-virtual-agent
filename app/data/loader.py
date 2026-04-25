import pandas as pd
import json

def carregar_dados():
    perfil = json.load(open('./data/perfil_investidor.json'))
    produtos = json.load(open('./data/produtos_financeiros.json'))
    historico = pd.read_csv('./data/historico_atendimento.csv')
    transacoes = pd.read_csv('./data/transacoes.csv')

    return perfil, produtos, historico, transacoes