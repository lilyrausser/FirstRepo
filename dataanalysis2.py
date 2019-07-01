import json

total_sum = 0
valid_entries = 0

with open("family.json") as infile: 
    family_data = json.load(infile)

    for person in family_data: 
        number_people_input = person["Number of people in your family"]

        if type(number_people_input) == str:
            substrings = number_people_input.split(" ")

            numbers_in_list = [int(el) for el in substrings if el.isdigit()]

            if len(numbers_in_list) == 1:
                total_sum += numbers_in_list[0]
                valid_entries += 1
                
        elif type(number_people_input) == int:
            total_sum += number_people_input
            valid_entries += 1

            average = total_sum / valid_entries

            print('{0:.3g}'.format(average))



