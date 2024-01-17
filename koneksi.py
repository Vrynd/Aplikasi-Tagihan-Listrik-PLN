import mysql.connector
def Connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="listrik_pln",
    )
    return connection
