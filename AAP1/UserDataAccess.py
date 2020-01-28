try:
    from ConnectionPool import connectionPool
    from Mechanic import Mechanic
except :
    from AAP1.ConnectionPool import connectionPool
    from AAP1.Mechanic import Mechanic


# Class that serves as the Data access object for the user object.
#Author Trey Ellis
class UserDataAccess():
    #adds a user to the database
    #returns true if successful 
    @staticmethod
    def AddUser( full_name, user_name, ASECert_id, address, bio, paypal_info, ASECert_HTTP):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()

        command = "INSERT INTO users(full_name, username, ASECert_id, address, bio, paypal_info, ASECert_HTTP) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(full_name, user_name, ASECert_id, address, bio, paypal_info, ASECert_HTTP)
        #print(command)
        connection_object.cmd_query(command)
        connection_object.commit()

        connection_object.close()

        return True

    #Removes a user from the database with id : user_id
    #returns true if successful 
    @staticmethod
    def RemoveUserbyID( user_id):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()

        command = "DELETE FROM users WHERE user_id = '{}';".format(user_id)
        #print(command)

        connection_object.cmd_query(command)
        connection_object.commit()


        connection_object.close()

        return True

    #Returns a user from the database with user name : user_name
    #returns the user if successful, -1 if not
    @staticmethod
    def ReturnUserByUserName( user_name):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        

        command = "SELECT * FROM users WHERE username = '{}';".format(user_name)
        #print(command)

        connection_object.cmd_query(command)
        User_Return = connection_object.get_rows()
        #should only be one row so pull the first
        try:
            User_Return = User_Return[0][0]
        except:
            connection_object.close()
            return -1

        connection_object.close()

        return User_Return

    #Removes a user from the database with user name : user_name
    #returns true if successful 
    @staticmethod
    def RemoveUserbyUserName( user_name):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()

        command = "DELETE FROM users WHERE username =  '{}';".format(user_name)
        #print(command)

        connection_object.cmd_query(command)
        connection_object.commit()

        connection_object.close()

        return True

    #Updates a user in the database with id : user_id with the passed in fields
    #returns true if successful 
    @staticmethod
    def UpdateUserByUserID( user_id, full_name, user_name, ASECert_id, address, bio, paypal_info, ASECert_HTTP):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()

        command ="UPDATE users SET full_name = '{}', username = '{}', ASECert_id = '{}', address = '{}', bio = '{}', paypal_info = '{}', ASECert_HTTP = '{}' WHERE user_id = '{}';".format(full_name, user_name, ASECert_id, address, bio, paypal_info, ASECert_HTTP, user_id)
        #print(command)

        connection_object.cmd_query(command)
        connection_object.commit()

        connection_object.close()

        return True

    #Helper method to convert a binary array user into a mechanic object
    #returns The mechanic user
    @staticmethod
    def ConvertToMechanic( User_Return):
        
        Output_User = Mechanic(int(User_Return[0]), User_Return[1].decode("utf-8" ), User_Return[2].decode("utf-8" ), User_Return[3].decode("utf-8" ), User_Return[4].decode("utf-8" ), User_Return[5].decode("utf-8" ), User_Return[6].decode("utf-8" ), User_Return[7].decode("utf-8" ))
        
        return Output_User


