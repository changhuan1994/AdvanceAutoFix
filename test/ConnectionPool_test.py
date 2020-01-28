import unittest
from AAP1.ConnectionPool import connectionPool
from AAP1.Mechanic import Mechanic

#Tests ConnectionPool
#Author Trey Ellis
class ConnectionPoolTests(unittest.TestCase):
    def testPoolCreation(self):

        # Get connection object from a pool
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()
        connection_object.cursor(buffered=True)


        #print ("Printing connection pool properties ")
        #print("Connection Pool Name - ", pool.connection_pool.pool_name)
        #print("Connection Pool Size - ", pool.connection_pool.pool_size)

        #if connection_object.is_connected():
            #db_Info = connection_object.get_server_info()
            #print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)

            #cursor = connection_object.cursor(buffered=True)
            #cursor.execute("select database();")
            #connection_object.commit()
            #record = cursor.fetchone()
            #print ("Your connected to - ", record)

        connection_object.cmd_query("DELETE FROM users WHERE user_id > 4;")
        connection_object.commit()

        connection_object.cmd_query('INSERT INTO users(full_name, username, ASECert_id, address, bio, paypal_info, ASECert_HTTP) VALUES ("Rob","Rob The Builder","IcanBuildIt","builder St","I can Build IT","pay me", "HTTP");')
        connection_object.commit()

        myresult = connection_object.cmd_query("SELECT * FROM users WHERE username = 'Rob The Builder'")
        #cursor.fetchall()

        #print("result")
        #print(myresult['columns'])
        for row in connection_object.get_rows()[0]:
            #print("Printing rows")
            #print(row)
            returneduser = Mechanic(int(row[0]), row[1].decode("utf-8" ), row[2].decode("utf-8" ), row[3].decode("utf-8" ), row[4].decode("utf-8" ), row[5].decode("utf-8" ), row[6].decode("utf-8" ), row[7].decode("utf-8" ))

            #print("Printing User")

            #print(returneduser.get_user_id())
            #print(returneduser.get_user_name())
            #print(returneduser.get_full_name())
            #print(returneduser.get_password())
            #print(returneduser.get_bio())
            #print(returneduser.get_address())
            #print(returneduser.get_paypal_info())

            self.assertEquals(returneduser.get_user_name(), "Rob The Builder")
            self.assertEquals(returneduser.get_full_name(), "Rob")
            self.assertEquals(returneduser.get_ASECert_id(), "IcanBuildIt")
            self.assertEquals(returneduser.get_bio(), "I can Build IT")
            self.assertEquals(returneduser.get_address(), "builder St")
            self.assertEquals(returneduser.get_paypal_info(), "pay me")

            


        connection_object.cmd_query("DELETE FROM users WHERE user_id > 4;")
        connection_object.commit()


        #connection_object.close()
        
if __name__ == '__main__':
    unittest.main()