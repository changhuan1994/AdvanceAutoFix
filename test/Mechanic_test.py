import unittest
from AAP1.Mechanic import Mechanic

#Tests Mechanic
#author Trey Ellis
class MechanicTests(unittest.TestCase):

    def testMechanicCreation(self):

        test_User = Mechanic(1, "Bob Jhones", "BobTheBuilder", "IcanBuildIt", "Builder Rd", "I can Build it", "PayMeHere", "HTTP")

        self.assertEqual(Mechanic.get_full_name(test_User) , "Bob Jhones")
        print("Result was : " + str(test_User.full_name))
        print("Result expected : Bob Jhones")

        self.assertEqual(Mechanic.get_user_id(test_User) , 1)
        print("Result was : " + str(test_User.user_id))
        print("Result expected : 1")

        self.assertEqual(Mechanic.get_user_name(test_User) ,  "BobTheBuilder")
        print("Result was : " + str(test_User.user_name))
        print("Result expected :  BobTheBuilder")

        self.assertEqual(Mechanic.get_ASECert_id(test_User) , "IcanBuildIt")
        print("Result was : " + str(test_User.ASECert_id))
        print("Result expected : IcanBuildIt")

        self.assertEqual(Mechanic.get_address(test_User) , "Builder Rd")
        print("Result was : " + str(test_User.address))
        print("Result expected : Builder Rd")

        self.assertEqual(Mechanic.get_bio(test_User) , "I can Build it")
        print("Result was : " + str(test_User.bio))
        print("Result expected : I can Build it")

        self.assertEqual(Mechanic.get_paypal_info(test_User) , "PayMeHere")
        print("Result was : " + str(test_User.paypal_info))
        print("Result expected : PayMeHere")

if __name__ == '__main__':
    unittest.main()
