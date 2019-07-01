

name = input("What is your name? ")
birthday = input("What is your date of birth? ")
age = input("What is your age? ")
home = input("Where do you call home? (city, state, county ")
live = input("How many people live in your home more than 50% of the time? ")
phone = input("How many hours per week do you spend on your phone?  ")
most_used = input("Name the app, program, or website that you use the most. ")


 
survey_results = {'name' : name ,
                    'birthday' : birthday, 
                    'age' : age,
                    'home' : home, 
                    'live' : live,
                    'phone' : phone, 
                    'most_used' : most_used,
   }
                    

import json


og_survey_results = {
    "lily": { 
        "name" : 'lily', 
        "birthday" :'09/04/2002', 
        "age" : 16, 
        "home" : 'alameda, ca, alameda', 
        "live" : 3,
        "phone" : 15, 
        "most_used" : 'instagram', 
        }, 
}

print(survey_results)

with open("survey_data.json", "w", encoding="utf-8") as outfile: 
    json.dump(survey_results, outfile, ensure_ascii=False, indent=2)

with open("survey_data.json") as infile: 
    data = json.load(infile)

    print(data)






