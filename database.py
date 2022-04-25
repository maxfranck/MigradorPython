import mysql.connector
from mysql.connector import errorcode

# Dados para conexão com banco
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        database='database',
        user='root',
        password=''
    )

def query_db(query):
    # Conecta com banco
    try:
        con = connect_db()
        consulta_sql = query

        if con.is_connected():
            cursor = con.cursor()
            cursor.execute(consulta_sql )
            linhas = cursor.fetchall()

            # Verifica se o retorno contém alguma linha
            if len(linhas)!=0:  
                for linha in linhas:
                    dado = linha[0]
            else:
                dado = None
            return dado
    
    # Mensagens de erro    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está errado com seu nome de usuário ou senha")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(err)

    # Encerra conexão
    else:
        if (con.is_connected()):
            con.close()
            cursor.close()
            print("Conexão encerrada")
