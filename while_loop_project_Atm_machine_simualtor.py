#Atm Machine simulator project
#First of all here we will create three varaibles like:
Pin_number = 1234
attempts = 0
Balance = 5000  # starting Balance
#So now we're gonna using while True Condition in this first we will 
#ask from the user about pin number
while True:
    entered_pin = int(input("Please enter you pin number"))
# Now we're using the if condition if the entered_pin is equal to pin_number then 
#then we the pin will be accepting and loop ganna go break 
    if entered_pin == Pin_number:
        print("pin accepted! Welcome to your account!\n")
        
        #Main Menu of the Atm
        while True:
            print("---ATM MENU----")
            print("1.Check balance")
            print("2.Deposit Money")
            print("3.withdraw Money")
            print("4.exit")
            choice = int(input("choose an option(1 to 4):"))
            if choice == 1:
                print(f"your current balance is: {Balance}PKR\n")
            #First we will ask from the user that how much money he wants to deposit
            elif choice == 2:
                deposit_amount = int(input("Enter the amount to deposit: "))
                #so now we will add the amount into the current balance
                Balance += deposit_amount # so it means that balance = balance+deposit
                print(f"{deposit_amount}PKR is successfully deposited!")
                print(f"your new balance is: {Balance}PKR\n")
            elif choice == 3:
                # Now we will ask from the user that how much money he
                #wants to withdraw
                withdraw_amount = int(input("Enter the amount to withdraw: "))
                # Ab check karenge ke kya user ke paas itne paise hain?
                if withdraw_amount <= Balance:
                    Balance -= withdraw_amount  # It means the Balance is subtracted from the current Balance
                    print(f"{withdraw_amount} PKR successfully withdrawn!")
                    print(f"Remaining balance: {Balance} PKR\n")
                else:
                    print("Transaction Failed! The amount is insufficient.\n")

