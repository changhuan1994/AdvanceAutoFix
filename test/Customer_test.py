import unittest
from AAP1.Customer import Customer

#Tests Customer
#Author Trey Ellis
class CustomerTests(unittest.TestCase):

    def testCustomerCreation(self):

        test_User = Customer(1, "Bob Jhones", "BobTheBuilder", "Builder Rd", "I can Build it", "PayMeHere")

        self.assertEqual(test_User.paypal_info , "PayMeHere")
        print("Result was : " + str(test_User.paypal_info))
        print("Result expected : PayMeHere")

        
if __name__ == '__main__':
    unittest.main()
