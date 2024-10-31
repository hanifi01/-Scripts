# "description": "Use range to print every second student’s name from data['students'].",
# "range_usage": "range_with_step"


students = [
    {
        "name": "Abdul Sharif",
        "email": "john.smith@example.com",
        "github": "johnsmith123"
    },
    {
        "name": "Abdullah Hanifi",
        "email": "john.smith@example.com",
        "github": "johnsmith123"
    },
    {
        "name": "Mohammad",
        "email": "alice.johnson@example.com",
        "github": "alicejohnson"
    },
    {
        "name": "Muhammad Amin",
        "email": "emma.davis@example.com",
        "github": "emmadavis89"
    },
    {
        "name": "Shirin Ziyovuddinova",
        "email": "michael.brown@example.com",
        "github": "michaelbrown"
    },
    {
        "name": "Abdulhamid Abdullajonov",
        "email": "michael.brown@example.com",
        "github": "michaelbrown"
    }
]


for i in range(1, len(students), 2):  
    print(students[i]["name"])  


