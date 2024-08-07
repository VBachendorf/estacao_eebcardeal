import mysql.connector
from mysql.connector import Error

def view_data(query):
    try:
        connection = mysql.connector.connect(

            host="187.45.102.198",
            user="root",
            password="#CARdeal2024",
            database="estacao"
        
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
