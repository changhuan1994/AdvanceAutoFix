try:
    from User import User
except:
    from AAP1.User import User

#special user class for Mechanics
#Author Trey Ellis
class Mechanic(User):
    def __init__(self, user_id, full_name, user_name, ASECert_id, address, bio, paypal_info, ASECert_HTTP):
        
        self.user_id = user_id 
        self.full_name = full_name
        self.user_name = user_name
        self.ASECert_id = ASECert_id
        self.address = address 
        self.bio = bio
        self.paypal_info = paypal_info
        self.ASECert_HTTP = ASECert_HTTP

        #super().__init__(self, user_id,full_name, user_name, password, address, bio)

    #get and set for ASECert_id
    def get_ASECert_id(self):
        return self.ASECert_id

    def set_ASECert_id(self, new_ASECert_id):
        self.ASECert_id = new_ASECert_id 
        return self.ASECert_id

    #get and set for ASECert_HTTP
    def get_ASECert_HTTP(self):
        return self.ASECert_HTTP

    def set_ASECert_HTTP(self, new_ASECert_HTTP):
        self.ASECert_HTTP = new_ASECert_HTTP 
        return self.ASECert_HTTP


    #get and set for paypal
    def get_paypal_info(self):
        return self.paypal_info

    def set_paypal_info(self, new_paypal_info):
        self.paypal_info = new_paypal_info 
        return self.paypal_info