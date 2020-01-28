try:
    from ConnectionPool import connectionPool
    from Job import Job
    
except :
    from AAP1.ConnectionPool import connectionPool
    from AAP1.Job import Job

import time
import datetime

# Class that serves as the Data access object for the Job object.
#Author Trey Ellis
class JobDataAccess():

    #Returns a Job from the database with Job Id : job_id
    #returns the job if successful, -1 if not
    @staticmethod
    def ReturnJobByID( job_id):
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 

        commandPart1 = "SELECT jobs.job_id, jobs.job_type_id, jobs.address, jobs.details, jobs.cus_id, users.full_name, job_types.job_name "
        commandPart2 = "FROM jobs "
        commandPart3 = "INNER JOIN job_types ON jobs.job_type_id = job_types.job_type_id "
        commandPart4 = "INNER JOIN users ON jobs.cus_id = users.user_id "
        commandPart5 = "where job_id = '{}';".format(job_id)


        command = commandPart1 + commandPart2 + commandPart3 + commandPart4 + commandPart5
        #print(command)

        connection_object.cmd_query(command)
        job_Return = connection_object.get_rows()
        #should only be one row so pull the first
        try:
            Job_Return = job_Return[0][0]
        except:
            connection_object.close()
            return -1

        Job_output =  Job(int(Job_Return[0]), int(Job_Return[1]), Job_Return[2].decode("utf-8" ), Job_Return[3].decode("utf-8" ), int(Job_Return[4]), Job_Return[5].decode("utf-8" ), Job_Return[6].decode("utf-8" ))
        connection_object.close()

        return Job_output



    #Returns The Job List from the database
    #returns the job List if successful, -1 if not
    @staticmethod
    def ReturnJobList():
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 



        commandPart1 = "SELECT jobs.job_id, jobs.job_type_id, jobs.address, jobs.details, jobs.cus_id, users.full_name, job_types.job_name \n"
        commandPart2 = "FROM jobs \n"
        commandPart3 = "INNER JOIN job_types ON jobs.job_type_id = job_types.job_type_id \n"
        commandPart4 = "INNER JOIN users ON jobs.cus_id = users.user_id\n"
        commandPart5 = "order by job_id;"

        command = commandPart1 + commandPart2 + commandPart3 + commandPart4 + commandPart5
        print(command)

        connection_object.cmd_query(command)
        job_Return = connection_object.get_rows()

        try:
            Job_Return = job_Return[0]
        except:
            connection_object.close()
            return -1

        connection_object.close()

        joblist = []

        for i in Job_Return:
            #print(i)
            nextJob = Job(int(i[0]), int(i[1]), i[2].decode("utf-8" ), i[3].decode("utf-8" ), int(i[4]), i[5].decode("utf-8" ), i[6].decode("utf-8" ))
            joblist.append(nextJob)

        return joblist


    #Returns The Job List from the database that are under the distance cap compared to the location passed
    #returns the job List if successful, -1 if not
    @staticmethod
    def ReturnJobListUnderdistance(logitude, latitude, distance, mec_id, job_type_ids):

        #print( isinstance( logitude, float))
        #print( isinstance( latitude, float))
        #print( isinstance( distance, int))
        #print( isinstance( mec_id, int))
        #print( isinstance( job_type_ids, list))

        #if passed values are not all ints it could be an sql injection
        if (not isinstance( logitude, float) and not isinstance( latitude, float) and not isinstance( distance, int) 
            and not isinstance( mec_id, int) and not isinstance( job_type_ids, list) ):
            raise ValueError('Passed values were not an int. Mysql database protected')
        

        job_type_id_string = ""
        index = 0
        for i in job_type_ids:

            #print(i)
            #checks all ids to make sure they are ints
            if (not isinstance( i, int)):
                raise ValueError('Passed Ids were not an int. Mysql database protected')

            #builds the job_type_id_string from the ints
            if (index == 0):
                job_type_id_string = job_type_id_string + "{}".format(i)
            else:
                job_type_id_string = job_type_id_string + ", {}".format(i)

            index += 1
            
        #print(job_type_id_string)
        
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 

        """ #Iteration 1 pulls jobs under distance 
        commandPart1 = "SELECT jobs.job_id, jobs.job_type_id, jobs.address, jobs.details, jobs.cus_id, users.full_name, job_types.job_name,\n"
        commandPart2 = "ST_Distance_Sphere(POINT('{}', '{}'), location)* .000621371192 as distance\n".format(logitude, latitude)
        commandPart3 = "FROM jobs\n"
        commandPart4 = "INNER JOIN job_types ON jobs.job_type_id = job_types.job_type_id\n"
        commandPart5 = "INNER JOIN users ON jobs.cus_id = users.user_id\n"
        commandPart6 = "having distance < '{}'\n".format(distance)
        commandPart7 = "ORDER BY distance;" 
        """
        """
        #Iteration 2 With preferences and only qualified unbooked jobs
        commandPart1 = "SELECT jobs.job_id, jobs.job_type_id, jobs.address, jobs.details, jobs.cus_id, users.full_name, job_types.job_name,\n"
        commandPart2 = "ST_Distance_Sphere(POINT('{}', '{}'), location)* .000621371192 as distance\n".format(logitude, latitude)
        commandPart3 = "FROM jobs\n"
        commandPart4 = "INNER JOIN job_types ON unbooked.job_type_id = job_types.job_type_id\n"
        commandPart5 = "INNER JOIN users ON unbooked.cus_id = users.user_id\n"
        commandPart6 = "INNER JOIN job_qualifications ON job_types.job_type_id = job_qualifications.job_type_id\n"
        commandPart7 = "WHERE jobs.job_id not in (Select job_id from bookings)\n"
        commandPart8 = "AND jobs.job_type_id in ('{}')\n".format(job_type_id_string)
        commandPart9 = "AND job_qualifications.qual_id in (Select qual_id from mechanics_qualifications where mec_id = '{}')\n".format(mec_id)
        commandPart10 = "having distance < '{}'\n".format(distance)
        commandPart11 = "ORDER BY distance;\n"
        """


        
        #Iteration 3 With preferences and only qualified unbooked jobs Allows for jobtypes with more than one qualification
        commandPart1 = "SELECT jobs.job_id, jobs.job_type_id, jobs.address, jobs.details, jobs.cus_id, users.full_name, job_types.job_name,\n"
        commandPart2 = "ST_Distance_Sphere(POINT('{}', '{}'), location)* .000621371192 as distance\n".format(logitude, latitude)
        commandPart3 = "FROM jobs\n"
        commandPart4 = "INNER JOIN job_types ON jobs.job_type_id = job_types.job_type_id\n"
        commandPart5 = "INNER JOIN users ON jobs.cus_id = users.user_id\n"
        commandPart6 = "WHERE jobs.job_id not in (Select job_id from bookings)\n"
        commandPart7 = "AND jobs.job_type_id in ({})\n".format(job_type_id_string)
        commandPart8 = "AND job_types.job_type_id not in \n"
        commandPart9 = "(select job_type_id from job_qualifications where qual_id not in (Select qual_id from mechanics_qualifications where mec_id = '{}'))\n".format(mec_id)
        commandPart10 = "having distance < '{}'\n".format(distance)
        commandPart11 = "ORDER BY distance;\n"
        

        command = commandPart1 + commandPart2 + commandPart3 + commandPart4 + commandPart5 + commandPart6 + commandPart7 + commandPart8 + commandPart9 + commandPart10 + commandPart11
        #print(command)


        connection_object.cmd_query(command)
        job_Return = connection_object.get_rows()

        try:
            Job_Return = job_Return[0]
        except:
            connection_object.close()
            return -1

        connection_object.close()

        joblist = []

        for i in Job_Return:
            #print(i)
            nextJob = Job(int(i[0]), int(i[1]), i[2].decode("utf-8" ), i[3].decode("utf-8" ), int(i[4]), i[5].decode("utf-8" ), i[6].decode("utf-8" ))
            joblist.append(nextJob)

        return joblist


    #Books the job with the job id passed, the mechanic id passed, and the selected store id passed
    #returns 1 if successful
    @staticmethod
    def BookJob(job_id, store_id, mec_id):


        acceptedStatus_id = 1

        command = "insert into bookings(job_id, store_id, mec_id) 	values('{}', '{}', '{}');".format(job_id, store_id, mec_id)
        #print(command)


        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        connection_object.commit()
        connection_object.close()

        JobDataAccess.insertStatus(acceptedStatus_id, job_id, "accepted job")

        return 1

    #Un Books the job with the job id passed
    @staticmethod
    def UnBookJob(job_id):

        command = "delete from bookings where job_id = '{}';".format(job_id)
        #print(command)


        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        connection_object.commit()
        connection_object.close()


    #Returns the list of all booked jobs
    #returns the Booked job List if successful, -1 if not
    @staticmethod
    def ReturnBookedJobs():

        command = "Select * from bookings;"
        #print(command)


        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        job_Return = connection_object.get_rows()

        try:
            Job_Return = job_Return[0]
        except:
            connection_object.close()
            return -1

        joblist = []

        for i in Job_Return:
            nextJob = [int(i[0]), int(i[1]), int(i[2])]
            joblist.append(nextJob)

        connection_object.close()

        return joblist


    #Returns the list of all booked jobs with a specific mech_id
    #returns the Booked job List if successful, -1 if not
    @staticmethod
    def ReturnBookedJobsWithMecID(mec_id):

        command = "Select * from bookings where mec_id = '{}';".format(mec_id)
        #print(command)


        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        job_Return = connection_object.get_rows()

        try:
            Job_Return = job_Return[0]
        except:
            connection_object.close()
            return -1

        joblist = []

        for i in Job_Return:
            nextJob = [int(i[0]), int(i[1]), int(i[2])]
            joblist.append(nextJob)

        connection_object.close()

        return joblist

    #Returns the list of all qualifications with a specific mech_id
    #returns the qualifications List if successful, -1 if not
    @staticmethod
    def ReturnQualificationsWithMecID(mec_id):


        commandPart1 = "Select mechanics_qualifications.qual_id, qualification.qualification_name\n"
        commandPart2 = "from mechanics_qualifications\n"
        commandPart3 = "INNER JOIN qualification ON mechanics_qualifications.qual_id = qualification.qual_id\n"
        commandPart4 = "where mec_id = '{}';".format(mec_id)

        #print(command)


        command = commandPart1 + commandPart2 + commandPart3 + commandPart4

        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        Qual_Return = connection_object.get_rows()

        try:
            Qual_Return = Qual_Return[0]
        except:
            connection_object.close()
            return -1

        qual_output = []
        
        #print(Qual_Return[0])
        #print(int(Qual_Return[0][0]), Qual_Return[0][1].decode("utf-8" ))

        for i in Qual_Return:
            qual_output.append( [int(i[0]), i[1].decode("utf-8" )] )

        connection_object.close()

        return qual_output

    #Returns the list of all jobtypes
    @staticmethod
    def ReturnJobTypesWithLink():


        command = "Select job_types.job_type_id, job_types.job_name, job_types.HHTP_Link from job_types;\n"

        print(command)

        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        Type_Return = connection_object.get_rows()

        try:
            Type_Return = Type_Return[0]
        except:
            connection_object.close()
            return -1

        type_output = []
        

        for i in Type_Return:
            type_output.append( [int(i[0]), i[1].decode("utf-8" ), i[2].decode("utf-8" )] )

        connection_object.close()

        return type_output

        

    #Returns the list of all status updates with a specific mech_id
    @staticmethod
    def ReturnJobHistoryOfMec(mec_id):



        commandPart1 = "Select status_list.job_id, status_list.status_update , status_list.status_time, users.full_name, job_types.job_name\n"
        commandPart2 = "from status_list\n"
        commandPart3 = "INNER JOIN jobs on status_list.job_id = jobs.job_id\n"
        commandPart4 = "INNER JOIN bookings on status_list.job_id = bookings.job_id\n"
        commandPart5 = "INNER JOIN job_types ON jobs.job_type_id = job_types.job_type_id\n"
        commandPart6 = "INNER JOIN users ON jobs.cus_id = users.user_id\n"
        commandPart7 = "where bookings.mec_id = '{}'".format(mec_id)
        commandPart8 = "order by status_time;"

        command = commandPart1 + commandPart2 + commandPart3 + commandPart4 + commandPart5 + commandPart6 + commandPart7 + commandPart8
        #print(command)

        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        History_Return = connection_object.get_rows()

        try:
            History_Return = History_Return[0]
        except:
            connection_object.close()
            return -1

        history_output = []
        
        for i in History_Return:
            history_output.append( [int(i[0]), i[1].decode("utf-8" ), i[2].decode("utf-8" ), i[3].decode("utf-8" ), i[4].decode("utf-8" )] )

        connection_object.close()

        return history_output

    #Returns the list of all status updates with a specific job_id
    @staticmethod
    def ReturnJobHistoryOfJob(job_id):



        commandPart1 = "Select status_list.status_id, status_list.job_id, status_list.status_update , status_list.status_time, users.full_name, job_types.job_name\n"
        commandPart2 = "from status_list\n"
        commandPart3 = "INNER JOIN jobs on status_list.job_id = jobs.job_id\n"
        commandPart4 = "INNER JOIN job_types ON jobs.job_type_id = job_types.job_type_id\n"
        commandPart5 = "INNER JOIN users ON jobs.cus_id = users.user_id\n"
        commandPart6 = "where status_list.job_id = '{}'".format(job_id)
        commandPart7 = "order by status_time;"

        command = commandPart1 + commandPart2 + commandPart3 + commandPart4 + commandPart5 + commandPart6 + commandPart7
        #print(command)

        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        History_Return = connection_object.get_rows()

        try:
            History_Return = History_Return[0]
        except:
            connection_object.close()
            return -1

        history_output = []
        
        for i in History_Return:
            history_output.append( [int(i[0]), int(i[1]), i[2].decode("utf-8" ), i[3].decode("utf-8" ), i[4].decode("utf-8" ), i[5].decode("utf-8" )] )

        connection_object.close()

        return history_output


    #Inserts a new status into the status_id, job_id, and status_update
    @staticmethod
    def insertStatus(status_id, job_id, status_update):

        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        command = "INSERT INTO Status_list(status_id, job_id, status_update, status_time) VALUES ({}, {}, '{}', '{}');".format(status_id, job_id, status_update, timestamp)
        #print(command)

        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        connection_object.commit()
        connection_object.close()

    #Returns a list of local stores under distance
    @staticmethod
    def ReturnStoreListUnderDistance(logitude, latitude, distance):

        commandPart1 = "Select store.store_id, store.store_address,\n"
        commandPart2 = "ST_Distance_Sphere(POINT('{}', '{}'), location)* .000621371192 as distance\n".format(logitude, latitude)
        commandPart3 = "from store\n"
        commandPart4 = "having distance < '{}'\n".format(distance)
        commandPart5 = "ORDER BY distance;\n"

        command = commandPart1 + commandPart2 + commandPart3 + commandPart4 + commandPart5
        #print(command)
        
        pool = connectionPool.getInstance()
        connection_object = pool.connection_pool.get_connection() 
        connection_object.cmd_query(command)
        Store_Return = connection_object.get_rows()

        try:
            Store_Return = Store_Return[0]
        except:
            connection_object.close()
            return -1

        store_output = []
        
        for i in Store_Return:
            store_output.append( [int(i[0]), i[1].decode("utf-8" )] )

        connection_object.close()

        return store_output