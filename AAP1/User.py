#parent Class for User Types
#Author Trey Ellis
class User(object):
    def __init__(self, user_id, full_name, user_name, address, bio):

        self.user_id = user_id 
        self.full_name = full_name
        self.user_name = user_name
        self.address = address 
        self.bio = bio


    #returns user variables
    def get_user_id(self):
        return self.user_id

    def get_full_name(self):
        return self.full_name

    def get_user_name(self):
        return self.user_name

    def get_address(self):
        return self.address

    def get_bio(self):
        return self.bio

    #sets user variables
    def set_user_id(self, new_id):
        self.user_id = new_id 
        return self.user_id

    def set_full_name(self, new_full_name):
        self.full_name = new_full_name
        return self.full_name

    def set_user_name(self, new_user_name):
        self.user_name = new_user_name
        return self.user_name

    def set_address(self, new_address):
        self.address = new_address 
        return self.address

    def set_bio(self, new_bio):
        self.bio = new_bio
        return self.bio