from typing import List, Tuple
import json
from collections import Counter
from memory_profiler import profile

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:

    mention_counts = Counter()
    
    # Process the JSON file line by line
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            mentioned_users = tweet.get('mentionedUsers', [])
            if mentioned_users is not None:
                for user in mentioned_users:
                    mention_counts[user['username']] += 1
    
    # Get the top 10 most mentioned users
    top_mentions = mention_counts.most_common(10)
    
    # Return as a list of tuples (user, count)
    return top_mentions