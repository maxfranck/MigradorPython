from datetime import datetime
import pandas as pd
import numpy as np
import listas

# def pega_planilha(planilha):
planilha = pd.read_excel('planilha.xlsx',
                        parse_dates=['Vencimento'],
                        date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d %I:%M:%S')
                        )
#Substitui todo valor vazio da planilha
planilha.fillna('', inplace=True)
# Arquivo que será exportado
script = open("script.sql", "w")

texto = list()
# hoje = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

for row in planilha.itertuples():

    # Tratamento do nome da qualidade e do tipo de cultra
    string = row[21]
    novo_nome = string.replace("Cafe ", "")
    novo_nome = novo_nome.replace("Arabica  ", "")
    novo_nome = novo_nome.replace(" Natural", "")
    if novo_nome == 'Bica':
        novo_nome = 'Bica Forte'

    #Modificando formato das datas
    now = datetime.now()
    hoje = now.strftime("%Y-%m-%d %H:%M:%S")
    l18 = datetime.strptime(row[18], "%d/%m/%Y")
    linha18 = l18.strftime("%Y-%m-%d")
    
    dados = np.array([
        ["oferta,", f"'{row[3]}',"],
        ["oferta_old,", f"'{row[3]}',"],
        ["tipoculturas_id,", f'{listas.dado_cultura(novo_nome)},'],
        ["safras_id,", f'{listas.dado_safra(row[15])},'],
        ["safracontratos_id,", f'{listas.dado_safra(row[15])},'],
        ["qtd,", f'{row[11]},'],
        ["qtd_inicial,", f'{row[11]},'],
        ["tipoculturas_rec_id,", f'{listas.dado_cultura(novo_nome)},'],
        ["at_id,", '9998,'],
        ["produtor_id,", '9999,'],
        ["locais_ini_id,", f'{listas.dado_armazem(row[16])},'],
        ["locais_fim_id,", f'{listas.dado_armazem(row[16])},'],
        ["locais_saida_id,", f'{listas.dado_armazem(row[16])},'],
        ["unidades_id,", '1,'],
        ["rts_id,", f'{listas.dado_rtv(row[7])},'],
        ["distribuicao_id,", f'{listas.dado_distribuidor(row[10])},'],
        ["regioes_id,", f'{listas.dado_regiao(row[4])},'],
        ["qualidades_id,", f'{listas.dado_qualidade(novo_nome)},'],
        ["qualidades_rec_id,", f'{listas.dado_qualidade(novo_nome)},'],
        ["rts_pedidos_id,", '9997,'],
        ["atn_id,", '9998,'],
        ["gerente_id,", '9993,'],
        ["status,", '1,'],
        ["data_cadastro,", f"'{hoje}',"],
        ["data_aprovacao,", f"'{linha18}',"],
        ["data_entrega,", f"'{linha18}',"],
        ["data_prevista,", f"'{linha18}',"],
        ["data_faturado,", f"'{linha18}',"],
        ["observacao,", "'MIGRADO',"],
        # ["observacao_entrega,", "''"],
        ["qtd_rec,", '0,'],
        ["qtd_a_receber,", '0,'],
        ["estoque,", '0,'],
        # ["certificados,", f'{None},'],
        ["subregiao,", f"'{row[5]}',"],
        ["regional,", f"'{row[6]}',"],
        ["cod_cli,", f'{row[9]},'],
        ["pbarter,", f"'{row[2]}',"],
        ["preco_base,", f'{row[20]},'],
        ["preco_carga,", f'{row[19]},'],
        ["preco_final,", f'{row[22]},'],
        ["comprado_ny,", '0,'],
        ["rolagem_ny,", '0,'],
        ["venda_ny,", '0,'],
        ["nybot,", '0,'],
        # ["mes_bolsa,", f'{None},'],
        ["capital_giro,", '0,'],
        ["preco_alocado,", f'{row[22]},'],
        ["cogsofftaker,", f'{row[30]},'],
        ["provisao,", '0,'],
        ["provisao_saca,", '0,'],
        ["comprado_ny_negociado,", '0,'],
        ["total_original,", '0,'],
        ["total_negociado,", '0,'],
        ["virtual_ny,", '0,'],
        ["total_venda_nybot,", '0,'],
        ["ganho_ny,", '0,'],
        ["codigo_rfa,", '0,'],
        # ["funrural,", f'{None},'],
        # ["quebra,", f'{None},'],
        # ["tipo_oferta,", f'{None},'],
        # ["potencial_certificacao,", f'{None},'],
        # ["pontualidade,", f'{None},'],
        # ["gtc,", f'{None},'],
        ["tiposofertas_id,", '2,'],
        # ["fixar,", f'{None},'],
        ["nucoffee,", '1,'],
        ["aplicabilidade,", '1,'],
        ["rastreabilidade,", '1,'],
        ["boas_praticas,", '1,'],
        ["finalizado,", '0,'],
        # ["liquidacao_financeira,", f'{None},'],
        ["somaqtdproduto,", '0,'],
        ["somavalorproduto,", '0,'],
        ["ativo,", '1,'],
        ["excluido,", '1,'],
        ["certificacao,", f"'{row[23]}',"],
        # ["portal,", ''],
        ["valorreportado,", '0,'],
        ["kpi,", '0,'],
        ["ofertareal,", '0,'],
        ["migracao_usuarios_id,", f'{2719},'],
        ["migracao_data,", f"'{hoje}',"],
        ["qtdlotebolsa,", f'{row[11]},'],
        ["data_vencimento,", f"'{row[13]}',"],
        ["service_provider,", f"'{row[2]}',"],
        ["qtd_ton,", f'{row[11]*60},'],
        ["company_code,", f"'{row[31]}',"],
        ["modalidade_vendas,", f"'{row[32]}',"],
        ["moeda,", f"'{row[33]}',"],
        ["taxa_cambio_ptax,", f'{row[34]},'],
        ["peso", f'{row[11]*60}']
    ])
    
    print('INSERT INTO ofertas (', end=' ', file=script)
    #Imprime os campos
    for x in dados:
        print(x[0], end=' ', file=script)
    print(') ', end=' ', file=script)
    print('VALUES (', end=' ', file=script)
    #Imprime os valores
    for x in dados:
        print(x[1], end=' ', file=script)
    print(');', file=script)
    
    # script.writelines(texto)
    
