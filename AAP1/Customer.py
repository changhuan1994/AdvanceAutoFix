try:
    from User import User
except:
    from AAP1.User import User


#special user class for admins
#Author Trey Ellis
class Customer(User):
    def __init__(self, user_id, full_name, user_name, address, bio, paypal_info):
        
        self.user_id = user_id 
        self.full_name = full_name
        self.user_name = user_name
        self.address = address 
        self.bio = bio
        self.paypal_info = paypal_info
        
        #super().__init__(self, user_id,full_name, user_name, password, address, bio)

    #get and set for paypal
    def get_paypal_info(self):
        return self.paypal_info

    def set_paypal_info(self, new_paypal_info):
        self.paypal_info = new_paypal_info 
        return self.paypal_info