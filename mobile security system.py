class MobileSecurity:
    
    def __init__(self, owner_name):
        
        self.__owner = owner_name
        self.__password = "1234"
        self.__status = "Locked"

    # Method to unlock the phone
    def unlock(self):
        if self.__status == "Unlocked":
            print("\nMobile is unlocked.")
        else:
            password = input("\nEnter Password : ")
            if password == self.__password:
                self.__status = "Unlocked"
                print("\nMobile Unlocked Successfully")
               
            else:
                print("\nIncorrect Password! Access Denied.")

    # Method to lock the phone
    def lock(self):
        if self.__status == "Locked":
            print("\nMobile is already locked.")
        else:
            self.__status = "Locked"
            print("\nMobile Locked Successfully")

    # Method to change the password safely
    def change_password(self):
        old_password = input("\nEnter Old Password: ")
        if old_password == self.__password:
            new_password = input("Enter New Password: ")
            self.__password = new_password
            print("\nPassword Changed Successfully")
        else:
            print("\nIncorrect Old Password!")

    # Method to show mobile details
    def show_details(self):
        print("\n========== MOBILE DETAILS ==========")
        print("Owner   :", self.__owner)
        print("Status  :", self.__status)
        print("====================================")


# Main Program starts here
print("========== MOBILE SECURITY SYSTEM ==========")
name = input("Enter Mobile Owner Name : ")

# Creating the object of the class
my_mobile = MobileSecurity(name)
print("\nMobile Security System Started")


while True:
    print("\n========== MENU ==========")
    print("1. Unlock Mobile")
    print("2. Lock Mobile")
    print("3. Change Password")
    print("4. Mobile Status")
    print("5. Exit")

    choice = input("\nEnter Choice : ")
    print("(Note: Default password is 1234)")
    
    
    if choice == '1':
        my_mobile.unlock()
    elif choice == '2':
        my_mobile.lock()
    elif choice == '3':
        my_mobile.change_password()
    elif choice == '4':
        my_mobile.show_details()
    elif choice == '5':
        print("\nThank You... 😊\n")
        break
    else:
        print("\nInvalid Choice! Please enter a number from 1 to 5.")
