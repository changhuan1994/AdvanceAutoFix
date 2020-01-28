#from pip._internal import main
#main(['install','mysql-connector-python-rf'])

import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling


#Singolton Style classs that serves as the connection pool to a mysql database.
#auto curates up to 32 connections
#Author Trey Ellis
class connectionPool():

    #class variables for singlton and database info
    __instance = None
    connections = 5
    connection_pool = None
    host = 'localhost'
    database = "aap"
    user='root'
    password=''

    #sets up the singlton and returns it
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if connectionPool.__instance == None:
            connectionPool()
        return connectionPool.__instance

    def __init__(self):
        """ Virtually private constructor. """
        try:
            if connectionPool.__instance != None:
                raise Exception("This class is a singleton!")
            else:
                #sets up the connection pool
                connectionPool.__instance = self
                self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name="AAPPool",
                    pool_size= self.connections,
                    pool_reset_session=True,
                    host= self.host,
                    database= self.database,
                    user= self.user,
                    password= self.password,
                    charset = 'utf8')                    
        except Error as e:
            print(e)
            raise Exception("Singlton Creation Failed!")
            

# Get connection object from a pool
#pool = connectionPool.getInstance()
#connection_object = pool.connection_pool.get_connection()

#db_Info = connection_object.get_server_info()

#cursor = connection_object.cursor(buffered=True)
#cursor.execute("select database();")
#connection_object.commit()
#record = cursor.fetchone()
#print ("Your connected to - ", record)

#print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)
#print ("Printing connection pool properties ")
#print("Connection Pool Name - ", pool.connection_pool.pool_name)
#print("Connection Pool Size - ", pool.connection_pool.pool_size)
#output = connection_object.cmd_query('INSERT INTO users(full_name, username, pass, address, bio, paypal_info) VALUES ("Bob","Bob The Builder","IcanBuildIt","builder St","I can Build IT","pay me");')
#connection_object.commit()
#connection_object.close()

#print ("the insert output is : ")    
#print(output)  

