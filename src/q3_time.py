from typing import List, Tuple
import pandas as pd
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    
    # Create a DataFrame from the JSON data
    df = pd.json_normalize(data)

    mentions = []
    for mentioned_users in df['mentionedUsers']:
        if mentioned_users:
            mentions.extend([user['username'] for user in mentioned_users])
    
    mentions = []
    for mentioned_users in df['mentionedUsers']:
        if mentioned_users:
            mentions.extend([user['username'] for user in mentioned_users])
    
    # Get the top 10 most mentioned users
    mention_counts = pd.Series(mentions).value_counts().nlargest(10)
    
    
    # Return as a list of tuples (user, count)
    return mention_counts.items()
