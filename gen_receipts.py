# This is a script that generates random receipts
#Using the random package to generate the 'ammount' that is on each receipt
#Using the choice function to generate the content for our JSON Package
#Using the 'dump' method

import random
import json
import os

# Using 'count' to define how many receipts we want to generate in this script
count = int(os.getenv("FILE_COUNT") or 100)
# using 'words' to get the list of words that want to use
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000) #generates a monetary amount
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount 
    } #setting the entire content to be a dictionary with the 'key' named as 'topic' and the 'value' as a currency
    with open(f'./new/receipt-{identifier}.json', 'w')as f:
        json.dump(content, f) #writing everything into a file that's a new directory
