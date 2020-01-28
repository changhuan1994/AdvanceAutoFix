import unittest
from AAP1.UserDataAccess import UserDataAccess
from AAP1.Mechanic import Mechanic

try:
    from ConnectionPool import connectionPool
except :
    from AAP1.ConnectionPool import connectionPool

#Tests UserDataAccess
#Author Trey Ellis
class UserDataAccessTests(unittest.TestCase):

    def testUserAdd(self):

        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()
        connection_object.cmd_query("DELETE FROM users WHERE user_id > 4;")
        connection_object.commit()
        connection_object.close()

        self.assertTrue(UserDataAccess.AddUser("Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP"))
        UserDataAccess.RemoveUserbyUserName("RobTheBuilder")

    def testUserReturn(self):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()
        connection_object.cmd_query("DELETE FROM users WHERE user_id > 4;")
        connection_object.commit()
        connection_object.close()

        test_User = Mechanic(1, "Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")
        UserDataAccess.AddUser("Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")

        test_User_Return = UserDataAccess.ReturnUserByUserName("RobTheBuilder")
        print(test_User_Return)


        Output_User = Mechanic(int(test_User_Return[0]), test_User_Return[1].decode("utf-8" ), test_User_Return[2].decode("utf-8" ), test_User_Return[3].decode("utf-8" ), test_User_Return[4].decode("utf-8" ), test_User_Return[5].decode("utf-8" ), test_User_Return[6].decode("utf-8" ), test_User_Return[7].decode("utf-8" ))
        #print(Output_User.get_user_id())
        #print(Output_User.get_user_name())
        #print(Output_User.get_full_name())
        #print(Output_User.get_bio())
        #print(Output_User.get_address())
        #print(Output_User.get_paypal_info())

        self.assertEqual(test_User.get_user_name(), Output_User.get_user_name())
        self.assertEqual(test_User.get_full_name(), Output_User.get_full_name())
        self.assertEqual(test_User.get_bio(), Output_User.get_bio())
        self.assertEqual(test_User.get_ASECert_id(), Output_User.get_ASECert_id())
        self.assertEqual(test_User.get_user_name(), Output_User.get_user_name())


    def testUserUpdate(self):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()
        connection_object.cmd_query("DELETE FROM users WHERE user_id > 4;")
        connection_object.commit()
        connection_object.close()

        test_User = Mechanic(1, "Rob Jhones", "RobTheBuilder", "ASE Changed", "Builder Rd", "I can Build it", "Pay Me", "HTTP")
        UserDataAccess.AddUser("Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")

        User_Return = UserDataAccess.ReturnUserByUserName("RobTheBuilder")
        Output_User = Mechanic(int(User_Return[0]), User_Return[1].decode("utf-8" ), User_Return[2].decode("utf-8" ), User_Return[3].decode("utf-8" ), User_Return[4].decode("utf-8" ), User_Return[5].decode("utf-8" ), User_Return[6].decode("utf-8" ), User_Return[7].decode("utf-8" ))

        self.assertTrue(UserDataAccess.UpdateUserByUserID( Output_User.get_user_id(), "Rob Jhones", "RobTheBuilder", "ASE Changed", "Builder Rd", "I can Build it", "Pay Me", "HTTP"))

        User_Return_change = UserDataAccess.ReturnUserByUserName("RobTheBuilder")
        Output_User_change = Mechanic(int(User_Return[0]), User_Return[1].decode("utf-8" ), User_Return[2].decode("utf-8" ), User_Return[3].decode("utf-8" ), User_Return[4].decode("utf-8" ), User_Return[5].decode("utf-8" ), User_Return[6].decode("utf-8" ), User_Return[7].decode("utf-8" ))

        self.assertNotEqual(Output_User.get_ASECert_id, Output_User_change.get_ASECert_id)


    def testUserRemoveByID(self):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()
        connection_object.cmd_query("DELETE FROM users WHERE user_id > 4;")
        connection_object.commit()
        connection_object.close()

        test_User = Mechanic(1, "Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")
        UserDataAccess.AddUser("Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")

        User_Return = UserDataAccess.ReturnUserByUserName("RobTheBuilder")
        print(User_Return)
        Output_User = Mechanic(int(User_Return[0]), User_Return[1].decode("utf-8" ), User_Return[2].decode("utf-8" ), User_Return[3].decode("utf-8" ), User_Return[4].decode("utf-8" ), User_Return[5].decode("utf-8" ), User_Return[6].decode("utf-8" ), User_Return[7].decode("utf-8" ))

        self.assertTrue(UserDataAccess.RemoveUserbyID(Output_User.get_user_id()))

        User_Return = UserDataAccess.ReturnUserByUserName("RobTheBuilder")
        self.assertEquals(User_Return, -1)


    def testUserRemoveByUserName(self):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()
        connection_object.cmd_query("DELETE FROM users WHERE user_id > 4;")
        connection_object.commit()
        connection_object.close()

        test_User = Mechanic(1, "Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")
        UserDataAccess.AddUser("Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")

        self.assertTrue(UserDataAccess.RemoveUserbyUserName("RobTheBuilder"))

        User_Return = UserDataAccess.ReturnUserByUserName("RobTheBuilder")
        self.assertEquals(User_Return, -1)

    def testConvertToMechanic(self):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection()
        connection_object.cmd_query("DELETE FROM users WHERE user_id > 4;")
        connection_object.commit()
        connection_object.close()

        test_User = Mechanic(1, "Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")
        UserDataAccess.AddUser("Rob Jhones", "RobTheBuilder", "ASE", "Builder Rd", "I can Build it", "Pay Me", "HTTP")

        
        User_Return = UserDataAccess.ReturnUserByUserName("RobTheBuilder")
        Output_User = UserDataAccess.ConvertToMechanic(User_Return)

        self.assertEqual(test_User.get_user_name(), Output_User.get_user_name())
        self.assertEqual(test_User.get_full_name(), Output_User.get_full_name())
        self.assertEqual(test_User.get_bio(), Output_User.get_bio())
        self.assertEqual(test_User.get_ASECert_id(), Output_User.get_ASECert_id())


        UserDataAccess.RemoveUserbyUserName("RobTheBuilder")

if __name__ == '__main__':
    unittest.main()
