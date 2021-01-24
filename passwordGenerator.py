# This is a Random Password & OTP Generator written in Python

# Import Library
import math, random, string


def generate_OTP(len) :
    
	digits = "0123456789"
	OTP = "" 

	for i in range(len) : 
		OTP += digits[math.floor(random.random() * 10)] 

	return OTP 


def generate_password(len) :
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(len)))
    return result_str


def Main() :
    print("!! Random Password Generator !!")
    print("0: Exit")
    print("1: Generate Password")
    print("2: Generate OTP")
    choice = int(input("Enter your choice : "))

    if choice == 0 :
        print(exit)

    elif choice == 1:
        len = int(input("Enter the length of Password : "))
        print("password : ",generate_password(len))

    elif choice ==2:
        len = int(input("Enter the length of OTP : "))
        print("OTP : ",generate_OTP(len))

    else :
        print("OOPS !!")
        print("Check your input.")

    


if __name__ == "__main__" : 
    Main()