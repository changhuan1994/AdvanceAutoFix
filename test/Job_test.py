import unittest
from AAP1.Job import Job

#Tests User
#Author Trey EllisS
class JobTests(unittest.TestCase):

    def testJobCreation(self):
        test_job = Job(1, 1, "Customer's car Address", "Help Me", 2, "Greg",  "Windshield Wiper Replacement")

        self.assertEqual( Job.get_job_id( test_job ) , 1)
        print("Result was : " + str(test_job.job_id))
        print("Result expected : 1")

        self.assertEqual(Job.get_job_type_id(test_job) , 1)
        print("Result was : " + str(test_job.job_type_id))
        print("Result expected : 1")

        self.assertEqual(Job.get_address(test_job) , "Customer's car Address")
        print("Result was : " + str(test_job.address))
        print("Result expected : Customer's car Address")

        self.assertEqual(Job.get_details(test_job) , "Help Me")
        print("Result was : " + str(test_job.details))
        print("Result expected : Help Me")

        self.assertEqual(Job.get_cus_id(test_job) , 2)
        print("Result was : " + str(test_job.cus_id))
        print("Result expected : 2")

        self.assertEqual(Job.get_customer_name(test_job) , "Greg")
        print("Result was : " + str(test_job.customer_name))
        print("Result expected : Greg")

        self.assertEqual(Job.get_job_type_name(test_job) , "Windshield Wiper Replacement")
        print("Result was : " + str(test_job.job_type_name))
        print("Result expected : Windshield Wiper Replacement")

if __name__ == '__main__':
    unittest.main()
