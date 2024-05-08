# Define a dictionary to store information about a person
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Print the person's name
print("Name:", person["name"])

# mengubah entri yang sudah ada
person["age"] = 31

# menambah entri baru
person["job"] = "Software Engineer"

# Print the updated information
print("Age:", person["age"])
print("City:", person["city"])
print("Job:", person["job"])
print(person)