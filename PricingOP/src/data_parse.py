""" 
File to parse and process data into readable dictionaries for pricing optimizations

"""

import requests
import pandas as pd
import numpy as np 


#--- TESTS ---
extra = True
websites = {"Dist A": "www.testA.com", "Dist B": "www.testB.com"}


response = requests.get("website goes here")



if response.status_code == 200: #checks request 
    print("Success! Fetching Data...")
    data = response.json()
else:
    print("Error fetching data")
    print(response.status_code)
print(response)
    
# --- ACTUAL CODE ---
class WebsiteManager:
    def __init__(self):
        pass

#maybe use headers function
    def add_website(self):
        while extra:
            print(websites)
            check = new_website = input("Do you have any additional websites? (yes/no) ")
            check.lower()
            try:
                if check == "yes":
                    new_website = input("Please enter the website URL: ")
                    websites[new_website] = new_website
                elif check == "no":
                    extra = False
                else:
                    raise ValueError("Invalid input")
            except ValueError as e:
                print(e)

    def remove_website(self):
        #code to remove website from list
        #by position or by name
        pass
        #we can print the keys to determine

    def update_website(self):
        #code to update if urls change but you want to maintain key
        pass

    def view_websites(self): #print distributor websites
        for key, value in websites.items():
            print(f"Distributor: {key}, Website: {value}")

    def analyze_websites(self): #this organizes the data into a readable format for me
        # code to analyze website data
        pass

    def build_data(self): #this puts data into dictionary
        pass