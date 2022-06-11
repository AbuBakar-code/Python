# Dictionary

# programing_dict = {
#     "name": "abubakar",
#     "age": "20",
#     "gender": "male",
#     "height": "5.11"   
# }

# print(programing_dict)

# for key in programing_dict:
#     print(key)
#     print(programing_dict[key])

# programing_dict["name"] = "Muhammad Abubakar"
# print(programing_dict)

# -------------------------------------------------------------------------

# Challenge 1

# students = {
#     "Harry": "81",
#     "Ron": "72", 
#     "Hermione": "99",
#     "Draco": "75",
#     "Niville": "85"
# }

# grades = {}

# for key in students:
#     if int(students[key]) >= 90 and int(students[key]) <=100:
#         grades[key] = "Outstanding"
#     elif int(students[key]) >= 81 and int(students[key]) <=90:
#         grades[key] = "Exceeds Expectations"
#     elif int(students[key]) >= 71 and int(students[key]) <= 80:
#         grades[key] = "Acceptable"
#     else:
#         print("You need to work hard")
    
# print(grades)

# -------------------------------------------------------------------------
# Dict in a Dict
# travel_log = {
#     "France": {"cities_visited": ["Paris", "xyz", "Dijon"]}
# }
# print(travel_log)
# -------------------------------------------------------------------------
# Dict in a list
# Challenge 2
# travel_log = [
#     {
#         "Country": "France",
#         "Visits": 12,
#         "Cities_visited": ["Paris", "xyz"]
#         },
#     {
#         "Country": "Pakistan",
#         "visits": 14,
#         "Cities_visited": ["Vehari", "Lahore"]
#         }
# ]

# def add_travel_log(country, visits, cities_visited):
#     new_country = {}
#     new_country["Country"] = country
#     new_country["Visits"] = visits
#     new_country["Cities_visited"] = cities_visited
#     travel_log.append(new_country)

#     print(f"You have visited {country} {visits} times")

# add_travel_log("Russia", 10, ["moscow", "St. Petersburg"])


