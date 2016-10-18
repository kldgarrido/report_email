import psycopg2
from credential import credential_postgress
from query_repository import gastos, ingresos
from model import reportitem


def create_connection():
    credential_list = []
    credential_list.append(credential_postgress['dbname'])
    credential_list.append(credential_postgress['user'])
    credential_list.append(credential_postgress['host'])
    credential_list.append(credential_postgress['password'])
    try:
        str_conn = "dbname={} user={} host={} password={}".format(*credential_list)
        conn = psycopg2.connect(str_conn)
        return conn
    except:
        print "I am unable to connect to the database"


def execute_gasto_query(fechas):
    result = []
    conn = create_connection()
    cur = conn.cursor()
    query = gastos.format(*fechas)

    try:
        cur.execute(query)
    except:
        print "I can't SELECT from bar"

    rows = cur.fetchall()


    for row in rows:
        item = reportitem(row[0], row[1])
        result.append(item)

    return result


def execute_ingreso_query(fechas):
        result = []
        conn = create_connection()
        cur = conn.cursor()
        query = ingresos.format(*fechas)

        try:
            cur.execute(query)
        except:
            print "I can't SELECT from bar"

        rows = cur.fetchall()

        for row in rows:
            item = reportitem(row[0], row[1])
            result.append(item)

        return result

