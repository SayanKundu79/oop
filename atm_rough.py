class ATM:
    def __init__(self):
        self.__pin=""# private
        self.__balance=0
        self.__menu()
    def __menu(self):
      while True:
        user_input=input("""
                        press 1 to create pin:
                        press 2 to deposit
                         press 3 to withdraw
                         press 4 to check balance 
                         press 5 to get pin
                         press 6 to change pin
                         press 7 to exit
                         """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        elif user_input=="5":
            self.get_pin()
        elif user_input=="6":
            self.set_pin()
        else :
            exit(0)
    def create_pin(self):
       
       while True:
        pin = input("Enter your 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4:
            self.__pin = int(pin)
            break
        else:
             print("❌ Invalid PIN. Please enter exactly 4 digits.")
    def get_pin(self):
        print(f"Your pin is {self.__pin}")
    def set_pin(self):
        new_pin=input("Enter new pin")
        if type(new_pin) ==str:
            self.__pin=new_pin
            print("pin changed succesfully")
    def deposit(self):
        amount=int(input("Enter the amount = "))
        self.__balance=self.__balance+amount
        print("Deosit succesfully")
        self.check_balance()
    def withdraw(self):
        wamount=int(input("Enter the Amount = "))
        if self.__balance>wamount:
            self.__balance=self.__balance-wamount
            print(f"Withdrawl of ₹{wamount} has been succesfull")
        else:
            print("Not have sifficient amount")
        self.check_balance()
    def check_balance(self):
        print(f"💳 Your account balance is ₹{self.__balance}")
 
sbi=ATM()

