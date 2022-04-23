from database import query_db

# Regiões
def dado_regiao(data):
    regiao = query_db(f"select id from regioes where nome like '%{data}%' limit 1")
    if regiao == None:
        print('A Classificar')
    else:
        print(regiao)

# Safras
def dado_safra(data):
    safra = query_db(f"select id from safras where nome like '%{data}%' limit 1")
    if safra == None:
        print('A Classificar')
    else:
        print(safra)

# RTVs
def dado_rtv(data):
    rtv = query_db(f"select id from usuarios where tiposusuarios_id = 11 and nome like '%{data}%' limit 1")
    if rtv == None:
        print('A Classificar')
    else:
        print(rtv)

# Distribuidores
def dado_distribuidor(data):
    distribuidor = query_db(f"select id from usuarios where tiposusuarios_id = 10 and nome like '%{data}%' limit 1")
    if distribuidor == None:
        print('A Classificar')
    else:
        print(distribuidor)

# Qualidades
def dado_qualidade(data):
    qualidade = query_db(f"select id from qualidades where nome like '%{data}%' limit 1")
    if qualidade == None:
        print('A Classificar')
    else:
        print(qualidade)

# Culturas
def dado_cultura(data):
    cultura = query_db(f"select id from tiposculturas where nome like '%{data}%' limit 1")
    if cultura == None:
        print('A Classificar')
    else:
        print(cultura)
