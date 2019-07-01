import earthquakes

earthquake_data = earthquakes.get_earthquakes()

earthquake_counts = {}

for earthquake in earthquake_data: 
    location_name = earthquake["location"]["name"]

    if location_name not in earthquake_counts: 
        earthquake_counts[location_name] = 0

    earthquake_counts[location_name] += 1 

for name, count in earthquake_counts.items(): 
    print(name + ": " + str(count))

