import json 

with open("positive.json") as positive_file: 
    positive_words = json.load(positive_file)

with open("negative.json") as negative_file: 
    negative_words = json.load(negative_file)

tweet_output = {}

with open("tweets_small.json") as infile:
    tweet_data = json.load(infile)

    for tweet in tweet_data: 
        tweet_text = tweet["text"]
        tweet_substrings = tweet_text.split(" ")

    for word in tweet_substrings: 
        if word in positive_words: 
            tweet_score += 1
        elif word in negative_words: 
            tweet_score -= 1
    tweet_id = tweet["id"]

    tweet_output[tweet_id] = tweet_score 

with open("tweet_output.json", "w", encoding="utf-8", indent=2):
    json.dump(tweet_output,outfile, ensure_ascii=true, indent=2)

