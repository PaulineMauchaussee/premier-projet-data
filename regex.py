import pandas as p
import re


file_path ="clients.csv"
data = p.read_csv(file_path)
print(data.head())

data['birthdate'] = p.to_datetime(data['birthdate'], format="%m-%d-%Y")   

#formater le string comme on le souhaite)
data['birthdate'] = data['birthdate'].dt.strftime("%d, %m, %Y")
print(data)

# Regex
regex = "^[A-Za-z]{1,50}[- ']{0,1}[A-Za-z]{1,50}$"
data["lastname"][0]
print(data["lastname"][0])


