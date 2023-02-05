response = {
    "error": None,
    "data": [ # This is a list of dictionaries
        {
            "name": "John Smith",
            "hobby": ["Gaming", "Eating"]
        },
        {
            "name": "Terry Blue",
            "hobby": ["Reading"]
        },
        {
            "name": "Alex Brown",
            "hobby": ["Writing", "Cooking", "Sport"]
        }
    ]
}

people = response["data"]
for person in people:
    if person["name"] == "Alex Brown":
        hobbies = person["hobby"]
    
print("Alex Brown's hobbies are")
for hobby in hobbies:
    print(hobby)
