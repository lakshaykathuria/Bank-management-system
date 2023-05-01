
import connection

print('Welcome To The Project\n'.center(100))
print('Of\n'.center(100))
print('Banking Structure'.center(100))
print("Press Enter To Continue\n")
b=input()
print("Options")
print("""1. To Create Account
2. To See All Record
3. For Balance Enquiry
4. To Debit
5. To Credit
6. Exit""")
menu=int(input("Enter Your Choice:\n"))
if menu==1:
    import Create_Account
    import Account_No
    a = input()
elif menu == 2:
    import name
    import phone
    import address
    import Account_Type
    import balance
    print("Account Holder Name:",name.Holder_Name)
    print("Phone Number:",phone.number)
    print("Address:",address.address)
    print("Account Type:",Account_Type.type)
    print("Balance:",balance.balance)
    input()
elif menu==3:
    import balance
    print("Balance:",balance.balance)
    input()
elif menu==4:
    import Debit
    input()
elif menu==5:
    import Credit
    input()
elif menu==6:
    print("Thank You")
else:
    print("Please Enter A valid Input")

