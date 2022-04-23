import pandas as pd
import listas
from IPython.display import display

# def pega_planilha(planilha):
planilha = pd.read_excel('planilha.xlsx')

# Pesquisar ID no banco de dados
# Regiões

regioes = planilha["Região Colheita"]
for regiao in regioes:
    listas.dado_regiao(regiao)

# Safras
safras = planilha["Safra Commodity"]
for safra in safras:
    listas.dado_safra(safra)

# RTVs
rtvs = planilha["Descrição do RTV"]
for rtv in rtvs:
    listas.dado_rtv(rtv)

# Distribuidores
distribuidores = planilha["Descrição do recebedor da mercadoria"]
for distribuidor in distribuidores:
    listas.dado_distribuidor(distribuidor)

# Tratamento do nome da qualidade e do tipo de cultra
string = planilha["Tipo Commodity"]
novo_nome = string.replace("Cafe ", "")
novo_nome = novo_nome.replace("Arabica ", "")
novo_nome = novo_nome.replace(" Natural", "")
if novo_nome == 'Bica':
    novo_nome = 'Bica Forte'

# Qualidades
qualidades = novo_nome
for qualidade in qualidades:
    listas.dado_qualidade(qualidade)

# Culturas
culturas = novo_nome
for cultura in culturas:
    listas.dado_cultura(cultura)


# Query
for linha in planilha:
    print(f"dados = ")
