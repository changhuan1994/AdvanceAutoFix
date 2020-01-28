#parent Class for Jobs
#Author Trey Ellis
class Job(object):
    def __init__(self, job_id, job_type_id, address, details, cus_id, customer_name, job_type_name):

        self.job_id = job_id 
        self.job_type_id = job_type_id
        self.address = address
        self.details = details 
        self.cus_id = cus_id
        self.customer_name = customer_name
        self.job_type_name = job_type_name

    #returns user variables
    def get_job_id(self):
        return self.job_id

    def get_job_type_id(self):
        return self.job_type_id

    def get_address(self):
        return self.address

    def get_details(self):
        return self.details

    def get_cus_id(self):
        return self.cus_id

    def get_customer_name(self):
        return self.customer_name

    def get_job_type_name(self):
        return self.job_type_name

    #sets user variables
    def set_job_id(self, new_id):
        self.job_id = new_id 
        return self.job_id

    def set_job_type_id(self, new_id):
        self.job_type_id = new_id 
        return self.job_type_id

    def set_address(self, new_address):
        self.address = new_address 
        return self.address

    def set_details(self, new_details):
        self.details = new_details 
        return self.details

    def set_user_id(self, new_id):
        self.user_id = new_id 
        return self.user_id

    def set_cus_id(self, new_id):
        self.user_id = new_id 
        return self.cus_id

    def set_customer_name(self, new_customer_name):
        self.customer_name = new_customer_name 
        return self.customer_name

    def set_job_type_name(self, new_job_type_name):
        self.job_type_name = new_job_type_name 
        return self.job_type_name