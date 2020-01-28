
import unittest
from AAP1.JobDataAccess import JobDataAccess
from AAP1.Job import Job

#Tests JobDataAccess
#Author Trey Ellis
class JobDataAccessTests(unittest.TestCase):

    #Requieres Database preload file to be run for test to pass
    def testJobReturnJobByID(self):

        test_job = Job(1, 1, "Customer's car Address", "Help Me", 2, "Greg", "Windshield Wiper Replacement")

        test_return = JobDataAccess.ReturnJobByID(test_job.get_job_id())
        #print(test_return)
        Output_Job = test_return
        #Output_Job = Job(int(test_return[0]), int(test_return[1]), test_return[2].decode("utf-8" ), test_return[3].decode("utf-8" ), int(test_return[4]), test_return[5].decode("utf-8" ), test_return[6].decode("utf-8" ))

        #print(test_return)

        self.assertEqual( Job.get_job_id( Output_Job ) , 1)
        print("Result was : " + str(Output_Job.job_id))
        print("Result expected : 1")

        self.assertEqual(Job.get_job_type_id(Output_Job) , 1)
        print("Result was : " + str(Output_Job.job_type_id))
        print("Result expected : 1")

        self.assertEqual(Job.get_address(Output_Job) , "Customer's car Address")
        print("Result was : " + str(Output_Job.address))
        print("Result expected : Customer's car Address")

        self.assertEqual(Job.get_details(Output_Job) , "Help Me")
        print("Result was : " + str(Output_Job.details))
        print("Result expected : Help Me")

        self.assertEqual(Job.get_cus_id(Output_Job) , 2)
        print("Result was : " + str(Output_Job.cus_id))
        print("Result expected : 2")

        self.assertEqual(Job.get_customer_name(test_job) , "Greg")
        print("Result was : " + str(test_job.customer_name))
        print("Result expected : Greg")

        self.assertEqual(Job.get_job_type_name(test_job) , "Windshield Wiper Replacement")
        print("Result was : " + str(test_job.job_type_name))
        print("Result expected : Windshield Wiper Replacement")

    #Requieres Database preload file to be run for test to pass
    def testJobReturnJobList(self):


        joblist = JobDataAccess.ReturnJobList()

        #for i in joblist:
        #    print(i.get_job_id())

        self.assertEqual(Job.get_job_type_name(joblist[0]) , "Windshield Wiper Replacement")
        print("Result was : " + str(joblist[0].job_type_name))
        print("Result expected : Windshield Wiper Replacement")

        self.assertEqual(Job.get_job_type_name(joblist[1]) , "Oil Change")
        print("Result was : " + str(joblist[1].job_type_name))
        print("Result expected : Oil Change")

        self.assertEqual(Job.get_job_type_name(joblist[2]) , "Tire Change")
        print("Result was : " + str(joblist[2].job_type_name))
        print("Result expected : Tire Change")

        self.assertEqual(Job.get_job_type_name(joblist[3]) , "Tire and Oil Change")
        print("Result was : " + str(joblist[3].job_type_name))
        print("Result expected : Tire and Oil Change")


    #Requieres Database preload file to be run for test to pass
    def testReturnJobListUnderdistance(self):

        joblist = JobDataAccess.ReturnJobListUnderdistance(-78.625679, 35.804994, 5, 3, [1, 2, 3, 4])

        #for i in joblist:
        #    print(i.get_job_id(), i.get_job_type_id(), i.get_details(), i.get_cus_id(), i.get_customer_name() )

        self.assertEqual(joblist[0].get_job_id(), 8)
        print("Result was : " + str(joblist[0].get_job_id()))
        print("Result expected : Tire and Oil Change")

        self.assertEqual(joblist[1].get_job_id(), 9)
        print("Result was : " + str(joblist[0].get_job_id()))
        print("Result expected : Windshield Wiper Replacement")




    #Requieres Database preload file to be run for test to pass
    def testBookJob(self):

        result = JobDataAccess.BookJob(1, 1, 3)
        self.assertEqual(result, 1)


    #Requieres Database preload file to be run for test to pass
    def testReturnBookedJobs(self):

        test_return = JobDataAccess.ReturnBookedJobs()



        #print(joblist)
        #print(joblist[0])
        self.assertEqual(test_return[0][0], 4)
        self.assertEqual(test_return[0][1], 1)
        self.assertEqual(test_return[0][2], 3)


    #Requieres Database preload file to be run for test to pass
    def testReturnBookedJobsWithMecID(self):


        test_return = JobDataAccess.ReturnBookedJobsWithMecID(3)


        #for i in joblist:
        #    print(i.get_job_id())

        #print(joblist)
        #print(joblist[0])
        self.assertEqual(test_return[0][0], 4)
        self.assertEqual(test_return[0][1], 1)
        self.assertEqual(test_return[0][2], 3)


    #Requieres Database preload file to be run for test to pass
    def testUnBookJob(self):

        JobDataAccess.UnBookJob(1)
        test_return = JobDataAccess.ReturnBookedJobs()
        self.assertEqual(test_return[0][0], 4)
        self.assertEqual(test_return[1][0], 3)
        self.assertEqual(test_return[2][0], 5)
        try:
            #this shouldn't pass as its been removed
            self.assertEqual(test_return[3][0], 1)
        except:
            pass
            



    #Requieres Database preload file to be run for test to pass
    def testReturnQualificationsWithMecID(self):

        test_return = JobDataAccess.ReturnQualificationsWithMecID(3)
                
        self.assertEqual(test_return[0][0], 1)
        self.assertEqual(test_return[1][0], 2)
        self.assertEqual(test_return[2][0], 3)

    #Requieres Database preload file to be run for test to pass
    def testReturnJobTypesWithLink(self):

        test_return = JobDataAccess.ReturnJobTypesWithLink()
        
        for i in test_return:
            print(i)

        self.assertEqual(test_return[0][0], 1)
        self.assertEqual(test_return[0][1], "Windshield Wiper Replacement")
        self.assertEqual(test_return[0][2], "HTTP Wipers")


    #Requieres Database preload file to be run for test to pass
    def testReturnJobHistoryOfMec(self):

        test_return = JobDataAccess.ReturnJobHistoryOfMec(3)
        
        #for i in test_return:
        #    print(i)

        self.assertEqual(test_return[0][0], 4)
        self.assertEqual(test_return[1][0], 3)
        self.assertEqual(test_return[2][0], 4)

    #Requieres Database preload file to be run for test to pass
    def testReturnJobHistoryOfJob(self):

        test_return = JobDataAccess.ReturnJobHistoryOfJob(4)
        
        #for i in test_return:
        #    print(i)

        self.assertEqual(test_return[0][0], 1)
        self.assertEqual(test_return[1][0], 2)
        self.assertEqual(test_return[2][0], 3)



    #Requieres Database preload file to be run for test to pass
    def testInsertStatus(self):
        
        JobDataAccess.insertStatus(4, 4, "Processing job")

        test_return = JobDataAccess.ReturnJobHistoryOfMec(3)

        self.assertEqual(test_return[0][0], 4)
        self.assertEqual(test_return[1][0], 3)
        self.assertEqual(test_return[2][0], 4)
        self.assertEqual(test_return[3][0], 4)
        self.assertEqual(test_return[4][0], 4)

    #Requieres Database preload file to be run for test to pass
    def testReturnStoreListUnderDistance(self):

        test_return = JobDataAccess.ReturnStoreListUnderDistance(-78.625679, 35.819539, 3)

        self.assertEqual(test_return[0][0], 1)
        self.assertEqual(test_return[1][0], 2)
        try:
            #this shouldnt return as its over 3 miles
            self.assertEqual(test_return[2][0], 3)
        except:
            pass


if __name__ == '__main__':
    unittest.main()
