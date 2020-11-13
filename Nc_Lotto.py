#Obelisk

print()
print("NC EDUCATION LOTTERY, LLC")
print("Welcome to the North Carolina Education Lottery's proprietary number selection and bank deposit interface.")
print()
reg_user = input("Are you a certified lottery official?")

if reg_user == "no":
    print("Please contact North Carolina Education Lottery Office in Raleigh")
    exit()

else:
    user_pin = input("Please enter your four-digit, certified lottery official PIN: ")
if user_pin == "1234":
    print("PIN accepted.")

else:
    print("PIN invalid.")
    print("Goodbye!")
    exit()
print()
print("Please set answers to security questions for future logins:")
print()
def security_questions():
    q1 = input("Mother's maiden name?")
    q2 = input("City of birth?")
    q3 = input("Favorite childhood pet?")

security_questions()
print()
user_ssn = input("Thank you, your identity has been confirmed. Please enter your Social Security number, then press enter:")
print()
print("Your account has been verified.")
print()
print("Bank information is required in order to deposit lottery funds. Please answer the following questions to proceed.")
print()
bank_account = input("Please enter your bank account number: ")
routing_number = input("Please enter bank routing number: ")
bank_balance = input("Please enter current account balance to synchronize bank and lottery servers: ")
bank_balance =+ .01
print()
print()
print("Thank you....please wait while our servers connect to your bank")
print()
print()
print("Connection succesful!")
print()
print("Now generating your lottery numbers...")
print()
print()
enter_input = input("Complete! Please press enter to recieve your lottery numbers!")

winning_numbers = [49, 2, 56, 81, 5, 32]
print()
print("Your lottery numbers are " + str(winning_numbers))
print()
winner_response = input("Would you like to compare your numbers against winning numbers?")
print()
if winner_response == "yes":
    print("Your numbers are...", winning_numbers)
    print( "The winning numbers are...", winning_numbers)
else:
    print("Goodbye!")
    exit()
print()
print("Congratulations! You are a winner!")
print()
transfer_cnfrm = input("Current Jackpot is: $168,000,000. Would you like to transfer lottery funds to the bank account provided above?")

jp = 168000000
if transfer_cnfrm == "yes":
    print()
    update = input("Updating your bank balance...")
    print()
else:
    print("Thank you, goodbye!")

print("Your updated account balance is ", jp + bank_balance)
