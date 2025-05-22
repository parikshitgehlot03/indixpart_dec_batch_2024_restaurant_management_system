from datetime import datetime
from SRC.authentication.sign_in import SignIn_Management
from SRC.authentication.sign_up import SignUp_Management

class Manage:

    def __init__(self):
        self.Staffpath = rf"D:\indixpart_dec_batch_2024_restaurant_management_system\SRC\database\employee.json"
        self.Adminpath = rf"D:\indixpart_dec_batch_2024_restaurant_management_system\SRC\database\admin.json"
        self.Logpath = rf"D:\indixpart_dec_batch_2024_restaurant_management_system\SRC\logs\Logs.txt"
        self.EmployeeData = []

    def write_log(self, message):
        with open(self.Logpath, "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] {message}\n")

    def management(self):
        try:
            print("** Shandaar Restaurant **")
            print("1 - Sign in")
            print("2 - Sign up")
            print("3 - Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                signin_ins = SignIn_Management()
                signin_ins.Signin(self.Adminpath, self.Staffpath)
            elif choice == 2:
                signup_ins = SignUp_Management()
                signup_ins.Signup(self.Staffpath)
            elif choice == 3:
                print("Exiting program...")
                exit()
            else:
                print("Enter valid choice!")
                self.management()

        except ValueError as ve:
            self.write_log(f"ValueError: Invalid input! Expected a number. Details: {ve}")
            print("Please enter a valid number.")
            self.management()
        except Exception as e:
            self.write_log(f"Exception: Unexpected error occurred. Details: {e}")
            print("An unexpected error occurred. Please try again.")
            self.management()