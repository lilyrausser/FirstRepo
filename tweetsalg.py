import json 

positive_tweet = 0
negative_tweet = 0

with open("positive.json") as positive_file: 
   positive_words = json.load(positive_file) 
with open("negative.json") as negative_file: 
    negative_words = json.load(negative_file)

    
with open("tweets_small.json") as infile: 
    total_tweets = json.load(infile)

    for tweet in total_tweets: 
        substrings = tweet['text'].split(" ")
        print(substrings)
        score = 0
        for text in substrings: 
            if text in positive_words is positive_tweet: 
                score += 1
            if text in negative_words is negative_tweet: 
                sccore -= 1
                break

                
            
        


#valid??

    # positive_words_in_tweet = [str(el) for el in substrings if el.ispositive()]
    # negative_words_in_tweet = [str(el) for el in substrings if el.isnegative()]

# with open("positive.json", "w", encoding="utf-8") as outfile: 
#     json.dump("positivedump", outfile, ensure_ascii=False, indent=2)
# with open("positive.json") as infile: 
#     data = json.load(infile)

# #with open("negative.json", "e", encoding= 'utf-8') as outfile: 
#     json.dump("negativedump", outfile, ensure_ascii=False, indent = 2)
# with open("negative.json") as infile: 
#         data = json.load(infile)



