import csv
import random
import time
import json
import os
import lastNameGenerator
import firstNameGenerator
import bigCityGenerator

os.system("mkdir output")

with open("SETTINGS.json", "r") as f:
    data = json.load(f)

numberOfPersons = int(data["numberOfPersons"])
min_age = int(data["minAge"])
max_age = int(data["maxAge"])

start = time.time()

first_name = firstNameGenerator.generate()
print("Got the first names!")
last_name = lastNameGenerator.generate()
print("Got the last names!")
big_city = bigCityGenerator.generate()
print("Got the cities!")

if data["csv"]:
    print("Writing csv file!")
    with open('output/output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["first_name", "last_name", "age", "city"])
        
        for _ in range(numberOfPersons):
            csv_writer.writerow([random.choice(first_name), random.choice(last_name), random.randint(min_age, max_age), random.choice(big_city)])
    
if data["json"]:
    print("Writing json file!")
    with open("output/output.json", "w") as f:
        dict = {}
        for i in range(numberOfPersons):
            dict[i] = {"first_name": random.choice(first_name), "last_name": random.choice(last_name), "age": random.randint(min_age, max_age), "city": random.choice(big_city)}
        json.dump(dict, f, indent=2)
    
print(f"Done in: {time.time() - start} seconds.")