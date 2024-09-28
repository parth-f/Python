# Q3. Create a python application for the following requirement . It is a banking application having minimum 5 accounts 
# in it. Class bank is having following details bankName, branch name,IFSC code , accountList(5 accounts) Class Account
#  is having following details AccHolderName ,mobileNumber , accNumber, balance Minimum balance amount of Rs3000 must 
# be there in account . 
# Implement following functions:: 
# 1:accept bank information 
# 2:print bank information 
# 3:add new account 
# 4.print information of all accounts 
# 5.print information of selected accounts 
# 6.delete selected account (Return 1 if deleted else 0) 
# 7.Deposit amount in a account (Return updated balance) 
# Write a menu driven program to achieve above requirements.

class Account:
    bank_name = "State Bank of India"
    branch_name = "Gurgaon"
    ifsc_code = "SBIN00049"


    def __init__(self,acc_holder_name, mobile_number, acc_number, balance):
        self.acc_holder_name = acc_holder_name
        self.mobile_number = mobile_number
        self.acc_number = acc_number

        class MinBalanceError(Exception):
            # Raised to show min balance reqired in the bank is 3000
            pass

        try:
            self.balance = balance
            if self.balance < 3000:
                raise MinBalanceError
        except MinBalanceError:
            print(f"Min Balance of 3000 Rs /- is required for your account creation {self.acc_holder_name}, You have {self.balance} which is lower than 3000")     
            del self.balance       
    
    def print_info(self):
        try:
            self.balance
            print("Name of Account Holder - ",self.acc_holder_name)
            print("Mobile Number - ",self.mobile_number)
            print("Account Number - ",self.acc_number)
            print("Account Balance - ",self.balance)
        except AttributeError:
            print(f"Min Balance of 3000 Rs /- is required for your account creation {self.acc_holder_name}")

hement = Account("Hemant Takhur",94203,284829842,4000)
hement.print_info()

print("")

rekha = Account("Rekha Savant",942,2423,300)
rekha.print_info()
    

