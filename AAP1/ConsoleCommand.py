from UserDataAccess import UserDataAccess
from Mechanic import Mechanic

#author Trey Ellis
print("Welcome to the basic AAP Command consle!")
while True:
    print("")
    print("1. Add Mechanic User")
    print("2. Return User By User Name")
    print("3. Remove User by User Name")
    print("4. Remove User by ID")
    print("5. Update User By User ID")
    print("6. Add Default User")
    print("Quit")
    print("Please make a selection")

    Input = str(input())
    if (Input.lower() == "quit"):
        print("Thanks for your time!")
        quit()
    
    if (Input.lower() == "1"):
        print("Please enter the full name.")
        full_name = str(input())
        print("Please enter the user name")
        user_name = str(input())
        print("Please enter the password")
        password = str(input())
        print("Please enter the address")
        address = str(input())
        print("Please enter the bio info")
        bio = str(input())
        print("Please enter the PayPal info")
        paypal_info = str(input())

        UserDataAccess.AddUser(full_name, user_name, password, address, bio, paypal_info)
        print("User created!")
    
    if (Input.lower() == "2"):
        print("Please enter the user name")
        user_name = str(input())

        User_Return = UserDataAccess.ReturnUserByUserName(user_name)
        Output_User = Mechanic(int(User_Return[0]), User_Return[1].decode("utf-8" ), User_Return[2].decode("utf-8" ), User_Return[3].decode("utf-8" ), User_Return[4].decode("utf-8" ), User_Return[5].decode("utf-8" ), User_Return[6].decode("utf-8" ))
        print("User ID")
        print(Output_User.get_user_id())
        print("User name")
        print(Output_User.get_user_name())
        print("Full Name")
        print(Output_User.get_full_name())
        print("Password")
        print(Output_User.get_password())
        print("Bio")
        print(Output_User.get_bio())
        print("address")
        print(Output_User.get_address())
        print("Paypal Info")
        print(Output_User.get_paypal_info())

        
    if (Input.lower() == "3"):
        print("Please enter the User Name.")
        user_name = str(input())

        UserDataAccess.RemoveUserbyUserName(user_name)
        print("User removed!")



        
    if (Input.lower() == "4"):
        print("Please enter the User ID.")
        user_id = int(input())

        UserDataAccess.RemoveUserbyID(user_id)
        print("User removed!")
    
    
    if (Input.lower() == "5"):
        print("Please enter the User Id to change.")
        user_id = str(input())
        print("Please enter the full name.")
        full_name = str(input())
        print("Please enter the user name")
        user_name = str(input())
        print("Please enter the password")
        password = str(input())
        print("Please enter the address")
        address = str(input())
        print("Please enter the bio info")
        bio = str(input())
        print("Please enter the PayPal info")
        paypal_info = str(input())


        UserDataAccess.UpdateUserByUserID( user_id, full_name, user_name, password, address, bio, paypal_info)
        print("User Changed!")

    
    if (Input.lower() == "6"):
        print("Adding Default user BobTheBuilder.")
        UserDataAccess.AddUser("Bob Jhones", "BobTheBuilder", "password", "Builder Rd", "I can Build it", "Pay Me")


    
        

