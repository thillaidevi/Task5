# Created a dictionary in the name of all_name_age_dict, assigned name [] and age[]into the dict
all_name_age_dict = {
    "name": ["Akshara", "Akshay", "Kayal", "Kavya", "Rakshana", "Yazhini", "Karthi"],  # List of names
    "age": [8, 3, 10, 15, 20, 25, 30]  # List of corresponding ages
}
filtered_names = list(map(lambda i: all_name_age_dict["name"][i],
                filter(lambda i: all_name_age_dict["age"][i] >= 18, range(len(all_name_age_dict["age"])))))
# Created a list using list keyword any used lambda function for the operation with the parameters,
# Maps the filtered indices to corresponding names.
# Filters indices of ages where age >= 18

# Print the filtered names
print("Names with age >= 18:", filtered_names )


