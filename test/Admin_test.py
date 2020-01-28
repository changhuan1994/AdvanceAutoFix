import unittest
from AAP1.Admin import Admin
#tests Admin
#Author Trey Ellis
class AdminTests(unittest.TestCase):

    def testAdminCreation(self):

        test_User = Admin(1, "Bob Jhones", "BobTheBuilder", "Builder Rd", "I can Build it")

        self.assertEqual(test_User.user_id , 1)
        print("Result was : " + str(test_User.user_id))
        print("Result expected : 1")

        
if __name__ == '__main__':
    unittest.main()
