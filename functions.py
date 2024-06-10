import csv
import pandas as pd
import sys

def verify_user(ic_number, password, filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == ic_number and row[1] == password:
                return True
    return False

def calculate_tax(income, tax_relief):
    chargeable_income=income - tax_relief

    # Example tax brackets (replace with actual Malaysian tax brackets)
    if chargeable_income <= 5000:
        tax_payable = 0
    elif chargeable_income <= 20000:
        tax_payable = (chargeable_income-5000) * 0.01
    elif chargeable_income <= 35000:
        tax_payable = (chargeable_income-20000) * 0.03 + 150
    elif chargeable_income <= 50000:
        tax_payable = (chargeable_income-35000) * 0.06 + 600
    elif chargeable_income <= 70000:
        tax_payable = (chargeable_income-50000) * 0.11 + 1500
    elif chargeable_income <= 100000:
        tax_payable = (chargeable_income-70000) * 0.19 + 3700
    elif chargeable_income <= 400000:
        tax_payable = (chargeable_income-100000) * 0.25 + 9400
    elif chargeable_income <= 600000:
        tax_payable = (chargeable_income-400000) * 0.26 + 84400
    elif chargeable_income <= 2000000:
        tax_payable = (chargeable_income-600000) * 0.28 + 136400
    else:
        tax_payable = (chargeable_income-2000000) * 0.3 + 528400
    return tax_payable

def save_to_csv(data, filename):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(["IC Number", "Annual Income", "Tax Relief", "Tax Payable"])
        writer.writerow([data["IC Number"], data["Annual Income"], data["Tax Relief"], data["Tax Payable"]])

def read_from_csv(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return None

def register_user(filename):
    ic_number = input("Enter your IC number: ")
    password = input("Enter your password(last 4 digits of your IC): ")
    if len(ic_number) != 12 or len(password) != 4:
        print("Invalid IC number or password. Please try again.")
        return None
    with open(filename, 'a', newline="") as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(["IC Number", "Password"])
        writer.writerow([ic_number, password])
    return {"ic_number": ic_number, "password": password}

def login_user(filename):
    ic_number = input("Enter your IC number: ")
    password = input("Enter your password(last 4 digits of your IC): ")
    if verify_user(ic_number, password, filename):
        return ic_number
    else:
        return None