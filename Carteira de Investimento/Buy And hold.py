
**importando as Bibliotecas**

import pandas as pd
import numpy as np
import yfinance as yf

"""**Carteira**
> Montando nossa carteira.

"""

compras = {'VALE3.SA':200,'AAPL34.SA':500,
           'COCA34.SA':300,'WEGE3.SA':350,
           'PETR4.SA':400,
           'BPAC11.SA':100,
           'SMAL11.SA':100,
           'TAEE11.SA' :200
           }

list(compras.keys())

sum(compras.values())

"""***Importando os dados.***"""

inicio = '2021-01-01'
fim = '2023-01-01'

"""***Simulação da carteira***

"""

precos = yf.download(list(compras.keys()), start = inicio, end = fim, progress=False)

primeiro = precos.iloc[0]

"""**Transformado os papaeis em indices.**"""

compras_df = pd.Series(compras, index=list(compras.keys()))

"""**Quantidade de papeis comprados, pelo aporte realizado na carteira.**"""

qtd_acoes = round(compras_df/primeiro[0])

pl = precos['Close'] * qtd_acoes

pl['PL TOTAL'] = PL.sum(axis=1)

pl.head()

"""Comparação com bovespa"""

ibov = yf.download('^BVSP', start = inicio, end = fim, progress=False)['Close']

pd.DataFrame(ibov)

"""**Juntando tudo**"""

consolilado = pd.merge(pl, ibov, how = 'inner', on= 'Date')

consolilado.head()

"""**Normalização**"""

ajuste_cons = consolilado/consolilado.iloc[0]

"""**desempenho**

> carteira x ibov


"""

ajuste_cons[['^BVSP', 'PL TOTAL']].plot(figsize=(7,5))

"""**FUNÇÃO PARA TESTAR CARTEIRAS**"""

def simula_carteira(inicio , fim, carteira):
  precos = yf.download(list(carteira.keys()), start = inicio, end = fim, progress=False)
  primeiro = precos.iloc[0]
  compras_df = pd.Series(carteira, index=list(carteira.keys()))
  qtd_acoes = round(compras_df/primeiro['Close'])
  pl = precos['Close'] * qtd_acoes
  pl['PL TOTAL'] = pl.sum(axis=1)
  ibov = yf.download('^BVSP', start = inicio, end = fim, progress=False)['Close']
  consolido = pd.merge(pl, ibov, how = 'inner', left_index=True, right_index=True)
  ajuste_cons = consolido/consolido.iloc[0]
  ajuste_cons[['^BVSP', 'PL TOTAL']].plot(figsize=(7,5));
  return ajuste_cons

"""**PORTIFOLIO NOVO**"""

portifolio = {
    'ITSA4.SA': 500,  # Itaúsa
    'BBDC4.SA': 400,  # Bradesco
    'PETR3.SA': 600,  # Petrobras
    'VALE3.SA': 700,  # Vale
    'ABEV3.SA': 300,  # Ambev
    'ITUB4.SA': 550   # Itaú Unibanco
}

simula_carteira(inicio,fim ,portifolio)
