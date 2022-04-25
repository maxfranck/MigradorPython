from database import query_db

# Regiões
def dado_regiao(data):
    regiao = query_db(f"select id from regioes where nome like '%{data}%' and ativo = 1 and excluido = 1 limit 1")
    if regiao == None:
        regiao = 20
    return regiao

# Safras
def dado_safra(data):
    safra = query_db(f"select id from safras where nome = '{data}' and ativo = 1 and excluido = 1 limit 1")
    if safra == None:
        safra = 99
    return safra

# RTVs
def dado_rtv(data):
    rtv = query_db(f"select id from usuarios where tiposusuarios_id = 11 and nome like '%{data}%' and ativo = 1 and excluido = 1 limit 1")
    if rtv == None:
        rtv = 9997
    return rtv

# Distribuidores
def dado_distribuidor(data):
    distribuidor = query_db(f"select id from usuarios where tiposusuarios_id = 10 and nome like '%{data}%' and ativo = 1 and excluido = 1 limit 1")
    if distribuidor == None:
        distribuidor = 9996
    return distribuidor

# Qualidades
def dado_qualidade(data):
    qualidade = query_db(f"select id from qualidades where nome like '%{data}%' and ativo = 1 and excluido = 1 limit 1")
    if qualidade == None:
        qualidade = 99
    return qualidade

# Culturas
def dado_cultura(data):
    cultura = query_db(f"select id from tiposculturas where nome like '%{data}%' and ativo = 1 and excluido = 1 limit 1")
    if cultura == None:
        cultura = 99
    return cultura

# Armazéns
def dado_armazem(data):
    armazem = query_db(f"select id from locais where tiposlocais_id = 2 and deposito_b = '{data}' and ativo = 1 and excluido = 1 limit 1")
    if armazem == None:
        armazem = 'Null'
    return armazem
