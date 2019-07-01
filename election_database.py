
import json

with open("election.json") as infile: 
     election = json.load(infile)


election_counts = {}
election_data_output = {}

# for election in election: 
#    location_name = election["Location"]["State Abbreviation"]

#    if location_name not in election_counts: 
#        election_counts[location_name] = 0 



for data in election:
    state_name = data["Location"]["State"]

    if state_name not in election_data_output: 
        election_data_output[state_name] = {}

    for candidate_name, vote_data in data["Vote Data"].items():
        if candidate_name not in election_data_output[state_name]: 
            election_data_output[state_name][candidate_name] = 0
        election_data_output[state_name][candidate_name] += vote_data["Number of Votes"]

total_winner = vote_data["Number of Votes"]

# def winner(input): 
#     votes = candidate_name(input)
#     dict = {}
#     for value in votes.values(): 
#         dict[value] = []
#     for(key,value) in votes.iteritems():
#         dict[value].append(key)
#     maxVote = sorted(dict.keys(), reverse = True)[0]
#     if len([maxVote]) > 1:
#         print(sorted(dict[maxVote])[0])
#     else: 
#         print(dict[maxVote][0])

# __name__ == "__main__"
# input = ("election22.json")
# winner(input)

with open("election22.json") as infile: 
    election_state = json.load(infile)

election_nation_output = {}

for state_name, candidate_votes in election_state.items(): 

    for candidate_name, candidate_votes in candidate_data.items(): 
        if candidate_name not in election_nation_output: 
            election_nation_output[candidate_name] = 0

            election_nation_output[candidate_name] += candidate_votes

with open("election23.json", "w", encoding= "utf-8") as outfile: 
    json.dump(election23.json, outfile, ensure_ascii = False, indent=2)

with open("election22.json", "w", encoding="utf-8") as outfile:
    json.dump(election_data_output, outfile, ensure_ascii=False, indent=2)


#bar graph 

# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt
# import json

# objects = ("election22.json")
# y_pos = np.arange(len(objects))
# performance = [10,8,6,4,2,1]

# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('2016 Election Results')

# plt.show()
