import unittest
from AAP1.User import User

#Tests User
#Author Trey EllisS
class UserTests(unittest.TestCase):

    def testUserCreation(self):

        test_User = User(1, "Bob Jhones", "BobTheBuilder", "Builder Rd", "I can Build it")

        self.assertEqual(User.get_full_name(test_User) , "Bob Jhones")
        print("Result was : " + str(test_User.full_name))
        print("Result expected : Bob Jhones")

        self.assertEqual(User.get_user_id(test_User) , 1)
        print("Result was : " + str(test_User.user_id))
        print("Result expected : 1")

        self.assertEqual(User.get_user_name(test_User) ,  "BobTheBuilder")
        print("Result was : " + str(test_User.user_name))
        print("Result expected :  BobTheBuilder")

        self.assertEqual(User.get_address(test_User) , "Builder Rd")
        print("Result was : " + str(test_User.address))
        print("Result expected : Builder Rd")

        self.assertEqual(User.get_bio(test_User) , "I can Build it")
        print("Result was : " + str(test_User.bio))
        print("Result expected : I can Build it")


if __name__ == '__main__':
    unittest.main()
