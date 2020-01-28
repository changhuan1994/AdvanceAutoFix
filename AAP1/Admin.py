try:
    from User import User
except:
    from AAP1.User import User
#special user class for admins
#Author Trey Ellis
class Admin(User):
    def __init__(self, user_id, full_name, user_name, address, bio):
        
        self.user_id = user_id 
        self.full_name = full_name
        self.user_name = user_name
        self.address = address 
        self.bio = bio
        
        #super().__init__(self, user_id,full_name, user_name, password, address, bio)