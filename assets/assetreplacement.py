import csv
import os
import sys
from datetime import datetime
import pandas as pd


class Vehicle:
    def __init__(self, name, purchase_year, replacement_years):
        self.name = name
        self.purchase_year = purchase_year
        self.replacement_years = replacement_years
        self.replacement_year = self.purchase_year + self.replacement_years

    def name_check(self):
        df = pd.read_csv('vehicle_replacement.csv')
        if self.name in df['Vehicle'].values:
            self.purchase_year = df.loc[df['Vehicle'] == self.name, 'Purchase Year'].values[0]
            self.replacement_years = df.loc[df['Vehicle'] == self.name, 'Replacement Year'].values[0]
            self.replacement_year = self.purchase_year + self.replacement_years
            print("Existing values: Purchase Year =", self.purchase_year, "Replacement Years =", self.replacement_years)
            return True

    def safety_risk(self):
        response = validate_input("Is this asset a safety risk? (yes/no): ", ["yes", "no"])
        if response == "yes":
            self.replacement_year = datetime.now().year
            self.write_to_csv()
            print("The vehicle is a safety risk and will be replaced this year.")
            sys.exit()

    def service_risk(self):
        response = validate_input("Is this asset still meeting service levels? (yes/no): ", ["yes", "no"])
        if response == "no":
            self.replacement_year = datetime.now().year
            self.write_to_csv()
            print(
                "This vehicle is no longer meeting it's expected service levels, please prepare a business case to up/downgrade")
            sys.exit()
            return True

    def condition_assessment(self, assessment):
        assessment_values = {5: 4, 4: 3, 3: 2, 2: 1, 1: 0}
        self.replacement_year += assessment_values.get(assessment, 0)

    def manager_adjustment(self, adjustment):
        self.replacement_year += adjustment

    def write_to_csv(self):
        df = pd.read_csv('vehicle_replacement.csv')
        # print(df)
        df2 = {'Vehicle': self.name, 'Purchase Year': self.purchase_year, 'Replacement Year': self.replacement_year}
        df.loc[len(df.index)] = df2
        # print (df)
        df.to_csv('vehicle_replacement.csv', index=False)


def validate_input(prompt, valid_response):
    while True:
        response = input(prompt).lower()
        if response in valid_response:
            return response
        print("Invalid input, please enter a valid response")


def write_to_csv(filename, fieldnames, data):
    with open(filename, mode='a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

Vehicle_name = input("Enter the vehicle number: ")
vehicle = Vehicle(Vehicle_name, None, None)
if vehicle.name_check() != True:
    Purchase_year = int(input("Enter the purchase year: "))
    Replacement_years = int(input("Enter the replacement years in policy: "))
    vehicle = Vehicle(Vehicle_name, Purchase_year, Replacement_years)

Assessment = int(input("Enter the condition assessment (5 for excellent, 4 for good, 3 for fair, 2 for poor, 1 for failed): "))
vehicle.condition_assessment(Assessment)

Manager_Adjustment_Necessary = validate_input("Is a manager adjustment necessary? (yes/no): ", ["yes", "no"])
if Manager_Adjustment_Necessary == "yes":
    Manager_Adjustment = int(input("Enter the manager adjustment (enter a positive or negative integer): "))
    vehicle.manager_adjustment(Manager_Adjustment)
    vehicle.write_to_csv()
    print("The adjusted replacement year for the", vehicle.name, "purchased in", vehicle.purchase_year, "is:",
          vehicle.replacement_year)
    print("The information has been written to vehicle_replacement.csv")
elif Manager_Adjustment_Necessary == "no":
    vehicle.write_to_csv()
