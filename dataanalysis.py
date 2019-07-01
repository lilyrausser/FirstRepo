import json

people = {}


#with open("survey_data.json", "w", encoding = "utf-8") as outfile: 
    #json.dump(survey_results, outfile, ensure_ascii = false, indent = 2)

with open("family.json") as infile:
    people = json.load(infile)

    print(people)

sum=0
average = 0
number_of_valid_people = 0


for person in people: 

    if 'Number of people in your family' in person.keys(): 
        valid_people = person['Number of people in your family']

    if type(valid_people) == int:
        sum += person['Number of people in your family']
        number_of_valid_people += 1

    else:
        for value in valid_people:
            if value.isdigit():
                sum += int(value)
                number_of_valid_people += 1
                break
            


            

                
               
average = sum / number_of_valid_people
            
print(average)
round(4.368421052631579, 1)





