import csv
import pandas as pd
import sys
from functions import verify_user, calculate_tax, save_to_csv, read_from_csv, register_user, login_user
def main():
    tax_filename = "tax_records.csv"
    users_filename = "registered_users.csv"

    while True:
        choice = input("Enter '1' to Register, '2' to Login, '3' to view tax record, '4' to Exit: ")

        if choice == '1':
            user = register_user(users_filename)
            if user:
                print("Registration successful!")
        elif choice == '2':
            ic_number = input("Enter your IC number: ")
            password = input("Enter your password(last 4 digits of your IC): ")
            if verify_user(ic_number, password, users_filename):
                print("Login successful!")

                annual_income = float(input("Enter your annual income: RM "))
                tax_relief = float(input("Enter your total tax relief amount: RM "))

                tax_payable = calculate_tax(annual_income, tax_relief)
                print(f"Your tax payable is: RM {tax_payable:.2f}")

                data = {
                    "IC Number": ic_number,
                    "Annual Income": annual_income,
                    "Tax Relief": tax_relief,
                    "Tax Payable": tax_payable
                }

                save_to_csv(data, tax_filename)
                print("User data saved successfully!")

                records = read_from_csv(tax_filename)
                if records is not None:
                    print("\nTax Records:")
                    print(records)
                else:
                    print("No records found.")
            else:
                print("Invalid login credentials. Please try again.")
        elif choice == '3':
            df = read_from_csv(tax_filename)
            if df is not None:
                print(df)
            else:
                print("No tax records found.")
                
        elif choice == '4':
            print("Exit the program. THANK YOU!")
            # Add this line to exit the program
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

main()